# Echel Spectra viewer
# Paddy Clancy and Thomas Boudreaux
from General import *

import matplotlib.pyplot as plt
import os
from PyQt4 import QtGui
from SecondGui import Ui_Header
import webbrowser
from GuiFunction import *
from astropy.io import fits
import sys
from Correlation import Ui_CrossCore

PreChecks.oscheck()

inputArray = []
usearray = [False, False]
fit = [False]
showfit = [False]
corlist = [False]
jankeyname = []
useorder = [1]

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Header()
        self.ui.setupUi(self)
        self.ui.consol.append('<font color = "green"> Spectral Image Plotter Version 0.3<br>Written by Paddy Clancy and Thomas Boudreaux  - 2016</font><br>')
        self.ui.consol.append('<font color = "blue"> Module and OS Checks OK</font><br>')
        self.ui.function1.setStyleSheet("background-color: red; color: black")
        self.ui.generatePathFiles.clicked.connect(self.generatepath)
        self.ui.quitBut.clicked.connect(self.end)
        self.ui.stackIm.stateChanged.connect(self.stackinput)
        self.ui.allStack.stateChanged.connect(self.allinput)
        self.ui.plotBut.clicked.connect(self.plot)
        self.ui.Secret.clicked.connect(self.secret)
        self.ui.FunctionFit.stateChanged.connect(self.fitter)
        self.ui.function1.clicked.connect(self.showfit)
        self.ui.function2.clicked.connect(self.correlate)
        self.ui.function3.clicked.connect(self.LS)
        self.ui.function4.clicked.connect(self.NI)
        self.ui.Shift.clicked.connect(self.NI)
        self.ui.info.clicked.connect(self.NI)
        self.ui.Reset.clicked.connect(self.NI)
        self.window2 = None

    def LS(self):
        dirs = os.listdir('.')
        for i in range(len(dirs)):
            self.ui.consol.append('<font color = "blue">' + dirs[i] + '</font>')
        self.ui.consol.append('<font color = "black"> ---------------------------- <font><br>')

    def NI(self):
        self.ui.consol.append('<font color = "red"> Button currently not implimented</font><br>')


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

        if len(namearray) > 0:
            self.ui.consol.append('<font color = "green"> Path Files Successfully generated</font><br>')
            self.ui.generatePathFiles.setStyleSheet("background-color: green; color: white")
        else:
            self.ui.consol.append('<font color = "red"> No Path Files Generated, is your data folder in the program direcotry?</font><br>')
            self.ui.generatePathFiles.setStyleSheet("background-color: red; color: white")

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
        elif fit[0] is False:
                self.ui.consol.append('<font color = "red"> Cannot Show function unless a function is being fit</font><br>')

    def correlate(self):
        self.window2 = CCWindow(self)
        self.window2.show()

    @staticmethod
    def end():
        print 'Closing Spectral Plotter in 5 seconds'
        exit()

    def secret(self):
        self.ui.consol.append('<font color = "green"> Displaying the Answer to life - Credit: http://d.justpo.st/images/2013/04/b83fb1b7222c18934e59c5b1bd2f43bd.jpg</font><br>')
        webbrowser.open('http://d.justpo.st/images/2013/04/b83fb1b7222c18934e59c5b1bd2f43bd.jpg')

    @staticmethod
    def stackinput():
        usearray[0] = not usearray[0]

    @staticmethod
    def allinput():
        usearray[1] = not usearray[1]

class CCWindow(QtGui.QMainWindow):
    def __init__ (self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_CrossCore()
        self.ui.setupUi(self)

        self.ui.listpath.setStyleSheet('background-color: grey')
        self.ui.return_2.clicked.connect(self.closeer)
        self.ui.ynlist.stateChanged.connect(self.uselist)
        self.ui.correlate.clicked.connect(self.ccorplot)

    def closeer(self):
       self.destroy()

    def uselist(self):
        corlist[0] = not corlist[0]

        if corlist[0] is False:
            self.ui.tempfilename.setStyleSheet('background-color: white')
            self.ui.targetfilename.setStyleSheet('background-color: white')
            self.ui.listpath.setStyleSheet('background-color: grey')
        else:
            self.ui.tempfilename.setStyleSheet('background-color: grey')
            self.ui.targetfilename.setStyleSheet('background-color: grey')
            self.ui.listpath.setStyleSheet('background-color: white')


    def ccorplot(self):
        if corlist[0] is True:
            self.ui.infobox.append('<font color="red">Multiple Correlation Not an opetion currently, please deselect and use single correlation</font><br>')
        else:
            degree = self.ui.fitdegree.value()
            templatename = self.ui.tempfilename.toPlainText()
            objectname = self.ui.targetfilename.toPlainText()
            self.ui.infobox.append('<font color ="green">Cross Correlating Orders, use "a" to advance</font><br>')
            Plotter.corplot(degree, templatename, objectname, 1)


class Plotter(MyForm, CCWindow):

    @staticmethod
    def corplot(degree, templatename, objectname, order):
        fig=plt.figure(figsize=(10, 7))
        ccorfig = fig.add_subplot(1, 1, 1)
        data = AdvancedPlotting.ccor(objectname, templatename, degree, order)
        ccorfig.plot(data['corwave'], data['correlation'])
        def plotcontrol(event):
            keydown = event.key
            if keydown == 'a' or keydown == 'A' and order < 62:
                plt.close()
                Plotter.corplot(degree, templatename, objectname, order + 1)
        fig.canvas.mpl_connect('key_press_event', plotcontrol)
        plt.show()

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

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())