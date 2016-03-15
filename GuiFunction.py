from astropy.io import fits
import numpy as np
from General import Mathamatics
import math
import jdcal
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
import matplotlib.pyplot as plt
from astropy.modeling import models,fitting
import jplephem
import de423
import astropy.time as astrotime
import astropy.coordinates as coords
import astropy.units as unit
import astropy.constants as const

run = [False]


# opens a log file, I don't always print to it but its nice to have handy when I want to print a lot of output
log = open('log.log', 'w')

# basic plot functionality
class PlotFunctionality(object):

    # plot mathod used by basic viewer
    @staticmethod
    def plot(name, start, showfit, shouldfit, degree, fig, offsety):
        name = str(name)
        sp = fits.open(name)
        # These are due to be replaced by wfextract()
        wavelength = np.float64(sp[0].data[start-1, :, 0])
        flux = np.float64(sp[0].data[start-1, :, 1])

        # determins wherether to show the two things
        if showfit is True:
            spect = fig.add_subplot(1, 2, 2)
        else:
            spect = fig.add_subplot(1, 1, 1)

        # determins whether to fit a function and if so fits a function and normalizes the curve
        if shouldfit:
            fitresults = PlotFunctionality.fitfunction(degree, wavelength, flux, offsety)
            spect.plot(fitresults['wave'], fitresults['y_new'])

            if showfit is True:
                PlotFunctionality.fitshower(fig, wavelength, flux, fitresults['y_poly'])
        else:
            spect.plot(wavelength, flux)

        # labels axies, graphss, and whatnot
        spect.set_xlabel('Wavelength (Angstroms)')
        spect.set_ylabel('Flux')
        spect.set_title('Single Order 1-D Spectra | Order number: ' + str(start))

    # method dealing with drawing out the fit show
    @staticmethod
    def fitshower(fig, wavelength, flux, y_poly):
        # subplot created
        fitfig = fig.add_subplot(1, 2, 1)
        fitfig.plot(wavelength, flux)
        fitfig.plot(wavelength, y_poly, color='black', linewidth=2)
        fitfig.set_xlabel('Wavelength (Angstroms)')
        fitfig.set_ylabel('Flux')
        fitfig.set_title('Spectra with Function Fit')

    # deals with flux normalizing the data
    @staticmethod
    def fitfunction(degree, wavelength, flux, offset):
        # two lists for later use in the function
        newwave = []
        newflux = []

        # ignored Hydrogen alpha and beta, this will latter be turned into a profile thing, using more or less the same
        # code used in ccor, however for now this works
        for j in range(len(wavelength)):
            if (wavelength[j] >= 4855 and wavelength[j] <= 4867) or (wavelength[j] >= 6554 and wavelength[j] <= 6570):
                pass
            else:
                newwave.append(wavelength[j])
                newflux.append(flux[j])
        # typecats BECAUSE I CAN, also BECAUSE IT NEEDS TO HAPPEN FOR CODE TO RUN
        degree = int(degree)
        # bear with me for the section, its kinda jankey
        # Fits a function z to the data with highest exponent degree
        z = np.polyfit(newwave, newflux, degree)
        # creats a function f which is z(something)
        f = np.poly1d(z)
        # creates all the y values for the function fit
        y_poly = f(newwave)
        # divides out the function fit to the flux to normalize it
        y_new = newflux / y_poly
        # for kicks
        y_fit = y_new
        # standard deviation and mean of the normalized flux
        fluxstdev = np.std(y_new)
        mean = np.mean(y_new)
        forrange = len(y_new)

        # this loop removes all values more than 3 sigma away from the mean, that will become user definable, it ignores
        # all values more than 3 sigma from the mean, removing those that are greater than the mean, (since they are most
        # likely cosimic rays) and just ignoring those that are below the mean
        for i in range(forrange):
            if y_new[i] >= (3 * fluxstdev) + mean:
                y_new[i] = mean
                y_fit[i] = mean
            if y_new[i] <= mean - (3 * fluxstdev):
                y_fit[i] = mean

        # this reintroduces the trend into the data (now with outlies removed)
        flux2 = y_fit * y_poly
        # goes threw the prosses of refitting the curve to the data sans outliers now
        z = np.polyfit(newwave, flux2, degree)
        f = np.poly1d(z)
        y_poly = f(wavelength)
        y_new = flux / y_poly

        # I honesetly don't know what this does any more, I will figure that out at some point (this is why I need to get
        # better at commenting b/c I wrote that like a week ago, but I don't know why I wrote that)
        for i in range(forrange):
            if y_new[i] >= (3 * fluxstdev) + mean:
                y_new[i] = mean
        # appled an artificial offset to the flattened data so that it can be seen better
        if offset != 0:
            for j in range(len(y_new)):
                y_new[j] += offset
        # returnes a dictionary of values, dictionary returns are the best and should be more widely known
        return {'y_poly': y_poly, 'y_new': y_new, 'wave': wavelength}

    # wavelength and flux extract method, this will soon replace all non method instances of this code for better modularization
    @staticmethod
    def wfextract(path, order):
        path = str(path)
        sp=fits.open(path)

        wavelength = np.float64(sp[0].data[order, :, 0])
        flux = np.float64(sp[0].data[order, :, 1])

        return {'wavelength': wavelength, 'flux': flux}

