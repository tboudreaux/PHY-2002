# Echel Spectra viewer
# Paddy Clancy and Thomas Boudreaux
from General import *

import matplotlib.pyplot as plt
import os
from PyQt4 import QtGui, QtCore
from SecondGui import Ui_Header
import webbrowser
from GuiFunction import *
from astropy.io import fits
import sys
from Correlation import Ui_CrossCore
from consolcontrol import *
from JumpToOrder import Ui_JumpToOrder

PreChecks.oscheck()

#These are here to allow for global variables passe betweel all classes, at some point these
#Should be replaced by PyQt Signals so that there aren't so many global definitions
inputArray = []
usearray = [False, False]
fit = [False]
showfit = [False]
corlist = [False]
jankeyname = []
useorder = [1]
commands = []
i = [0, 1]

# The main GUI Class that runs
class MyForm(QtGui.QMainWindow):
    #I nitilazation of the GUI
    def __init__(self, parent=None):
        # Ininitlazation of the Widget
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Header()
        self.ui.setupUi(self)
        self.ui.consol.append('<font color = "green"> Spectral Image Plotter Version 0.3<br>Written by Paddy Clancy and Thomas Boudreaux  - 2016</font><br>')
        self.ui.consol.append('<font color = "blue"> Module and OS Checks OK</font><br>')
        self.ui.function1.setStyleSheet("background-color: red; color: black")
        # These are the GUI functional ties for the main window
        self.ui.generatePathFiles.clicked.connect(self.generatepath)
        # attempting to replace some of these long functions with lambda statments in otder to clean up code
        self.ui.quitBut.clicked.connect(lambda : exit())
        self.ui.stackIm.stateChanged.connect(lambda : not usearray[0])
        self.ui.allStack.stateChanged.connect(lambda : not usearray[1])
        self.ui.plotBut.clicked.connect(self.plot)
        self.ui.Secret.clicked.connect(self.secret)
        self.ui.FunctionFit.stateChanged.connect(self.fitter)
        self.ui.function1.clicked.connect(self.showfit)
        self.ui.function2.clicked.connect(self.correlate)
        self.ui.function3.clicked.connect(self.LS)
        self.ui.function4.clicked.connect(self.NI)
        self.ui.Shift.clicked.connect(self.NI)
        self.ui.info.clicked.connect(self.info)
        self.ui.Reset.clicked.connect(self.NI)
        # These initialize the windows as empty objects in the Main GUI controller
        self.window2 = None
        self.window3 = None

    ###########################
    ##  GUI tie in functions ##
    ###########################

    # Easter Egg
    def secret(self):
        self.ui.consol.append('<font color = "green"> Displaying the Answer to life - Credit: http://d.justpo.st/images/2013/04/b83fb1b7222c18934e59c5b1bd2f43bd.jpg</font><br>')
        webbrowser.open('http://d.justpo.st/images/2013/04/b83fb1b7222c18934e59c5b1bd2f43bd.jpg')

    # This function controls all keyPresses, it runs at all times in the main window and grabs keypress from that
    def keyPressEvent(self, e):

        # Return controller for consol input
        if e.key() == QtCore.Qt.Key_Return:
            command = self.ui.consolinput.text()
            commandcomp = str.split(str(command))
            iscommand = commandcomp[0]
            commandcomp.pop(0)
            BSPS.route(iscommand, commandcomp)
            self.ui.consol.append(command)
            self.ui.consolinput.clear()
            commands.append(command)

        # Next and previous command for consol input
        elif e.key() == QtCore.Qt.Key_Down:
            i[0] -= 1
            self.ui.consolinput.setText(commands[i[0]])
        elif e.key() == QtCore.Qt.Key_Up:
            i[0] += 1
            self.ui.consolinput.setText(commands[i[0]])

    # Prints the info screen from the info.txt file in the directory tree to the consol
    def info(self):
       infofile = open('info.txt', 'rb')
       infotxt = infofile.read()
       self.ui.consol.append(infotxt)

    # Lists the directories in the working directory in the consol
    # This is due to be replaced when the lauguage is implimented with the ls command built into the language
    def LS(self):
        dirs = os.listdir('.')
        for i in range(len(dirs)):
            self.ui.consol.append('<font color = "blue">' + dirs[i] + '</font>')
        self.ui.consol.append('<font color = "black"> ---------------------------- <font><br>')

    # General Not Implimented function
    def NI(self):
        self.ui.consol.append('<font color = "red"> Button currently not implimented</font><br>')

    # controls the state of the fitting, also helps set the color of the "show fit" button
    def fitter(self):
        fit[0] = not fit[0]
        if fit[0] is False:
            self.ui.function1.setStyleSheet('background-color: red; color: black')
            showfit[0] = False

    # This generates the Path Files by searching through the directory tree for stars with different names
    # This is due to be replaced by a command in the language when the language is implimented
    def generatepath(self):
        count = 0
        namearray = []

        # Generates a list with unique names for all objects
        for root, dirs, files in os.walk('.', topdown=True):
            for file in files:
                if 'achi' in file:
                    filename = os.path.join(root, file)
                    sp = fits.open(filename)
                    hdu = sp[0].header
                    objname = (hdu['OBJECT'])
                    if objname not in namearray:
                        namearray.append(objname)

        # Generates the Lists paths to stars, and addes those to the list widget
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

    # This grabs the infomration for the plot function and then passed it to the Plotter class to plot the function
    # This could probably be cleaned up a bit, however thats a relativly low priority given that its not super
    #   as is right now
    def plot(self):
        # Closes whatever figure is open so that the screen is not overrun with windows everytime Plot is pressed
        # the effect of this is that one can modify parmaters in the GUI and then replot by pressing plot
        plt.close(1)

        # Fetch the values and strings stored in relevent text fields
        degree = self.ui.amplitude.toPlainText()
        pathfilename = self.ui.pathListInput.toPlainText()
        numToStack = self.ui.numStack.value()
        filename = self.ui.singleFileInput.toPlainText()
        order = self.ui.startOrd.value()

        # This opens the jump to window, at some point in the near future this will go away and be called form within
        #   the plotter class so that the user can press j without havin gto refocus on the GUI
        #self.jumpTo()

        # Determins whether to use stack plot or nstack plot, would like to figure out a better way to to this than arrays
        #   but that is currently not a super high priority
        if usearray[0] is True:
            Plotter.stackplot(pathfilename, usearray[1], numToStack, order, degree, fit[0])
        else:
            Plotter.nstackplot(filename, order, degree, fit[0])

    # This controls the "show fit" button, its color and the boolean behind it. Again I would like to come up with a better
    #   way to store the booleans behind buttons, but that is for a latter date
    def showfit(self):
        if fit[0] is True:
            showfit[0] = not showfit[0]
            if showfit[0] is True:
                self.ui.function1.setStyleSheet("background-color: green; color: white")
            else:
                self.ui.function1.setStyleSheet("background-color: red; color: black")
        elif fit[0] is False:
                self.ui.consol.append('<font color = "red"> Cannot Show function unless a function is being fit</font><br>')

    # Calls to open the cross correlation class (and from that then the window)
    def correlate(self):
        self.window2 = CCWindow(self)
        self.window2.show()

    # calls the jump to function (currently this does jack shit so this is a major area for improvment)
    def jumpTo(self):
        degree = self.ui.amplitude.toPlainText()
        pathfilename = self.ui.pathListInput.toPlainText()
        numToStack = self.ui.numStack.value()
        filename = self.ui.singleFileInput.toPlainText()
        order = self.ui.startOrd.value()
        self.window3 = OrderJump(self)
        self.window3.show()

    # Once I determin that the lambda fundtions work these will be deleted, they are antiquated now
    # @staticmethod
    # def end():
    #     exit()

    # @staticmethod
    # def stackinput():
    #     usearray[0] = not usearray[0]

    # @staticmethod
    # def allinput():
    #     usearray[1] = not usearray[1]

