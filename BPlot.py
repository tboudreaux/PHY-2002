# Echel Spectra viewer & analizer
# Paddy Clancy and Thomas Boudreaux
from General import *
prerun = open('prerun.log','w')
# GUI file import statements
print >>prerun, 'Cheking for GUI files'
try:
    from Correlation2 import Ui_CrossCore
    from JumpToOrder import Ui_JumpToOrder
    from Editor import Ui_MainWindow
    from GaussianFitter import Ui_GaussianFitter
    from SecondGui import Ui_Header
    from MultiplotViewerTesttwo import Ui_MultiplotViewer
    print >>prerun, 'GUI files OK'
except ImportError:
    print >>prerun, 'Some or all GUI files missing, please check to make sure that you donwloaded the entire package and re-run'
    exit()

# importer for pip module
print >>prerun, 'Checking pip'
try:
    import pip
    print >>prerun, 'pip OK'
except ImportError:
    print >>prerun, 'pip not found, will try to continue running program, if all other dependanceied are installed program should run OK'

packages = ['import random', 'import matplotlib.pyplot as plt', 'import os', 'from PyQt4 import QtGui, QtCore',
            'import webbrowser', 'from astropy.io import fits', 'import sys', 'import time',
            'from matplotlib.backend_bases import key_press_handler', 'from pylab import *',
            'from matplotlib.widgets import CheckButtons', 'from PyQt4.uic import loadUiType', 'import jplephem',
            'import de423', 'import jdcal', 'from matplotlib.figure import Figure',
            'from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as NavigationToolbar)',
            'import astropy.time as astrotime', 'import astropy.coordinates as coords', 'import astropy.units as unit',
            'import astropy.constants as const', 'from astropy.modeling import models,fitting',
            'from scipy import asarray as ar,exp', 'from scipy.optimize import curve_fit', 'import math',
            'import numpy as np']

code = []
for importer in range(len(packages)):
    cont = False
    commandtemp = packages[importer].split(' ')
    package = commandtemp[1]
    try:
        exec(packages[importer])
        print >>prerun, package, 'OK'
        code.append(1)
        code.append(1)
        code.append(1)
    except ImportError:
        print >>prerun, packages[importer], 'Not found in your python install, it is recomended that you use annaconda'
        print packages[importer], 'Not found in your python install, it is recomended that you use annaconda'
        while cont is False:
            installpac = raw_input('Would you like to install ' + packages[importer] + ' [Y/n]: ')
            if installpac == 'Y':
                pip.main(['install', package])
                try:
                    exec(packages[importer])
                    print >>prerun, package, 'OK'
                    code.append(0)
                    code.append(1)
                    code.append(1)
                except ImportError:
                    print >>prerun, 'An Unkown Error has occured while importing or installing', package, 'Please consider using annaconda'
                    code.append(0)
                    code.append(1)
                    code.append(0)
            cont = True
            if installpac == 'n':
                print >>prerun, package, 'will not be installed, the program cannot run without this packages and will now shutdown, please consider using anaconda'
                print package, 'will not be installed, the program cannot run without this packages and will now shutdown, please consider using anaconda'
                cont = True
                code.append(0)
                code.append(0)
                code.append(0)
                exit()
            else:
                print 'Please Enter either Y or n'
print len(code)
print >>prerun, 'Trying other program dependancy files'
try:
    from GuiFunction import *
    from consolcontrol import *
except ImportError:
    print >>prerun, 'Some or all internal dependancies were not met, please make sure that you downloaded the entire package and re-run'
    exit()
# Checks os for compatability
mac = PreChecks.oscheck()
for precode in range(len(code)):
    code[precode] = str(code[precode])
code = ''.join(code)
savecode = code
code = int(code, 2)

print >>prerun, 'Pre-run Checks finished with code:', code, '(', savecode, ')'
prerun.close()
print 'Pre-run Checks finished with code:', code
# These are here to allow for global variables passe betweel all classes, at some point these
# Should be replaced by local namespace variables, however I have yet to get around to that
inputArray = []
usearray = [False, False]
fit = [False]
showfit = [False]
corlist = [False]
jankeyname = []
useorder = [1]
commands = []
commandnum = [0, 1]
UserFunctions = ['open', 'open', 'open', 'open']
readfile = open('UserFunc.conf', 'rb')
plotparm = [None] * 11
funcconf = [['1','Null', 'Function1'], ['2', 'Null', 'Function2'], ['3', 'Null', 'Function3'], ['4', 'Null', 'Function4']]
jumpcore = [False]
compare = [False]
simplefilearray = []
foundit = False
whilecounter = 0
masterfilearray = []
flist = os.listdir('.')
halphause = [True]; hbetause = [True]; heliumause = [True]
FullCC = []
FullO = []
FullGaus = []
allplots = [False]
checkPlots = [True]*62
velocity = []
for name in flist:
    if 'PathTo' in name:
        foundit = True
        simplefilearray.append(name)

