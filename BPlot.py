# Echel Spectra viewer
# Paddy Clancy and Thomas Boudreaux
from General import *
initrun = False
#if PreChecks.modimport() is True and initrun == False:
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from PyQt4 import QtGui
from SecondGui import Ui_Header
from GuiFunction import *
from astropy.io import fits
"""
    print 'All Modules OK'
    initrun = True
else:
    print 'Not All Modules are installed, Please Install All Required Modules try again (See README.txt)'
    exit()
"""
PreChecks.oscheck()

inputArray = []
usearray = [False, False]
fit = [False]
showfit = [False]


class Plotter(object):

    @staticmethod
    def stackplot(stackfile, allimages, num, start, degree, shouldfit):
        fig = plt.figure(figsize=(10, 7))
        pathlist = open(stackfile, 'rb')
        patharray = []
        for line in pathlist:
            patharray.append(line)
        if allimages is True:
            stacknum = len(patharray)
        else:
            if num > len(patharray):
                num = len(patharray)
            stacknum = num

        for i in range(stacknum):
            name = patharray[i]
            name = name[:-1]
            PlotFunctionality.plot(name, start, showfit[0], shouldfit, degree, fig)
        plt.tight_layout()
        plt.ion()
        plt.show()

        # gets keyboard input and calls plot functions
        def plotcontrol(event):
            keydown = event.key
            if keydown == 'a' or keydown == 'A':
                plt.close()
                Plotter.stackplot(stackfile, allimages, num, start-1, degree, shouldfit)
            elif keydown == 'd' or keydown == 'D':
                plt.close()
                Plotter.stackplot(stackfile, allimages, num, start+1, degree, shouldfit)
            elif keydown == 'q' or keydown == 'Q':
                plt.close()
                if num != 1:
                    Plotter.stackplot(stackfile, allimages, num - 1, start, degree, shouldfit)
                elif num == 1:
                    Plotter.stackplot(stackfile, allimages, num, start, degree, shouldfit)
            elif keydown == 'e' or keydown == 'E':
                plt.close()
                Plotter.stackplot(stackfile, allimages, num + 1, start, degree, shouldfit)
        fig.canvas.mpl_connect('key_press_event', plotcontrol)

    @staticmethod
    def nstackplot(name, start, degree, shouldfit):
        fig = plt.figure(figsize=(10, 7))
        PlotFunctionality.plot(name, start, showfit, shouldfit, degree, fig)
        plt.tight_layout()
        plt.ion()
        plt.show()

        def plotcontrol(event):
            keydown = event.key
            if keydown == 'a' or keydown == 'A':
                plt.close()
                Plotter.nstackplot(name, start-1, degree, shouldfit)
            elif keydown == 'd' or keydown == 'D':
                plt.close()
                Plotter.nstackplot(name, start+1, degree, shouldfit)
        fig.canvas.mpl_connect('key_press_event', plotcontrol)

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        print 'here'
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Header()
        self.ui.setupUi(self)
        self.ui.function1.setStyleSheet("background-color: red; color: black")
        self.ui.generatePathFiles.clicked.connect(self.generatepath)
        self.ui.quitBut.clicked.connect(self.end)
        self.ui.stackIm.stateChanged.connect(self.stackinput)
        self.ui.allStack.stateChanged.connect(self.allinput)
        self.ui.plotBut.clicked.connect(self.plot)
        self.ui.Secret.clicked.connect(self.secret)
        self.ui.FunctionFit.stateChanged.connect(self.fitter)
        self.ui.function1.clicked.connect(self.showfit)

    def fitter(self):
        fit[0] = not fit[0]
        if fit[0] is False:
            self.ui.function1.setStyleSheet('background-color: red; color: black')
            showfit[0] = False

    def generatepath(self):
        count = 0
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
            self.ui.listWidget.addItem('Star name: ' + starname)
            self.ui.listWidget.addItem('File name: PathTo' + starname)
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
                            self.ui.listWidget.addItem(name)
                            count += 1
                            progress = (count/len(namearray))*100
                            self.ui.PathFileProgress.setValue(progress)
        self.ui.generatePathFiles.setStyleSheet("background-color: green; color: white")

    def plot(self):
        plt.close(1)
        if usearray[0] is True:
            pathfilename = self.ui.pathListInput.toPlainText()
            numToStack = self.ui.numStack.value()
            order = self.ui.startOrd.value()
            degree = self.ui.amplitude.toPlainText()
            Plotter.stackplot(pathfilename, usearray[1], numToStack, order, degree, fit[0])
        else:
            filename = self.ui.singleFileInput.toPlainText()
            degree = self.ui.amplitude.toPlainText()
            order = self.ui.startOrd.value()
            Plotter.nstackplot(filename, order, degree, fit[0])

    def showfit(self):
        if fit[0] is True:
            showfit[0] = not showfit[0]
            if showfit[0] is True:
                self.ui.function1.setStyleSheet("background-color: green; color: white")
            else:
                self.ui.function1.setStyleSheet("background-color: red; color: black")
    @staticmethod
    def end():
        exit()

    @staticmethod
    def secret():
        webbrowser.open('http://d.justpo.st/images/2013/04/b83fb1b7222c18934e59c5b1bd2f43bd.jpg')

    @staticmethod
    def stackinput():
        usearray[0] = not usearray[0]

    @staticmethod
    def allinput():
        usearray[1] = not usearray[1]


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())