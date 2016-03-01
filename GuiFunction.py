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
import ephem
import astropy.time as astrotime
import astropy.coordinates as coords
import astropy.units as unit
import astropy.constants as const
import Astrolib

run = [False]

#  opens a log file, I don't always print to it but its nice to have handy when I want to print a lot of output
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
        # wavelength = np.float64(sp[0].data[1, start-1, :])
        # flux = np.float64(sp[0].data[2, start-1, :])
        # fitsdata = sp[1].data
        data = sp[0].data
        print sp[0].data.shape

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
        correlationnp = []
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
        croped = False
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
                        if smallerwave[n] <= targetdata['wavelength'][j] <= largerwave[n]:
                            pass
                        else:
                            newtargetwave.append(targetdata['wavelength'][j])
                            newtargetflux.append(targetdata['flux'][j])
                            newtemplatewave.append(templatedata['wavelength'][j])
                            newtemplateflux.append(templatedata['flux'][j])
                croped = True
            elif smallest < largerwave[n] < largest:
                for j in range(len(targetdata['wavelength'])):
                    if smallerwave[n] <= targetdata['wavelength'][j] <= largerwave[n]:
                        pass
                    else:
                        newtargetwave.append(targetdata['wavelength'][j])
                        newtargetflux.append(targetdata['flux'][j])
                        newtemplatewave.append(templatedata['wavelength'][j])
                        newtemplateflux.append(templatedata['flux'][j])
                croped = True
            #else:
            #print 'in the final else'
            # if there are no wavelengths to ignore then it sets the new use arrays to the target data relevent
        if croped is False:
            newtargetwave = targetdata['wavelength'].tolist()
            newtargetflux = targetdata['flux'].tolist()
            newtemplatewave = templatedata['wavelength'].tolist()
            newtemplateflux = templatedata['flux'].tolist()
        else:
            pass

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
        meantemp = sum(newtemplatewave)/len(newtemplatewave)

        # This does the actual shifting
        for i in range(value):
            # creates a new array equal to the total template flux array
            shiftflux = targetflux
            shiftwave = newtargetwave
            #crops the array so that only the part that lies under the part of the template being inveseigated matters
            shiftflux = shiftflux[i:-(value-i)]
            shiftwave = shiftwave[i:-(value-i)]


            # correlates the two arrays of fluxes and appends that to an array


            correlationnpvalue = np.correlate(templateflux, shiftflux)
            # print correlationnpvalue
            correlationnp.append(correlationnpvalue[0])
            z = templateflux - shiftflux
            savez = z
            z = [x**2 for x in z]
            z = sum(z)
            z /= (len(shiftflux))
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
        # g_init = models.Gaussian1D(amplitude=max(correlation), mean=0, stddev=2.)
        # fit_g = fitting.LevMarLSQFitter()
        # g = fit_g(g_init, offset, correlation)
        def gaus(x,a,x0,sigma, offset):
            return (-a*exp(-(x-x0)**2/(2*sigma**2))) # + offset # where offset is the offset of the spectre
        waverange = (max(newtargetwave)) - (min(newtargetwave))
        pixrange = len(newtargetwave)
        dispersion = waverange/pixrange
        # return{'correlation': correlation, 'offset': offset, 'fit': gaus, 'dispersion': dispersion, 'meantemp': meantemp}
        return{'correlation': correlationnp, 'offset': offset, 'fit': gaus, 'dispersion': dispersion, 'meantemp': meantemp}

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
        DateOBS = hdulist[0].header['UTSHUT']
        TimeEPX = hdulist[0].header['EXPTIME']
        # print DateOBS
        YearShut = int(DateOBS[:4])
        MonthShut = int(DateOBS[5:7])
        DayShut = int(DateOBS[8:10])
        Hour = int(DateOBS[11:13])
        Minute = int(DateOBS[14:16])
        second = float(DateOBS[17:])
        second += (float(TimeEPX)/2)
        Mtotal = (second/60)+ Minute
        Htotal = (Mtotal/60) + Hour
        DayAdd = Htotal/24
        # Parses the time from the header into years months and dates, for latter use in JD converter
        # Calculate the Julian Date
        JD = sum(jdcal.gcal2jd(YearShut, MonthShut, DayShut))
        JD = JD + DayAdd
        # Convert to JD2000
        # MJD = JD - 2451545.0
        MJD = JD - 2400000.5

        # This calculates the distance to the sun on a given Julian Date, these at some point need to be modified, however
        # this should work for the time being
        MeanLon = 280.460 + 0.9856474 * MJD
        MeanAnon = 357.528 + 0.9856003 * MJD
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
        RAfromHDU = hdulist[0].header['RA']
        DecfromHDU = hdulist[0].header['DEC']
        # print 'Object RA and DEC:', RAfromHDU, DecfromHDU
        RAHour = int(RAfromHDU[:2])
        RAMinute = int(RAfromHDU[3:5])
        RASecond = float(RAfromHDU[6:])
        DecDegrees = int(DecfromHDU[:2])
        DecMinute = int(DecfromHDU[3:5])
        DecSecond = float(DecfromHDU[6:])
        #RATotalMin = RAMinute + (RASecond/240)
        RADegrees = (RAHour*15)+(RAMinute/4) + (RASecond/240)
        # print 'RA Object Degrees:', RADegrees
        RARadians = (RADegrees/360)*2*math.pi
        # print 'RA Object Radians:', RARadians
        DecTotalMin = DecMinute + (DecSecond/60)
        DecTotalDegrees = DecDegrees + (DecTotalMin/60)
        # print 'Dec Object Degrees:', DecTotalDegrees
        DecRadians = (DecTotalDegrees/360)*2*math.pi
        # print 'Dec Object Radians:', DecRadians
        eph = jplephem.Ephemeris(de423)
        pos_sunjpl = eph.position('Sun', JD)
        pos_earthjpl = eph.position('earthmoon', JD)
        EarthToSun = pos_sunjpl-pos_earthjpl
        sunDist = math.sqrt((EarthToSun[0]**2)+(EarthToSun[1]**2) + (EarthToSun[2]**2))#*unit.km
        sun = ephem.Sun()
        useDate = str(YearShut) + '/' + str(MonthShut) + '/' + str(DayShut+DayAdd)
        sun.compute(useDate)
        sunRA = str(sun.ra)
        sunDEC = str(sun.dec)
        # sunRA = '17:13:54.10'
        # sunDEC = '-23 00 50.9'
        # print sunRA, sunDEC
        RASunHour = int(sunRA[:2])
        RASunMinute = int(sunRA[3:5])
        RASunSecond = float(sunRA[6:])
        DecSunDegrees = int(sunDEC[:2])
        DecSunMinute = int(sunDEC[4:6])
        DecSunSecond = float(sunDEC[7:])
        #RASunTotalMin = RASunMinute + (RASunSecond/60)
        RASunDegrees = (RASunHour*15)+(RASunMinute/4) + (RASunSecond/240)
        # print 'RA sun Degrees:', RASunDegrees
        RASunRadians = (RASunDegrees/360)*2*math.pi
        # print 'RA sun Radians:', RASunRadians
        DecSunTotalMin = DecSunMinute + (DecSunSecond/60)
        DecSunTotalDegrees = DecSunDegrees + (DecSunTotalMin/60)
        # print 'Dec Sun Degrees:', DecSunTotalDegrees
        DecSunRadians = (DecSunTotalDegrees/360)*2*math.pi
        # print 'Dec Sun Radians:', DecSunRadians
        # print sunRA, sunDEC
        # calculates values for use in the HJD Calculation
        EcclipticLon = MeanLon + 1.915*math.sin(MeanAnon) + 0.020*math.sin(2*MeanAnon)
        # Solar Distance in AU
        SolarDist = 1.00014 - 0.01671*math.cos(MeanAnon) - 0.00014*math.cos(2*MeanAnon)
        SolarDist *= 14959787066
        sunx = SolarDist*math.sin(DecSunRadians)*math.cos(RASunRadians)
        suny = SolarDist*math.sin(DecSunRadians)*math.sin(RASunRadians)
        sunz = SolarDist*math.cos(DecSunRadians)
        objectx = math.sin(DecRadians)*math.cos(RARadians)
        objecty = math.sin(DecRadians)*math.sin(RARadians)
        objectz = math.cos(DecRadians)
        magobject = math.sqrt(((math.sin(DecRadians)*math.cos(RARadians))**2)+
                              ((math.sin(DecRadians)*math.sin(RARadians))**2)+((math.cos(DecRadians))**2))
        objectxhat = objectx/magobject
        objectyhat = objecty/magobject
        objectzhat = objectz/magobject
        # time = distance / speed
        barveldata = Astrolib.baryvel(JD)
        vel_helio = barveldata[0]
        vel_bary = barveldata[1]
        print 'Bary Velocity is:',vel_bary, 'Helio velocity is:', vel_helio
        heliojd = Astrolib.helio_jd(MJD, RADegrees, DecDegrees)

        c = 299792458 # m/s

        HJD = MJD - (sunDist/(c/1000))*(math.sin(DecRadians)*math.sin(DecSunRadians)+math.cos(DecRadians)*
                                 math.cos(DecSunRadians)*math.cos(RARadians-RASunRadians))
        HJD = HJD + 2451545.0
        heliojd += 2400000.5
        return heliojd

    @staticmethod
    def gaussianfit(filename, hydrogenalpha, hydrogenbeta, heliumalpha):
        allwave = []
        allflux = []
        xvalue = []
        yvalue = []
        maxvalue = []
        for run in range(62):
            data = PlotFunctionality.wfextract(filename,run)
            for ted in range(len(data['wavelength'])):
                allwave.append(data['wavelength'][ted])
                allflux.append(data['flux'][ted])
        selection = AdvancedPlotting.waveselection(hydrogenalpha,hydrogenbeta,heliumalpha)
        # newwave = data['wavelength']
        # newflux = data['flux']
        wavenew = []
        fluxnew = []
        for i in range(len(selection)):
            lower = min(range(len(allwave)), key = lambda k: abs(allwave[k]-selection[i][0]))
            upper = min(range(len(allwave)), key = lambda k: abs(allwave[k]-selection[i][1]))
            print "upper:", upper, "lower:",lower

            for j in range(len(allwave)):
                if lower<j<upper:
                    #print "count",j
                    wavenew.append(float(allwave[j]))
                    fluxnew.append(float(allflux[j]))

            x = ar(wavenew)
            y = ar(fluxnew)
            n = len(x)
            print n # amount of data
            def gaus(x,a,x0,sigma,offset):
                return (-a*exp(-(x-x0)**2/(2*sigma**2))) + offset   # where offset is the offset of the spectra
            center = allwave[(upper-((upper-lower)/2))]
            print(center)
            gaussy,gaussx = curve_fit(gaus,x,y,p0=[.5,center,5,1])
            print(gaussy)
            # g_init = models.Gaussian1D(amplitude = max(fluxnew), mean = meancalc, stddev = sigma)
            # fit_g = fitting.LevMarLSQFitter()
            # g = fit_g(g_init, wavenew, fluxnew)

            plt.plot(x,gaus(x,*gaussy))
            plt.show()
            plt.pause(5)

            #maximum = max(g)
            wavenew = None
            fluxnew = None
            wavenew = []
            fluxnew = []
            xvalue.append(gaussx)
            yvalue.append(gaussy)
            #maxvalue.append(maximum)

        return {'gaussx': xvalue,'gaussy': yvalue,'maximum': maxvalue}


    ## TOUCH THE COW
    ## DO IT NOW


##################################
## Code to pull from text file. ##
##################################

    @staticmethod
    def waveselection(hydrogena,hydrogenb,heliuma):
       wave1 = open('lines.sec','rb') # opens file to read line wavelengths
       wave1 = wave1.readlines()
       length = len(wave1)

       for i in range(length):
           wave1[i] = wave1[i].split('-') # splits the strings
           wave1[i][1] = wave1[i][1][:-1] # gets rid of the newline character
           print wave1[i]
           wave1[i] = [float(x) for x in wave1[i]]
       wave2=[]
       if hydrogena is False:
           pass
       elif hydrogena is True:
           wave2.append(wave1[0])
       if hydrogenb is False:
           pass
       elif hydrogenb is True:
           wave2.append(wave1[1])
       if heliuma is False:
           pass
       elif heliuma is True:
           wave2.append(wave1[2])
       return wave2

    @staticmethod
    def gaussianfitold(x,y,a,mean,stddev):
        g_init = models.Gaussian1D(a,mean,stddev)
        fit_g = fitting.LevMarLSQFitter()
        g = fit_g(g_init,x,y)
        return g