# This is the order jump GUI, as before it currently is non functional, will fix at sometime
class OrderJump(QtGui.QMainWindow):
    def __init__ (self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_JumpToOrder()
        self.ui.setupUi(self)

        self.ui.cancel.clicked.connect(self.closser)
        self.ui.replot.clicked.connect(self.replot)

    def replot(self):
        order = self.ui.order.value()
        Plotter

    def closser(self):
        self.destroy()

# this is the cross correlation GUI
class CCWindow(QtGui.QMainWindow):
    def __init__ (self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_CrossCore()
        self.ui.setupUi(self)

        self.ui.listpath.setStyleSheet('background-color: grey')
        self.ui.return_2.clicked.connect(self.closeer)
        self.ui.ynlist.stateChanged.connect(self.uselist)
        self.ui.correlate.clicked.connect(self.ccorplot)

    # Closes the Cross correlation GUI
    def closeer(self):
       self.destroy()

    # The Boolean operator for Cross Corelation list (cross corelate multiple orders at one time or not)
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

    # The is the function that controls plotting cross correlation, currently it calls the corplot function in Plotter
    #   It has some functionality now but it is by no means where it needs to be
    def ccorplot(self):
        if corlist[0] is True:
            self.ui.infobox.append('<font color="red">Multiple Correlation Not an opetion currently, please deselect and use single correlation</font><br>')
        else:
            degree = self.ui.fitdegree.value()
            templatename = self.ui.tempfilename.toPlainText()
            objectname = self.ui.targetfilename.toPlainText()
            self.ui.infobox.append('<font color ="green">Cross Correlating Orders, use "a" to advance</font><br>')
            Plotter.corplot(degree, templatename, objectname, 1)

# This is plotter code, at some point it may be nice to move this class (During the great reorginazation of code to come)
class Plotter(MyForm, CCWindow):

    # Corplot function that calls the ccofig function from GUI function to extract the required data
    # incidentaly this will be completely reorganized in the great reorganization of code to come
    @staticmethod
    def corplot(degree, templatename, objectname, order):
        # Creates a matplotlib figure of given size (will at some point be configuarble in the forcoming settings menu)
        fig=plt.figure(figsize=(10, 7))
        # Adds the ccorfig subplot
        ccorfig = fig.add_subplot(1, 1, 1)
        # fetches the data from the ccor function in Advanced Plotting by calling the function, data is returnted as a
        #   2 element dictionary, so then when its plotted below there its is called with the dictionaty nameing
        data = AdvancedPlotting.ccor(objectname, templatename, degree, order)
        ccorfig.plot(data['corwave'], data['correlation'])

        # This allows one to move between orders in C
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
                if int(start)-1 != 0:
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