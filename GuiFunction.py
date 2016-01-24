from astropy.io import fits
import numpy as np


run = [False]


class PlotFunctionality(object):

    @staticmethod
    def plot(name, start, showfit, shouldfit, degree, fig,):
        sp = fits.open(name)

        wavelength = np.float64(sp[0].data[start, :, 0])
        flux = np.float64(sp[0].data[start, :, 1])

        if showfit is True:
            spect = fig.add_subplot(1, 2, 2)
        else:
            spect = fig.add_subplot(1, 1, 1)

        if shouldfit:
            fitresults = PlotFunctionality.fitfunction(degree, wavelength, flux, spect)
            spect.plot(wavelength, fitresults['y_new'])

            if showfit is True:
                PlotFunctionality.fitshower(fig, wavelength, flux, fitresults['y_poly'])
        else:
            spect.plot(wavelength, flux)

        while run[0] is False:
            spect.set_xlabel('Wavelength (Angstroms)')
            spect.set_ylabel('Flux')
            spect.set_title('Single Order 1-D Spectra | Order number: ' + str(start))
            run[0] = True

    @staticmethod
    def fitshower(fig, wavelength, flux, y_poly):
        fitfig = fig.add_subplot(1, 2, 1)
        fitfig.plot(wavelength, flux)
        fitfig.plot(wavelength, y_poly, color='black', linewidth=2)
        fitfig.set_xlabel('Wavelength (Angstroms)')
        fitfig.set_ylabel('Flux')
        fitfig.set_title('Spectra with Function Fit')

    @staticmethod
    def fitfunction(degree, wavelength, flux, spect):
        degree = int(degree)
        z = np.polyfit(wavelength, flux, degree)
        f = np.poly1d(z)
        y_poly = f(wavelength)
        y_new = flux - y_poly
        return {'y_poly': y_poly, 'y_new': y_new}