if len(simplefilearray) is not 0:
    for name in simplefilearray:
        tempopen = open(name, 'rb')
        tempopen = tempopen.readlines()
        tempopen = [x[:-1] for x in tempopen]
        tempopen.insert(0, name)
        masterfilearray.append(tempopen)

# The main GUI Class that controlles the rest og the program
class MyForm(QtGui.QWidget):
    #I nitilazation of the GUI
    def __init__(self, parent=None):
        # Ininitlazation of the Widget
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Header()
        self.ui.setupUi(self)
        self.com = Plotter()
        pathbool = False
        # These next few lines control the Custom User Function Persistence Features
        lastrun = readfile.readlines()
        for o in range(4):
            lastrun[o] = lastrun[o][:-1]

        saverun = lastrun
        for j in range(len(lastrun)):
            lastrun[j] = lastrun[j].split()

        # These lines load in the data that was read in from the file into the User functions, could prorobably be
        # simplified with a switch statment, however thats not really nessisary right now
        if len(saverun) >= 1:
            UserFunctions[0] = lastrun[0][1]

            self.ui.UseFunction1.clicked.connect(self.functiontie1)
            self.ui.UseFunction1.setText(lastrun[0][2])
            funcconf[0] = lastrun[0]
        if len(saverun) >= 2:
            UserFunctions[1] = lastrun[1][1]
            self.ui.UserFunction2.clicked.connect(self.functiontie2)
            self.ui.UserFunction2.setText(lastrun[1][2])
            funcconf[1] = lastrun[1]
        if len(saverun) >= 3:
            UserFunctions[2] = lastrun[2][1]
            self.ui.UserFuntion3.clicked.connect(self.functiontie3)
            self.ui.UserFuntion3.setText(lastrun[2][2])
            funcconf[2] = lastrun[2]
        if len(saverun) == 4:
            UserFunctions[3] = lastrun[3][1]
            self.ui.userFuntion4.clicked.connect(self.functiontie4)
            self.ui.userFuntion4.setText(lastrun[3][2])
            funcconf[3] = lastrun[3]

        if len(masterfilearray) is not 0:
            pathbool = True
            for k in range(len(masterfilearray)):
                starname = masterfilearray[k][0][6:]
                self.ui.listWidget.addItem('Star name: ' + starname)
                self.ui.listWidget.addItem('File name: PathTo' + starname)
                for p in range(len(masterfilearray[k])):
                    if p is not 0:
                        self.ui.listWidget.addItem(masterfilearray[k][p])
        # These control most of the button assignments in the main GUI
        self.ui.consol.append('<font color = "green"> SAUL Version 0.5<br>Written by Paddy Clancy and Thomas Boudreaux  - 2016</font><br>')
        self.ui.consol.append('<font color = "blue"> Module and OS Checks OK</font><br>')
        self.ui.consol.append('<font color = "blue"> type "lcom" for a list of avalibel commands</font><br>')
        if pathbool is True:
            self.ui.consol.append('<font color = "green"> Path Files Successfully located in working directory</font><br>')
            self.ui.generatePathFiles.setStyleSheet("background-color: green; color: white")
        self.ui.function1.setStyleSheet("background-color: red; color: black")
        # These are the GUI functional ties for the main window
        self.ui.generatePathFiles.clicked.connect(self.generatepath)
        # attempting to replace some of these long functions with lambda statments in otder to clean up code
        self.ui.quitBut.clicked.connect(lambda : exit())
        self.ui.stackIm.stateChanged.connect(lambda : usearray.__setitem__(0, not usearray[0]))
        self.ui.allStack.stateChanged.connect(lambda : usearray.__setitem__(1, not usearray[1]))
        self.ui.plotBut.clicked.connect(self.plot)
        self.ui.Secret.clicked.connect(self.secret)
        self.ui.FunctionFit.stateChanged.connect(self.fitter)
        self.ui.function1.clicked.connect(self.showfit)
        self.ui.function2.clicked.connect(self.correlate)
        self.ui.LS.clicked.connect(self.LS)
        self.ui.function4.clicked.connect(self.gaussian)
        self.ui.info.clicked.connect(self.info)
        self.ui.Reset.clicked.connect(BSPSEss.reload)


        # These initialize the other windows as empty objects in the Main GUI controller
        self.window2 = None
        self.window3 = None
        self.window3 = None
        self.window4 = None

    ###########################
    ##  GUI tie in functions ##
    ###########################

    def gaussian(self):
        self.window4 = GaussianWindow(self)
        self.window4.show()

    # Easter Egg
    def secret(self):
        r = random.randrange(1, 5)
        if r == 1:
            self.ui.consol.append('<font color = "green"> Displaying a possible Answer to life - Credit: http://d.justpo.st/images/2013/04/b83fb1b7222c18934e59c5b1bd2f43bd.jpg</font><br>')
            webbrowser.open('http://d.justpo.st/images/2013/04/b83fb1b7222c18934e59c5b1bd2f43bd.jpg')
        elif r == 2:
            self.ui.consol.append('<font color = "green"> Displaying a possible Answer to life - Credit: http://sf.co.ua/id90453</font><br>')
            webbrowser.open('http://sf.co.ua/id90453')
        elif r == 3:
            self.ui.consol.append('<font color = "green"> Displaying a possible Answer to life - Credit: https://s-media-cache-ak0.pinimg.com/236x/2f/88/26/2f8826f5a6a97006ecd350211eb584ee.jpg</font><br>')
            webbrowser.open('https://s-media-cache-ak0.pinimg.com/236x/2f/88/26/2f8826f5a6a97006ecd350211eb584ee.jpg')
        elif r == 4:
            self.ui.consol.append('<font color = "green"> Displaying a possible Answer to life - Credit: http://nicolascage.us/wp-content/uploads/2013/09/Universe-Cupcake.jpg</font><br>')
            webbrowser.open('http://nicolascage.us/wp-content/uploads/2013/09/Universe-Cupcake.jpg')

    # This function controls all keyPresses, it runs at all times in the main window and grabs keypress from that
    def keyPressEvent(self, e):

        # Return controller for consol input
        if e.key() == QtCore.Qt.Key_Return:
            command = self.ui.consolinput.text()
            commandcomp = str.split(str(command))
            iscommand = commandcomp[0]
            commandcomp.pop(0)

            # Passes the parsed command and parameters into the consol control class routing function
            # the routing function returns a string
            string = BSPS.route(iscommand, commandcomp)

            # appends the entered command to the consol
            self.ui.consol.append('<font color = green>' + command + '</font>')

            # all these //word are the syntax for commands that have special functions
            # clears the terminal window
            if string == '//clear':
                self.ui.consol.clear()
                string = None

            # Brings up an ASCII Text editor
            elif string == '//edit':
                self.window3 = Editor(self)
                self.window3.show()

                # Opens file if file exists / creats file if file does not exist
                # This could be done better with logic instead of rellying on errors, however so far it works
                # and as such that is low priority
                try:
                    text = open(commandcomp[0], 'rb')
                    text = text.read()
                except IOError:
                    text = open(commandcomp[0], 'w')
                self.window3.ui.textEdit.append(text)
                self.window3.ui.FileName.setText(commandcomp[0])
                string = None

            #lists the number of open user functions
            elif string == '//lfunc':
                count = 0
                for i in range(4):
                    if UserFunctions[i] == 'open':
                        count += 1
                self.ui.consol.append('There are ' + str(count) + ' Open functions')
                string = None

            # lists more detail on open user functions
            elif string == '//lfuncall':
                count = 0
                for q in range(4):
                    self.ui.consol.append(UserFunctions[q] + '[' + str(q+1)  + ']')
                    if UserFunctions[q] == 'open':
                        count += 1
                self.ui.consol.append('There are ' + str(count) + ' Open functions')
                string = None

            #controls the tieing of scripts to user buttons, most of this is repetative logic
            elif string == '//tie':
                script = commandcomp[0]
                function = commandcomp[1]
                if function == '1' or function == 'one' or function == 'One':
                    if len(commandcomp) == 3:
                        self.ui.UseFunction1.setText(commandcomp[2])
                        funcconf[0][0] = '1 '; funcconf[0][1] = script; funcconf[0][2] = commandcomp[2]
                    else:
                        self.ui.UseFunction1.setText(script)
                        funcconf[0][0] = '1 '; funcconf[0][1] = script; funcconf[0][2] = script
                    UserFunctions[0] = script
                    self.ui.UseFunction1.clicked.connect(self.functiontie1)
                if function == '2' or function == 'two' or function == 'Two':
                    if len(commandcomp) == 3:
                        self.ui.UserFunction2.setText(commandcomp[2])
                        funcconf[1][0] = '2 '; funcconf[1][1] = script; funcconf[1][2] = commandcomp[2]
                    else:
                        self.ui.UserFunction2.setText(script)
                        funcconf[1][0] = '2 '; funcconf[1][1] = script; funcconf[1][2] = script
                    UserFunctions[1] = script
                    self.ui.UserFunction2.clicked.connect(self.functiontie2)
                if function == '3' or function == 'three' or function == 'Three':
                    if len(commandcomp) == 3:
                        self.ui.UserFuntion3.setText(commandcomp[2])
                        funcconf[2][0] = '3 '; funcconf[2][1] = script; funcconf[2][2] = commandcomp[2]
                    else:
                        self.ui.UserFuntion3.setText(script)
                        funcconf[2][0] = '3 '; funcconf[2][1] = script; funcconf[2][2] = script
                    UserFunctions[2] = script
                    self.ui.UserFuntion3.clicked.connect(self.functiontie3)
                if function == '4' or function == 'four' or function == 'Four':
                    if len(commandcomp) == 3:
                        self.ui.userFuntion4.setText(commandcomp[2])
                        funcconf[3][0] = '4 '; funcconf[3][1] = script; funcconf[3][2] = commandcomp[2]
                    else:
                        self.ui.userFuntion4.setText(script)
                        funcconf[3][0] = '4 '; funcconf[3][1] = script; funcconf[3][2] = script

                    UserFunctions[3] = script
                    self.ui.userFuntion4.clicked.connect(self.functiontie4)
                datafile = open('UserFunc.conf', 'w')
                for n in range(len(funcconf)):
                    printwords = funcconf[n][0] + ' ' + funcconf[n][1] + ' ' + funcconf[n][2]
                    #for k in range(3):
                    print >>datafile, printwords
                string = None

            # Checks to make sure that the sring exists
            if string:
                # appends the sting returnes from the routing function to the consol, if it has not been deinitialized
                # in the command logic above
                self.ui.consol.append(string)
            self.ui.consolinput.clear()
            commands.append(command)

        # Next and previous command for consol input
        elif e.key() == QtCore.Qt.Key_Down:
            commandnum[0] -= 1
            self.ui.consolinput.setText(commands[commandnum[0]])
        elif e.key() == QtCore.Qt.Key_Up:
            commandnum[0] += 1
            self.ui.consolinput.setText(commands[commandnum[0]])
        elif e.key() == QtCore.Qt.Key_J:
            self.jumpTo()

    # Prints the info screen from the info.txt file in the directory tree to the consol
    def info(self):
       infofile = open('info.txt', 'rb')
       infotxt = infofile.read()
       self.ui.consol.append(infotxt)

    # Lists the directories in the working directory in the consol
    # This is due to be replaced when the language is implimented with the ls command built into the language

    def functiontie1(self):
        text = BSPSEss.pyrun(UserFunctions[0])
        self.ui.consol.append(text)

    def functiontie2(self):
        text = BSPSEss.pyrun(UserFunctions[1])
        self.ui.consol.append(text)

    def functiontie3(self):
        text = BSPSEss.pyrun(UserFunctions[2])
        self.ui.consol.append(text)

    def functiontie4(self):
        text = BSPSEss.pyrun(UserFunctions[3])
        self.ui.consol.append(text)

    def LS(self):
        dirs = os.listdir('.')
        for i in range(len(dirs)):
            self.ui.consol.append('<font color = "blue">' + dirs[i] + '</font>')
        self.ui.consol.append('<font color = "black"> ---------------------------- <font><br>')

    # General Not Implimented function

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
        self.ui.listWidget.clear()
        masterfilearray = None
        masterfilearray = []
        smallarray = []
        largearray = []
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
            smallarray.append(nameforfile)
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
                            smallarray.append(name)
                            count += 1
                            progress = (count/len(namearray))*100
                            self.ui.PathFileProgress.setValue(progress)
                            masterfilearray.append(smallarray)


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
        degree = self.ui.amplitude.value()
        plotparm[0] = degree
        try:
            if usearray[0] is True:
                pathfilename = self.ui.pathListInput.text()
                numToStack = self.ui.numStack.value()
                plotparm[1] = pathfilename; plotparm[2] = numToStack
            else:
               filename = self.ui.singleFileInput.text()
               plotparm[3] = filename
        except IOError:
            self.ui.consol.append('<font color = "red"> No Such File found, please check spelling and try again</font>')

        order = self.ui.startOrd.value()
        # Determins whether to use stack plot or nstack plot, would like to figure out a better way to to this than arrays
        #   but that is currently not a super high priority
        if usearray[0] is True:
            Plotter.stackplot(pathfilename, usearray[1], numToStack, order, degree, fit[0])
        else:
            Plotter.nstackplot(filename, order, degree, fit[0])
        jumpcore[0] = False
        self.jumpTo()

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
        # degree = self.ui.amplitude.toPlainText()
        # pathfilename = self.ui.pathListInput.toPlainText()
        # numToStack = self.ui.numStack.value()
        # filename = self.ui.singleFileInput.toPlainText()
        # order = self.ui.startOrd.value()
        self.window3 = OrderJump(self)
        self.window3.show()

