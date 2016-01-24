from astropy.io import fits
import numpy as np
from Correlation import Ui_CrossCore
from PyQt4 import QtGui
from PyQt4.QtGui import QApplication, QDialog
import sys

run = [False]

log = open('log.log', 'w')

class PlotFunctionality(object):

    @staticmethod
    def plot(name, start, showfit, shouldfit, degree, fig,):
        name = str(name)
        sp = fits.open(name)

        wavelength = np.float64(sp[0].data[start, :, 0])
        flux = np.float64(sp[0].data[start, :, 1])

        if showfit is True:
            spect = fig.add_subplot(1, 2, 2)
        else:
            spect = fig.add_subplot(1, 1, 1)

        if shouldfit:
            fitresults = PlotFunctionality.fitfunction(degree, wavelength, flux)
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
    def fitfunction(degree, wavelength, flux):
        degree = int(degree)
        z = np.polyfit(wavelength, flux, degree)
        f = np.poly1d(z)
        y_poly = f(wavelength)
        y_new = flux - y_poly
        return {'y_poly': y_poly, 'y_new': y_new}

    @staticmethod
    def wfextract(path, order):
        path = str(path)
        sp=fits.open(path)

        wavelength = np.float64(sp[0].data[order, :, 0])
        flux = np.float64(sp[0].data[order, :, 1])

        return {'wavelength': wavelength, 'flux': flux}

class AdvancedPlotting(PlotFunctionality):

    @staticmethod
    def ccor(targetpath, templatepath, degree):
        targetflux = []
        templateflux = []
        #for i in range(61):
        targetflux.append(PlotFunctionality.fitfunction(degree, PlotFunctionality.wfextract(targetpath, 1)['wavelength'], PlotFunctionality.wfextract(targetpath, 1)['flux'])['y_new'])
        templateflux.append(PlotFunctionality.fitfunction(degree, PlotFunctionality.wfextract(templatepath, 1)['wavelength'], PlotFunctionality.wfextract(templatepath, 1)['flux'])['y_new'])
        print >>log, 'Target Flux\n'
        print >>log, len(targetflux[0])
        print >>log, 'Template Flux\n'
        print >>log, len(targetflux[0])
        correlated = np.correlate(targetflux, templateflux)
        print correlated
        return correlated

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