class AdvancedPlotting(PlotFunctionality):

    # correlation math / logic
    @staticmethod
    def ccor(targetpath, templatepath, degree, order, numberignore, largerwave, smallerwave, value):
        # local namespace arrays and variables used throuout, I don't have a problem useing these here because they are
        # local
        targetflux = []
        templateflux = []
        correlation = []
        correlationbad = []
        offset = []

        # These call the wfextract function to get the flux and wavelength for the target and template as a dictionary
        targetdata = PlotFunctionality.wfextract(targetpath, order)
        templatedata = PlotFunctionality.wfextract(templatepath, order)
        newtargetwave = []
        newtargetflux = []
        newtemplatewave = []
        newtemplateflux = []
        # Finds the largest and smallest wavelengths in the the target for the given order
        largest = Mathamatics.largest(targetdata['wavelength'])
        smallest = Mathamatics.smallest(targetdata['wavelength'])

        # this next large block of code is what deals with ignoring certain wavelengths, this is a mildly optimized
        # version (way more that before at least) and it makes sure to only take wavelengths into account that are not
        # in the range specified by the user
        for n in range(numberignore):

            # This checks when the smaller wavelength is and if it falls in the range of the array it will then preform
            # more checks, if not it will move on
            if smallest < smallerwave[n] < largest:

                # This checks if the largest wavelength is in the range of the array,
                if smallest < largerwave[n] < largest:
                    for j in range(len(targetdata['wavelength'])):
                        # Checks if the target wavelength is in in the range of the ignore, if so passes
                        if smallerwave[n] <= targetdata['wavelength'][j] <= largerwave[n]:
                            pass
                        else:
                            # Does the actual appending of the new data, only appends if the range is not inbetween the
                            # ignore ranges
                            newtargetwave.append(targetdata['wavelength'][j])
                            newtargetflux.append(targetdata['flux'][j])
                            newtemplatewave.append(templatedata['wavelength'][j])
                            newtemplateflux.append(templatedata['flux'][j])
                # if the largest is not in the array
                else:
                    # Same more or less logic than above
                    for j in range(len(targetdata['wavelength'])):
                        if smallerwave[n] <= targetdata['wavelength'][j] <= largest:
                            pass
                        else:
                            newtargetwave.append(targetdata['wavelength'][j])
                            newtargetflux.append(targetdata['flux'][j])
                            newtemplatewave.append(templatedata['wavelength'][j])
                            newtemplateflux.append(templatedata['flux'][j])
            elif smallest < largerwave[n] < largest:
                for j in range(len(targetdata['wavelength'])):
                    if smallest <= targetdata['wavelength'][j] <= largerwave[n]:
                        newtargetwave.append(targetdata['wavelength'][j])
                        newtargetflux.append(targetdata['flux'][j])
                        newtemplatewave.append(templatedata['wavelength'][j])
                        newtemplateflux.append(templatedata['flux'][j])
            else:
                # if there are no wavelengths to ignore then it sets the new use arrays to the target data relevent
                newtargetwave = targetdata['wavelength'].tolist()
                newtargetflux = targetdata['flux'].tolist()
                newtemplatewave = templatedata['wavelength'].tolist()
                newtemplateflux = templatedata['flux'].tolist()

        # Gets the target flux and normalizes it by calling the functional fitting function
        targetflux.append(PlotFunctionality.fitfunction(degree, newtargetwave, newtargetflux, 0)['y_new'])
        # the targetflux array (and acrually all arrays returned from fitfunction) are multidimensional, in this case
        # we only want the first element of that
        targetflux = targetflux[0]
        targetflux[:] = [x - 1 for x in targetflux]
        # trims down the target flux array to the fixed window size, at some point this will be user controllable
        # plt.plot(targetflux)
        # plt.draw()
        # time.sleep(10)
        # plt.close()
        # Here we obtain the right honorable template flux of the land and do do unto it the normalization which has
        # been decreade should be done unto it and it was done unto it, and I dont know why I type these things sometimes
        templateflux.append(PlotFunctionality.fitfunction(degree, newtemplatewave, newtemplateflux, 0)['y_new'])
        # same thing as above, wanting only the first element and whatnot
        templateflux = templateflux[0]
        templateflux = templateflux[(value/2):-(value/2)]
        templateflux[:] = [x - 1 for x in templateflux]

        # This does the actual shifting
        for i in range(value):
            # creates a new array equal to the total template flux array
            shiftflux = targetflux
            shiftwave = newtargetwave
            #crops the array so that only the part that lies under the part of the template being inveseigated matters
            shiftflux = shiftflux[i:-(value-i)]
            shiftwave = shiftwave[i:-(value-i)]


            # correlates the two arrays of fluxes and appends that to an array

            correlationbad.append(np.correlate(templateflux, shiftflux))
            print len(correlationbad)
            z = templateflux - shiftflux
            savez = z
            z = [x**2 for x in z]
            z = sum(z)
            z /= (len(shiftflux)-1)
            z = math.sqrt(z)
            bottom = math.sqrt((np.std(templateflux)**2)+(np.std(shiftflux)**2))
            z /= bottom
            correlation.append(z)

            # plt.plot(templateflux, label=str(np.correlate(templateflux, shiftflux)))
            # plt.plot(shiftflux)
            # plt.legend()
            # plt.show()
            # plt.pause(0.1)
            # plt.close()
            # appends whatever the offset relative to 0 is (reconnizing that the offset is half on oneseid and half on another)
            offset.append((value/2)-i)
        savecor = correlation
        correlation = [abs(x - max(savecor)) for x in savecor]
        g_init = models.Gaussian1D(amplitude=max(correlation), mean=0, stddev=2.)
        fit_g = fitting.LevMarLSQFitter()
        g = fit_g(g_init, offset, correlation)
        waverange = (max(newtargetwave)) - (min(newtargetwave))
        pixrange = len(newtargetwave)
        dispersion = waverange/pixrange
        #return{'correlation': correlation, 'offset': offset, 'fit': g, 'dispersion': dispersion}
        return{'correlation': correlationbad, 'offset': offset, 'fit': g, 'dispersion': dispersion}

    # This method deals with showing the wavelengths in the cross correlation chart, basically it allows one to see
    # what is being cross correlated, which is helpful for you know...SCIENCE
    @staticmethod
    def waveshower(fig, path1, path2, order, degree):
        # I have yet to figure out if my nearly obsessive use of local and global name space arrays for basically everything
        # in some way goes against python best practices (I get hints that maybe it does). I think maybe I should be using
        # something like pandas dataframes, or numpy arrays, but those are all big words that I dont want to think about
        # all that being said, here are two lists
        flux1 = []
        flux2 = []
        # gets the data from the two files
        data1 = PlotFunctionality.wfextract(path1, order)
        data2 = PlotFunctionality.wfextract(path2, order)
        # Normalizes the data from the two functions
        flux1.append(PlotFunctionality.fitfunction(degree, data1['wavelength'], data1['flux'], 0)['y_new'])
        flux2.append(PlotFunctionality.fitfunction(degree, data2['wavelength'], data2['flux'], 0)['y_new'])
        flux1[:] = [x - 1 for x in flux1]
        flux2[:] = [x -1 for x in flux2]
        # creats the wubplot, and places it, using the system that I FINALY figured out, just so I wont forget, or so that
        # when I forget I will be able to reference this and relearn quicickly, the position (x, y, z) basically is what
        # fraction of the screen you will take up so (1, 1, 1) is all of the x all of the z and all of the y (2, 1, 1,)
        # is half of the x all of the y and all of the z, so (2, 1, 2) is half of the all of the y and half of the z
        waves = fig.add_subplot(2,1,2)
        # Plots data, what more do you want
        waves.plot(data1['wavelength'], flux1[0])
        waves.plot(data2['wavelength'], flux2[0])
        # Labes some stuff
        waves.set_xlabel('wavelength (Angstroms)')
        waves.set_ylabel('Normalized Flux')
        waves.set_title('spectra viewer')

    # Here we see a fine example of unused functions in the prime of there unuseness, they are presitinly not being used
    # anywher in the code, serve absouluty no pourpous other than to amuse me, and only still exist because I will enjoy
    # typing this comment out more than I will deleating the code.
    @staticmethod
    def listcomp(list1, list2):
        same = False
        if len(list1) == len(list2):
            same = True
        return same

    @staticmethod
    def openlist(filename):
        listactual = open(filename, 'rb')
        listarray = []
        for line in listactual:
            listarray.append(line)
        return listarray
    # End the unused section of code