class GaussianWindow(QtGui.QMainWindow):
    def __init__ (self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_GaussianFitter()
        self.ui.setupUi(self)
        self.ui.quit.clicked.connect(self.closer) # for the quit button
        self.ui.HydrogenA.stateChanged.connect(lambda : halphause.__setitem__(0, not halphause[0]))
        self.ui.HydrogenB.stateChanged.connect(lambda : hbetause.__setitem__(0, not hbetause[0]))
        self.ui.HeliumA.stateChanged.connect(lambda : heliumause.__setitem__(0, not heliumause[0]))
        self.ui.pushButton.clicked.connect(self.plot)
        if len(masterfilearray) is not 0:
            for k in range(len(masterfilearray)):
                starname = masterfilearray[k][0][6:]
                self.ui.listWidget.addItem('Star name: ' + starname)
                for p in range(len(masterfilearray[k])):
                    if p is not 0:
                        self.ui.listWidget.addItem(masterfilearray[k][p])
            self.ui.infobox.append('<font color = "green">Files Succesfully loaded</font>')
        else:
            self.ui.infobox.append('<font color = "red">No Files Found or loaded, did you generate path files?</font>')
    def closer(self):
        self.close()
    def plot(self):
        filename = self.ui.lineEdit.text()
        Gauss = AdvancedPlotting.gaussianfit(filename,halphause[0],hbetause[0],heliumause[0])



# This is the order jump GUI, as before it currently is non functional, will fix at sometime
class OrderJump(QtGui.QDialog):
    def __init__ (self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_JumpToOrder()
        self.ui.setupUi(self)
        self.ui.cancel.clicked.connect(self.closser)
        self.ui.replot.clicked.connect(self.replot)

    def replot(self):
        order = self.ui.order.value()
        if jumpcore[0] is False:
            if usearray[0] is True:
                plt.close()
                Plotter.stackplot(plotparm[1], usearray[1], plotparm[2], order, plotparm[0], fit[0])
            else:
                plt.close()
                Plotter.nstackplot(plotparm[3], order, plotparm[0], fit[0])
        else:
            pass
            # plt.close()
            # Plotter.corplot(plotparm[4], plotparm[5], plotparm[6], order, plotparm[7], plotparm[8], plotparm[9], compare[0], plotparm[10], True)


    def closser(self):
        self.close()

class Editor(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Close.clicked.connect(lambda : self.close())
        self.ui.Save.clicked.connect(self.save)

    def save(self):
        with open(self.ui.FileName.text(), 'wt') as writefile:
            writefile.write(self.ui.textEdit.toPlainText())

class MultiView(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MultiplotViewer()
        self.ui.setupUi(self)
        self.number = 0
        fig = []
        self.canvas = []
        windowsize = self.size()
        windowsize = str(windowsize)
        windowwidth = int(windowsize[19:-6])
        windowheight = int(windowsize[24:-1])
        widgets = dict()
        windowheight -= (0.2)*windowheight
        print windowheight
        boxheight = windowheight/3
        print boxheight
        ax = []
        for i in range(62):
            widgets[i+1] = 'self.ui.widget_' + str(i+1)
        for q in range(62):
            fig.append(Figure(figsize=(2.81,boxheight/100), dpi=85, facecolor='w'))
        for q in range(62):
            self.canvas.append(FigureCanvas(fig[q]))
        for q in range(62):
            self.canvas[q].setParent(eval(widgets[q+1]))
        for q in range(62):
            ax.append(fig[q].add_subplot(111, xlabel='Offset(A)', ylabel='CC', title='order: '+ str(q+1)))
        for q in range(62):
            ax[q].plot(FullO[q], FullCC[q])
            ax[q].plot(FullO[q], FullGaus[q])
        del FullCC[:]
        del FullO[:]
        del FullGaus[:]

        self.ui.Advance.clicked.connect(self.go)
        self.window2 = None

    @staticmethod
    def flop(num):
        checkPlots[num] = not checkPlots[num]

    def go(self):
        checks = dict()
        checkArray = []
        useCheckArray = dict()
        usevelocity = []
        for q in range(62):
            checks[q] = 'self.ui.checkBox_' + str(q+1)
        for q in range(62):
            checkArray.append(eval(checks[q]).isChecked())
        for i in range(len(checkArray)):
            if checkArray[i] is True:
                useCheckArray[i] = checkArray[i]
            else:
                pass
        for i in range(len(velocity)):
            if checkArray[i] is True:
                usevelocity.append(velocity[i])
            else:
                pass
        meanVel = sum(usevelocity)/len(usevelocity)
        Velstd = np.std(usevelocity)
        usetext = 'Mean of Selected velocity: ' + str(meanVel) + '\nStandard Deviation in Selected Velocities: ' + str(Velstd)
        self.window2 = Editor()
        self.window2.ui.textEdit.append(usetext)
        self.window2.ui.FileName.setText('CCorOutput.txt')
        self.window2.show()

# this is the cross correlation GUI


class CCWindow(QtGui.QMainWindow):
    def __init__ (self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_CrossCore()
        self.ui.setupUi(self)
        if len(masterfilearray) is not 0:
            for k in range(len(masterfilearray)):
                starname = masterfilearray[k][0][6:]
                self.ui.FileBox.addItem('Star name: ' + starname)
                for p in range(len(masterfilearray[k])):
                    if p is not 0:
                        self.ui.FileBox.addItem(masterfilearray[k][p])
            self.ui.infobox.append('<font color = "green">Files Succesfully loaded</font>')
        else:
            self.ui.infobox.append('<font color = "red">No Files Found or loaded, did you generate path files?</font>')
        self.smallerwaves = []
        self.largerwaves = []
        self.ranges = []

        try:            # looks at a text file to get numbers and stuff (food is not exempt from the stuff category)
            self.profiles = {'CHIRON':'chiron.pconf'}
            profile1 =  open(self.profiles['CHIRON'], 'rb')  # opens the file for python
            self.ui.SystemProfiles.addItem('CHIRON')
            profile1 = profile1.readlines()  # converts each line into a single element in an array
            self.length = len(profile1)


            for i in range(self.length):
                profile1[i] = profile1[i].split('-')  # reads through a string and splits at the '-' and creates a multi dimensional array
                profile1[i][1] = profile1[i][1][:-1]  # gets rid of the newline character
                self.smallerwaves.append(profile1[i][0])
                self.largerwaves.append(profile1[i][1])
                self.smallerwaves[i] = float(self.smallerwaves[i])
                self.largerwaves[i] = float(self.largerwaves[i])
        except IOError:
            self.ui.infobox.append('<font color = "red"> ERROR - DEFAULT PROFILE {CHIRON} NOT FOUND</font>')

        dirs = os.listdir('.')
        for i in range(len(dirs)):
            if '.pconf' in dirs[i] and 'chiron' not in dirs[i] and dirs[i][:-6]:
                self.ui.UserProfile.addItem(dirs[i][:-6])
        self.useuser = False
        self.ui.listpath.setStyleSheet('background-color: grey')
        self.ui.return_2.clicked.connect(self.closeer)
        self.ui.ynlist.stateChanged.connect(self.uselist)
        self.ui.correlate.clicked.connect(self.ccorplot)
        self.ui.AddProfile.clicked.connect(self.addProfile)
        self.ui.addout.clicked.connect(self.addout)
        self.ui.SaveProfile.clicked.connect(self.setprofile)
        self.ui.useUser.stateChanged.connect(self.user)
        self.ui.multiplotshow.stateChanged.connect(lambda : allplots.__setitem__(0, not allplots[0]))
        self.window2 = None


    def user(self):
        self.useuser = not self.useuser

    def setprofile(self):
        if self.useuser is True:
            profile = str(self.ui.UserProfile.currentText())
        else:
            profile = str(self.ui.SystemProfiles.currentText())
        try:
            profile += '.pconf'
            profileopen =  open(profile, 'rb')
            profileopen = profileopen.readlines()
            length = len(profileopen)

            for i in range(length):
                profileopen[i] = profileopen[i].split('-')
                profileopen[i][1] = profileopen[i][1][:-1]
                self.smallerwaves.append(profileopen[i][0])
                self.largerwaves.append(profileopen[i][1])
                self.smallerwaves[i] = float(self.smallerwaves[i])
                self.largerwaves[i] = float(self.largerwaves[i])
        except IOError:
            self.ui.infobox.append('<font color = "red"> ERROR - .pconf profile file not found</font>')

    def addout(self):
        lower = self.ui.Lowertext.text()
        upper = self.ui.uppertext.text()
        rangenum = str(lower) + '-' + str(upper)
        self.ui.listoforders.addItem(rangenum)
        self.ui.Lowertext.clear()
        self.ui.uppertext.clear()
        self.ranges.append(rangenum)

    def addProfile(self):
        name = self.ui.ProfileName.text()
        if len(name) > 0:
            name += '.pconf'
            write = open(name, 'w')
            for i in range(len(self.ranges)):
                print >>write, self.ranges[i]
            self.ui.listoforders.clear()
            self.ui.ProfileName.clear()
            self.ranges = None
            self.ranges = []
            self.ui.ProfileName.setStyleSheet('border: 1px solid grey')
        else:
            self.ui.ProfileName.setStyleSheet('border: 1px solid red')

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_J:
            self.jumpTo()
        elif e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def jumpTo(self):
        self.window2 = OrderJump()
        self.window2.show()

    # Closes the Cross correlation GUI
    def closeer(self):
       self.close()

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
            templatename = self.ui.tempfilename.text()
            objectname = self.ui.targetfilename.text()
            value = self.ui.ShiftSize.value()
            run = False
            try:
                if allplots[0] is False:
                    Plotter.corplot(degree, templatename, objectname, 1, self.length, self.smallerwaves, self.largerwaves, compare[0], value, True)
                    self.ui.infobox.append('<font color ="green">Cross Correlating Orders, use "a" to advance</font><br>')
                elif allplots[0] is True:
                    self.ui.infobox.append('<font color = "green">Calculating Cross Correlation Coefficients for all orders</font>')
                    self.ui.infobox.append('<font color = "green">This can take some time, please be paitient</font>')
                    Plotter.corplot(degree, templatename, objectname, 1, self.length, self.smallerwaves, self.largerwaves, compare[0], value, False)
                run = True
            except ValueError:
                self.ui.infobox.append('<font color ="red">Please Make sure that file names are entered in the boxs</font>')
            except IOError:
                self.ui.infobox.append('<font color ="red">Please Make sure that file names are spelled correctly</font>')
            print 'In Here'
            HJD = AdvancedPlotting.coordconvert(objectname)
            print HJD
            plotparm[4] = degree; plotparm[5] = templatename; plotparm[6] = objectname; plotparm[7] = self.length
            plotparm[8] = self.smallerwaves; plotparm[9] = self.largerwaves; plotparm[10] = value
            jumpcore[0] = True
            if run is True:
                if allplots[0] is False:
                    pass
                elif allplots[0] is True:
                    try:
                        self.window3 = MultiView()
                        self.window3.show()
                    except ValueError:
                        self.ui.infobox.append('<font color ="red">Please Make sure that file names are entered in the boxs</font>')
                    except IOError:
                        self.ui.infobox.append('<font color ="red">Please Make sure that file names are spelled correctly</font>')
                else:
                    self.ui.infobox.append('<font color = "red">An unknown error has occured, please make sure all inputs are correct</font>')


# This is plotter code, at some point it may be nice to move this class (During the great reorginazation of code to come)
class Plotter():

    # Corplot function that calls the ccofig function from GUI function to extract the required data
    # incidentaly this will be completely reorganized in the great reorganization of code to come
    # I wrote the comment like a week ago now and I have yet to begin the great reorganization of code
    # as my younger naive self called it, rather it has been a slow logical change in the code base
    # whatever, maybe one day.
    @staticmethod
    def corplot(degree, templatename, objectname, order, num, larger, smaller, show, value, doPlot):
        # Creates a matplotlib figure of given size (will at some point be configuarble in the forcoming settings menu)
        # fig=plt.figure(figsize=(10, 7))
        # Adds the ccorfig subplot
        # ccorfig = fig.add_subplot(1, 1, 1)
        # fetches the data from the ccor function in Advanced Plotting by calling the function, data is returnted as a
        #   2 element dictionary, so then when its plotted below there its is called with the dictionaty nameing
        if doPlot is True and order < 62:
            print 'here'
            finished = [False]
            data = AdvancedPlotting.ccor(objectname, templatename, degree, order, num, larger, smaller, value)
            fig = plt.figure(figsize=(10, 10))
            if show is False:
                ccorfig = fig.add_subplot(1, 1, 1)
            else:
                ccorfig = fig.add_subplot(2,1,1)
                AdvancedPlotting.waveshower(fig, templatename, objectname, order, degree)
            index = 0
            maximum = data['fit'](data['offset'])[0]
            for count in range(len(data['fit'](data['offset']))):
                if data['fit'](data['offset'])[count] > maximum:
                    maximum = data['fit'](data['offset'])[count]
                    index = count
            index = value/2 - index
            tempvelocity = index * data['dispersion']
            ccorfig.plot(data['offset'], data['correlation'], label='Raw Data | Relative Velocity: ' + str(tempvelocity))
            ccorfig.plot(data['offset'], data['fit'](data['offset']), label='Gaussian Fit | x at max: ' + str(index))
            ccorfig.set_xlabel('Offset')
            ccorfig.set_ylabel('Correlation Coefficient')
            ccorfig.set_title('Cross Correlation, order number: ' + str(order))
            plt.legend(loc = 'best')
            # This allows one to move between orders in C
            def plotcontrol(event):
                keydown = event.key
                # A advances in the cross correlation, nothing is printed out as of yet, it just produced the plot
                # eventually this whole function if gonna be reorganized to allow for multiple figures to be displayed over
                if keydown == 'a' or keydown == 'A':
                    plt.close()
                    Plotter.corplot(degree, templatename, objectname, order + 1, num, larger, smaller, compare[0], value, doPlot)
                elif keydown == 'c' or keydown == 'C':
                    plt.close()
                    compare[0] = not compare[0]
                    Plotter.corplot(degree, templatename, objectname, order, num, larger, smaller, compare[0], value, doPlot)
            # connects to the key press event function
            fig.canvas.mpl_connect('key_press_event', plotcontrol)
            plt.show()
        else:
            del velocity[:]
            for i in range(62):
                data = AdvancedPlotting.ccor(objectname, templatename, degree, i, num, larger, smaller, value)
                index = 0
                maximum = data['fit'](data['offset'])[0]
                for count in range(len(data['fit'](data['offset']))):
                    if data['fit'](data['offset'])[count] > maximum:
                        maximum = data['fit'](data['offset'])[count]
                        index = count
                index = value/2 - index
                velocity.append(index * data['dispersion'])
                FullCC.append(data['correlation'])
                FullO.append(data['offset'])
                FullGaus.append(data['fit'](data['offset']))
            if allplots[0] is False:
                CCWindow.window3 = MultiView()
                CCWindow.window3.show()

            else:
                pass
        print 'now here'

    # The plot controller for the plot that plots (enough plots for you yet?) stacked plots (there we go)
    @staticmethod
    def stackplot(stackfile, allimages, num, start, degree, shouldfit):

        # Initialized the matplotlib figure
        fig = plt.figure(figsize=(10, 7))

        # Opens the file with the path to files list in it and reads that into an array, this code is ideentical more
        # or less to code that has been written earlier in BPlot and other classes for reading in data files
        pathlist = open(stackfile, 'rb')
        patharray = []
        for line in pathlist:
            patharray.append(line)

        # figures out whether or not to stack all the images based on a global namespace variable (that I should change
        # to a local namespace variable bu that is neither here nor there for the time being), I actually want to change
        # This more fundamentally so that when all images is stacked, instead of flipping a boolean it just counts and
        # sets a value, this will allow for a change in the number stacked when the button is presses, Currently very
        # low priority
        if allimages is True:
            stacknum = len(patharray)

        # if not stack all, how many stack
        else:
            if num > len(patharray):
                num = len(patharray)
            stacknum = num

        # This applies an offset to stacked / Normalized orders to that the velocity offset can be more clearly seen
        offset = 0
        for i in range(stacknum):
            name = patharray[i]
            name = name[:-1]
            offset += 0.1
            PlotFunctionality.plot(name, start, showfit[0], shouldfit, degree, fig, offset)

        # You are probably wondering (I know I am) why this seamingly important line is commented out, and why when it
        # is not commented out MAC OSX systems go cray cray, they shouldn't go cray cray but they do go cray cray
        # that was odd, moving on, keep this commmented out until that bug is sorted out or OS X systems will go
        # cray cray
        #plt.tight_layout()
        plt.ion()
        plt.show()

        # gets keyboard input and calls plot functions
        def plotcontrol(event):
            keydown = event.key
            if keydown == 'a' or keydown == 'A':
                # closes the window
                plt.close()

                # Checks to to keep you from going negative, I actually don't know if this works right now but its
                # so low on my priority list that I haven't given it any thought (I mean not an ioda) since I first
                # wrote this line, so yea.
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
            elif keydown == 'j' or keydown == 'J':
                MyForm.window3 = OrderJump()
                MyForm.window3.show()

        # Connects to the matplot lib keypress function
        fig.canvas.mpl_connect('key_press_event', plotcontrol)

    # function called when no images will be staked, this is basically obsolete, and should be at some point replace
    # except no, idk, im having a mental break down about this
    @staticmethod
    def nstackplot(name, start, degree, shouldfit):
        # same deal here as with stackplot above
        fig = plt.figure(figsize=(10, 7))
        PlotFunctionality.plot(name, start, showfit[0], shouldfit, degree, fig, 0)
        #plt.tight_layout()
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
            elif keydown == 'j' or keydown == 'J':
                MyForm.window3 = OrderJump()
                MyForm.window3.show()
        fig.canvas.mpl_connect('key_press_event', plotcontrol)




# Bascically the most important section of code in the whole code because it makes everything start, its also the
# only section of code in this entire program I don't really understand (I got this section from a tutorial)
# scratch that I get it now (this line was written like 2 weeks after the pervious two)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())