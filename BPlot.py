# Echel Spectra viewer
# Paddy Clancy and Thomas Boudreaux
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import platform
import sys
import os
from PyQt4 import QtGui
from SecondGui import Ui_Header
from astropy.modeling import models, fitting

operatings = platform.system()
print('Checking Operating System')
if operatings == 'Windows':
    print('Program does not run on Windows machines, please use a UNIX Like system to run program')
    exit()
else:
    print('OS OK')

inputArray = []
useArray = [False, False]


class Plotter(object):

    @staticmethod
    def stackplot(stackfile, allimages, num, start):
        pathList = open(stackfile, 'rb')
        pathArray = []
        for line in pathList:
            pathArray.append(line)
        if allimages is True:
            stackNum = len(pathArray)
        else:
            if num > len(pathArray):
                num = len(pathArray)
            stackNum = num


        for i in range(stackNum):
            name = pathArray[i]
            name = name[:-1]
            sp = fits.open(name)
            hdu = sp[0].header

            ordernum = start

            dateobs = (hdu['DATE-OBS'])
            objName = (hdu['OBJECT'])
            wavelength = np.float64(sp[0].data[ordernum, :, 0])
            flux = np.float64(sp[0].data[ordernum, :, 1])

            plt.plot(wavelength, flux)

        plt.xlabel('Wavelength (Angstroms)')
        plt.ylabel('Flux')
        plt.title('Single Order 1-D Spectra for ' + str(stackNum) + ' Stars | Order number: ' + str(start))
        plt.show()

    @staticmethod
    def nstackplot(name, start):
        filename = str(name)
        # opens file as a fits file using the fits function set from astropy
        sp = fits.open(filename)

        # Opens the Header file as a object hdu
        hdu = sp[0].header

        # Order number Changer (Change this to look at different orders)
        ordernum = start
        # Pulls the date from the fits header
        dateobs = (hdu['DATE-OBS'])

        # Pulls the wavelength and flux values for a given order number, stores as a numpy array
        wavelength = np.float64(sp[0].data[ordernum, :, 0])
        flux = np.float64(sp[0].data[ordernum, :, 1])

        # Plots the wavelength and flux values
        plt.plot(wavelength, flux)
        plt.xlabel('Wavelength')
        plt.ylabel('Flux')
        plt.title('Spectral Curve')

        # Initializes X11 window
        plt.show()


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Header()
        self.ui.setupUi(self)

        self.ui.generatePathFiles.clicked.connect(self.search)
        self.ui.quitBut.clicked.connect(self.end)
        self.ui.stackIm.stateChanged.connect(self.stackinput)
        self.ui.allStack.stateChanged.connect(self.allinput)
        self.ui.plotBut.clicked.connect(self.plot)

    @staticmethod
    def end():
        exit()

    @staticmethod
    def stackinput():
        useArray[0] = not useArray[0]

    @staticmethod
    def allinput():
        useArray[1] = not useArray[1]

    def search(self):
        namearray = []
        for root, dirs, files in os.walk('.', topdown=True):
            for file in files:
                if 'achi' in file:
                    filename = os.path.join(root, file)
                    sp = fits.open(filename)
                    hdu = sp[0].header
                    objname = (hdu['OBJECT'])
                    if objname not in namearray:
                        namearray.append(objname)
        for i in range(len(namearray)):
            starname = namearray[i]
            nameforfile = 'PathTo' + starname
            printlist = open(nameforfile, 'w')
            for root, dirs, files in os.walk('.', topdown=True):
                for file in files:
                    if 'achi' in file:
                        name = os.path.join(root, file)
                        sp = fits.open(name)
                        hdu = sp[0].header
                        objname1 = (hdu['OBJECT'])
                        if starname in objname1:
                            print >>printlist, name
        self.ui.generatePathFiles.setStyleSheet("background-color: green; color: white")

    def plot(self):
        if useArray[0] is True:
            pathfilename = self.ui.pathListInput.toPlainText()
            numToStack = self.ui.numStack.value()
            order = self.ui.startOrd.value()
            Plotter.stackplot(pathfilename, useArray[1], numToStack, order)
        else:
            filename = self.ui.singleFileInput.toPlainText()
            print filename
            order = self.ui.startOrd.value()
            Plotter.nstackplot(filename, order)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())