###################
##  Experimental ##
###################

# Here is the experimental HJD correction code, it is currently very rough and does not work

    @staticmethod
    def coordconvert(name):
        name = str(name)
        # This is basic read in stuff, its used the same at other points in the code, same idea here
        hdulist = fits.open(name)
        RA = hdulist[0].header['RA']
        Dec = hdulist[0].header['Dec']
        RA= RA.split(':')
        Dec= Dec.split(':')
        # typecats all the enteries in RA and Dec from strs to floats
        for i in range(len(RA)):
            RA[i] = float(RA[i])
            Dec[i] = float(Dec[i])
        ObsDate = hdulist[0].header['DATE']

        # Parses the time from the header into years months and dates, for latter use in JD converter
        Year = int(ObsDate[:-15])
        Month = int(ObsDate[5:-12])
        Day = int(ObsDate[8:-9])
        # Calculate the Julian Date
        JD = sum(jdcal.gcal2jd(Year, Month, Day))

        # Convert to JD2000
        J2 = JD - 2451545.0

        # This calculates the distance to the sun on a given Julian Date, these at some point need to be modified, however
        # this should work for the time being
        MeanLon = 280.460 + 0.9856474 * J2
        MeanAnon = 357.528 + 0.9856003 * J2
        cont = False
        # corrects for, and places the mean annomoly in the range of 360
        while cont is False:
            if MeanAnon > 360:
                MeanAnon -= 360
            elif MeanAnon < 0:
                MeanAnon += 360
            else:
                cont = True
        cont = False
        # does the same thing for mean longitude
        while cont is False:
            if MeanLon > 360:
                MeanLon -= 360
            elif MeanLon < 0:
                MeanLon += 360
            else:
                cont = True
        # calculates values for use in the HJD Calculation
        EcclipticLon = MeanLon + 1.915*math.sin(MeanAnon) + 0.020*math.sin(2*MeanAnon)
        SolarDist = 1.00014 - 0.01671*math.cos(MeanAnon) - 0.00014*math.cos(2*MeanAnon)
        HJD = AdvancedPlotting.jd_corr(J2, name, jd_type='hjd')
        print 'in function:', HJD
        BJD = AdvancedPlotting.jd_corr(J2, name, jd_type='bjd')
        print 'in function:', BJD

        # The Next section here calculates the Unit vector pointed at the target

        return {'HJD': HJD, 'BJD': BJD}

    # https://mail.scipy.org/pipermail/astropy/2014-April/003148.html
    @staticmethod
    def jd_corr(mjd, filename, jd_type='hjd'):
        hdulist = fits.open(filename)
        RA = hdulist[0].header['RA']
        Dec = hdulist[0].header['Dec']
        CTIO_LON = 30.1697
        CTIO_LAT = 70.8065
        # Initialise ephemeris from jplephem
        eph = jplephem.Ephemeris(de423)

        # Source unit-vector
        ## Assume coordinates in ICRS
        ## Set distance to unit (kilometers)
        src_vec = coords.ICRS(ra=RA, dec=Dec, unit=(unit.degree, unit.degree), distance=coords.Distance(1, unit.km))

        # Convert epochs to astropy.time.Time
        ## Assume MJD(UTC)
        t = astrotime.Time(mjd, scale='utc', format='mjd')#lat=CTIO_LAT, lon=CTIO_LON)

        # Get Earth-Moon barycenter position
        ## NB: jplephem uses Barycentric Dynamical Time, e.g. JD(TDB)
        ## and gives positions relative to solar system barycenter
        barycenter_earthmoon = eph.position('earthmoon', t.tdb.jd)

        # Get Moon position vectors
        moonvector = eph.position('moon', t.tdb.jd)

        # Compute Earth position vectors
        pos_earth = (barycenter_earthmoon - moonvector * eph.earth_share)*unit.km

        if jd_type == 'bjd':
            # Compute BJD correction
            ## Assume source vectors parallel at Earth and Solar System Barycenter
            ## i.e. source is at infinity
            corr = np.dot(pos_earth.T, src_vec.cartesian.value)/const.c
        elif jd_type == 'hjd':
            # Compute HJD correction via Sun ephemeris
            pos_sun = eph.position('sun', t.tdb.jd)*unit.km
            sun_earth_vec = pos_earth - pos_sun
            corr = np.dot(sun_earth_vec.T, src_vec.cartesian.value)/const.c
        else:
            return '<font color="red">ERROR, CORRECTION TYPE NOT SPECIFIED OR SPELLED WRONG</font>'

        # TDB is the appropriate time scale for these ephemerides
        dt = astrotime.TimeDelta(corr, scale='tdb', format='jd')
        # Compute and return HJD/BJD as astropy.time.Time
        new_jd = t + dt
        return new_jd

    # fits and plots a gaussian function to certain spectral lines
    @staticmethod
    def gaussianfit(filename, upper, lower, plotnumber):
        allwave = []
        allflux = []
        xvalue = []
        yvalue = []
        maxvalue = []
        for run in range(62):   # pulls out wavelength and flux values from the fits file
            data = PlotFunctionality.wfextract(filename,run)
            for ted in range(len(data['wavelength'])):
                allwave.append(data['wavelength'][ted])
                allflux.append(data['flux'][ted])
        selection = [lower,upper]
        wavenew = []
        fluxnew = []
        for i in range(len(selection)):
            lower = min(range(len(allwave)), key=lambda k: abs(allwave[k]-selection[0]))
            upper = min(range(len(allwave)), key=lambda k: abs(allwave[k]-selection[1]))

            for j in range(len(allwave)):   # gives the wavelength between the uper and lower bounds
                if lower<j<upper:
                    wavenew.append(float(allwave[j]))
                    fluxnew.append(float(allflux[j]))

            x = ar(wavenew)   # ar() turns wavenew and fluxnew into arrays
            y = ar(fluxnew)
            n = len(x)

            normx = []
            normy = []
            degree = 4

            for j in range(len(x)):   # fills in normx and normy
                normx.append(x[j])
                normy.append(y[j])
            z = np.polyfit(normx,normy,degree)
            f = np.poly1d(z)
            ypoly = f(normx)
            ynew = normy/ypoly
            yfit = ynew
            fluxstdev = np.std(ynew)
            mean = np.mean(ynew)
            forrange = len(ynew)

            for i in range(forrange):   # this replaces anything within 3sigma with the mean
                if ynew[i] >= (3*fluxstdev) + mean:
                    ynew[i] = mean
                    yfit[i] = mean
                if ynew[i] <= mean - (3*fluxstdev):
                    yfit[i] = mean

            flux2 = yfit * ypoly
            z = np.polyfit(normx,flux2,degree)
            f = np.poly1d(z)
            ypoly = f(x)
            ynew = y/ypoly

            def gaus(x,a,x0,sigma,offset):
                return (-a*exp(-(x-x0)**2/(2*sigma**2))) + offset   # where offset is the offset of the spectra
            center = allwave[(upper-((upper-lower)/2))]
            gaussy,gaussx = curve_fit(gaus,normx,ynew,p0=[.5,center,5,.7])
            maximum = max(gaussy)
            wavenew = None
            fluxnew = None
            wavenew = []
            fluxnew = []
            xvalue.append(gaussx)
            yvalue.append(gaussy)
            maxvalue.append(maximum)

            fignewton = plt.figure()
            figothernewton = fignewton.add_subplot(1,1,1)
            figothernewton.plot(normx, ynew)
            figothernewton.plot(x,gaus(x,*gaussy))
            if plotnumber == 1:
                plt.title('Hydrogen Alpha')
            elif plotnumber == 2:
                plt.title('Hydrogen Beta')
            elif plotnumber == 3:
                plt.title('Helium I')

            plt.show()
            # plt.pause(5)


        return 0


    ## TOUCH THE COW
    ## DO IT NOW

    ## Code to pull from text file and run the gaussian fit thingy. ##

    @staticmethod
    def waveselection(filename,hydrogena,hydrogenb,heliuma):
       wave1 = open('lines.sec','rb') # opens file to read line wavelengths
       wave1 = wave1.readlines()
       length = len(wave1)

       for i in range(length):
           wave1[i] = wave1[i].split('-') # splits the strings
           wave1[i][1] = wave1[i][1][:-1] # gets rid of the newline character
           wave1[i] = [float(x) for x in wave1[i]]
       wave2=[0,0]
       if hydrogena is False:
           pass
       elif hydrogena is True:
           wave2=wave1[0]
           AdvancedPlotting.gaussianfit(filename,wave2[1],wave2[0],1)   # runs the fitting function with wavelengths
       if hydrogenb is False:
           pass
       elif hydrogenb is True:
           wave2=wave1[1]
           AdvancedPlotting.gaussianfit(filename,wave2[1],wave2[0],2)
       if heliuma is False:
           pass
       elif heliuma is True:
           wave2=wave1[2]
           AdvancedPlotting.gaussianfit(filename,wave2[1],wave2[0],3)
       return 0
