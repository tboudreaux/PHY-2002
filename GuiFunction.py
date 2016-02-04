from astropy.io import fits
import numpy as np
from General import Mathamatics
import math
import astropy.coordinates as coord
from astropy import units as u
import jdcal
run = [False]


# opens a log file, I don't always print to it but its nice to have handy when I want to print a lot of output

log = open('log.log', 'w')

# basic plot functionality
class PlotFunctionality(object):

    @staticmethod
    def plot(name, start, showfit, shouldfit, degree, fig, offsety):
        name = str(name)
        sp = fits.open(name)
        AdvancedPlotting.coordconvert(name)
        wavelength = np.float64(sp[0].data[start-1, :, 0])
        flux = np.float64(sp[0].data[start-1, :, 1])

        if showfit is True:
            spect = fig.add_subplot(1, 2, 2)
        else:
            spect = fig.add_subplot(1, 1, 1)

        if shouldfit:
            fitresults = PlotFunctionality.fitfunction(degree, wavelength, flux, offsety)
            spect.plot(fitresults['wave'], fitresults['y_new'])

            if showfit is True:
                PlotFunctionality.fitshower(fig, wavelength, flux, fitresults['y_poly'])
        else:
            spect.plot(wavelength, flux)

        spect.set_xlabel('Wavelength (Angstroms)')
        spect.set_ylabel('Flux')
        spect.set_title('Single Order 1-D Spectra | Order number: ' + str(start))


    @staticmethod
    def fitshower(fig, wavelength, flux, y_poly):
        fitfig = fig.add_subplot(1, 2, 1)
        fitfig.plot(wavelength, flux)
        fitfig.plot(wavelength, y_poly, color='black', linewidth=2)
        fitfig.set_xlabel('Wavelength (Angstroms)')
        fitfig.set_ylabel('Flux')
        fitfig.set_title('Spectra with Function Fit')

    @staticmethod
    def fitfunction(degree, wavelength, flux, offset):
        newwave = []
        newflux = []
        for j in range(len(wavelength)):
            if (wavelength[j] >= 4855 and wavelength[j] <= 4867) or (wavelength[j] >= 6554 and wavelength[j] <= 6570):
                pass
            else:
                newwave.append(wavelength[j])
                newflux.append(flux[j])
        degree = int(degree)
        z = np.polyfit(newwave, newflux, degree)
        f = np.poly1d(z)
        y_poly = f(newwave)
        y_new = newflux / y_poly
        y_fit = y_new
        fluxstdev = np.std(y_new)
        mean = np.mean(y_new)
        forrange = len(y_new)
        for i in range(forrange):
            if y_new[i] >= (3 * fluxstdev) + mean:
                y_new[i] = mean
                y_fit[i] = mean
            if y_new[i] <= mean - (3 * fluxstdev):
                y_fit[i] = mean
        flux2 = y_fit * y_poly
        z = np.polyfit(newwave, flux2, degree)
        f = np.poly1d(z)
        y_poly = f(wavelength)
        y_new = flux / y_poly
        for i in range(forrange):
            if y_new[i] >= (3 * fluxstdev) + mean:
                y_new[i] = mean
        if offset != 0:
            for j in range(len(y_new)):
                y_new[j] += offset
        return {'y_poly': y_poly, 'y_new': y_new, 'wave': wavelength}

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
    def ccor(targetpath, templatepath, degree, order, numberignore, largerwave, smallerwave):
        # local namespace arrays and variables used throuout, I don't have a problem useing these here because they are
        # local
        targetflux = []
        correlation =[]
        corwave = []

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

        # finds the differenec between the largest and smallest wavelength and then rounds that up to the nearest int
        diff = largest - smallest
        diff = int(math.ceil(diff))

        # Gets the flux and normalizes it by calling the functional fitting function
        targetflux.append(PlotFunctionality.fitfunction(degree, newtargetwave, newtargetflux, 0)['y_new'])

        # This does the actual shifting
        for i in range(2*diff):
            # More local name space variables that are jangly but okay
            templateflux = []
            usetemplateflux = []
            usetargetflux = []

            # Calculares the new Wavelength valuses for the template in each run of the cross correlation loop
            wshift = [x + diff - i + 1 for x in newtemplatewave]
            start = Mathamatics.smallest(wshift)

            # Same thing as above but for the template as opposed to the target
            templateflux.append(PlotFunctionality.fitfunction(degree, wshift, newtemplateflux, 0)['y_new'])

            # This is the section of code that is ment to deal with removing the edges of the arrays (ie the sections
            # not lines up with each other) in order to not throw off the cross correlation
            # in all honest if I had to guess this is where the problems lie
            if Mathamatics.smallest(wshift) > Mathamatics.smallest(newtargetwave):
                for k in range(len(newtargetwave)):
                    if newtargetwave[k] < start:
                        pass
                    else:
                        usetemplateflux.append(templateflux[0][k])
                        usetargetflux.append(targetflux[0][k])
            elif Mathamatics.smallest(wshift) == Mathamatics.smallest(newtargetwave):
                pass
            else:
                for k in range(len(newtargetwave)):
                    if wshift[k] < start:
                        pass
                    else:
                        usetargetflux.append(targetflux[0][k])
                        usetemplateflux.append(templateflux[0][k])
            # This is the line that does the actual correlation, passing in the adjusted fluxes
            correlation.append(np.correlate(usetargetflux, usetemplateflux))

            # This is a missnomer, wave is not in any way related to this, this is more appropriately titles
            # offsett or something, but either way its called cor wave because I wrote this late at night
            # so yea, thats a thing
            corwave.append(diff-i)

        # returns a dictionary of values (y and x values respectivly)
        return {'correlation': correlation, 'corwave': corwave}

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

    @staticmethod
    def coordconvert(name):
        hdulist = fits.open(name)
        RA = hdulist[0].header['RA']
        Dec = hdulist[0].header['Dec']
        RA= RA.split(':')
        Dec= Dec.split(':')
        for i in range(len(RA)):
            RA[i] = float(RA[i])
            Dec[i] = float(Dec[i])
        ObsDate = hdulist[0].header['DATE']
        Year = int(ObsDate[:-15])
        Month = int(ObsDate[5:-12])
        Day = int(ObsDate[8:-9])
        # Calculate the Julian Date
        JD = sum(jdcal.gcal2jd(Year, Month, Day))

        # Convert to JD2000
        J2 = JD - 2451545.0

        # This calculates the distance to the sun on a given Julian Date
        MeanLon = 280.460 + 0.9856474 * J2
        MeanAnon = 357.528 + 0.9856003 * J2
        cont = False
        while cont is False:
            if MeanAnon > 360:
                MeanAnon -= 360
            elif MeanAnon < 0:
                MeanAnon += 360
            else:
                cont = True
        cont = False
        while cont is False:
            if MeanLon > 360:
                MeanLon -= 360
            elif MeanLon < 0:
                MeanLon += 360
            else:
                cont = True
        EcclipticLon = MeanLon + 1.915*math.sin(MeanAnon) + 0.020*math.sin(2*MeanAnon)
        SolarDist = 1.00014 - 0.01671*math.cos(MeanAnon) - 0.00014*math.cos(2*MeanAnon)

        # The Next section here calculates the Unit vector pointed at the target

        Cs = coord.SkyCoord(ra=RA*u.degree, dec=Dec*u.degree)

        print Cs.ra
        print Cs.dec
        print MeanAnon, MeanLon, SolarDist, RA, Dec