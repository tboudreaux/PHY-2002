# Echel Spectra viewer
# Paddy Clancy and Thomas Boudreaux
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
# TODO  figure out how to get directorys working

############################
#        Pre-Code          #
############################
# General Use Verriable Section

# General Yes no menu funtion


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
    for i in range(2):
        name = pathArray[i]
        name = name[:-1]
        sp = fits.open(name)
        hdu = sp[0].header

        ordernum = 0

        dateobs = (hdu['DATE-OBS'])

        wavelength = np.float64(sp[0].data[ordernum, :, 0])
        flux = np.float64(sp[0].data[ordernum, :, 1])

        wavearray.append(wavelength)
        fluxarray.append(flux)

    for i in range(2):
        tempWave = wavearray
        tempWave = tempWave[i*ords:(i*ords)+ords]
        tempFlux = fluxarray
        tempFlux = tempFlux[i*ords:(i*ords)+ords]
        plt.scatter(tempWave, tempFlux)
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