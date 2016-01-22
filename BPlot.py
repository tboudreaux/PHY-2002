# Echel Spectra viewer
# Paddy Clancy and Thomas Boudreaux
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import platform
import sys, os
from PyQt4 import QtGui, QtCore
from basicgui import Ui_Header
from Bsort import Generate
# TODO  figure out how to get directories working


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Header()
        self.ui.setupUi(self)

        self.ui.generatePathFiles.clicked.connect(self.search)
        #self.ui.generatePathFiles.connect(self.search)

    def helloworld(self):
        self.ui.singleFileInput.setText("Single File Input")
        print("Hello world again")

    def search(self):
        pathArray = []
        nameArray = []
        pathList = open('PathList', 'w')
        for root, dirs, files in os.walk('.', topdown=True):
            for file in files:
                if 'achi' in file:
                    filename = os.path.join(root, file)
                    sp = fits.open(filename)
                    hdu = sp[0].header
                    objName = (hdu['OBJECT'])
                    if objName not in nameArray:
                        nameArray.append(objName)
        printArray = []
        for i in range(len(nameArray)):
            starName = nameArray[i]
            print starName, 'StarName'
            nameforFile = 'PathTo' + starName
            printList = open(nameforFile, 'w')
            for root, dirs, files in os.walk('.', topdown=True):
                for file in files:
                    if 'achi' in file:
                        name = os.path.join(root, file)
                        sp = fits.open(name)
                        hdu = sp[0].header
                        objName1 = (hdu['OBJECT'])
                        if starName in objName1:
                            print >>printList, name
        self.ui.generatePathFiles.setStyleSheet("background-color: green")

if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())

print('Packages OK')
############################
#        Pre-Code          #
############################
# General Use Variable Section

# General Yes no menu function
app = QtGui.QApplication(sys.argv[0])
window = QtGui.QWidget()

window.show()


operatingS = platform.system()

print('Checking Operating System')
if operatingS == 'Windows':
    print('Program does not run on Windows machines, please use a UNIX Like system to run program')
    exit()
else:
    print('OS OK')

print('Loading Functions')


def yesno(question):
    cont = True
    while cont is True:
        ask = raw_input(question + ' [Y/n]: ')
        if ask == 'y' or ask == 'Y':
            response = True
            cont = False
        elif ask == 'n' or ask == 'N':
            response = False
            cont = False
        else:
            print('Please enter either Y or n')
    return response
print ('Functions OK')

# General Section Dedicated to Keeping questions for functions organized
StackQuestion = "Would you like to stack orders?"
StackAll = "Would you like to stack all the images?"



# Options
ynstack = yesno(StackQuestion)

if ynstack is True:
    stackfile = raw_input("Please Enter the name of the file with the paths to the images to stack: ")
    pathList = open(stackfile, 'rb')
    pathArray = []
    for line in pathList:
        pathArray.append(line)
    allimages = yesno(StackAll)
    if allimages is True:
        stackNum = len(pathArray)
    else:
        stackNum = input('How Many images would you like to stack?: ')
    wavearray = []
    fluxarray = []
    ords = 62
    for i in range(stackNum):
        name = pathArray[i]
        name = name[:-1]
        print name
        sp = fits.open(name)
        hdu = sp[0].header

        ordernum = 0

        dateobs = (hdu['DATE-OBS'])
        objName = (hdu['OBJECT'])
        wavelength = np.float64(sp[0].data[ordernum, :, 0])
        flux = np.float64(sp[0].data[ordernum, :, 1])

        wavearray.append(wavelength)
        fluxarray.append(flux)

    for i in range(stackNum):
        tempWave = wavearray
        tempWave = tempWave[i*ords:(i*ords)+ords]
        tempFlux = fluxarray
        tempFlux = tempFlux[i*ords:(i*ords)+ords]
        plt.scatter(tempWave, tempFlux, label=objName)
    plt.show()

elif ynstack is False:
    # Gets file name from user
    name = raw_input('Please Enter the name of the file: ')

    # opens file as a fits file using the fits function set from astropy
    sp = fits.open(name)

    # Opens the Header file as a object hdu
    hdu = sp[0].header

    # Order number Changer (Change this to look at different orders)
    ordernum = 0
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