# Spectral Analysis Utility (SAUL)
# Thomas Boudreaux, Paddy Clancy, and Dr. Brad N. Barlow
# Developed at High Point University
# Under Lesser General Public Liscense (LGPL)
from General import *
prerun = open('prerun.log','w')
#  GUI file import statements
print >>prerun, 'Cheking for GUI files'
try:
    from Editor import Ui_MainWindow
    from MultiplotViewerTesttwo import Ui_MultiplotViewer
    from closeyn import Ui_Dialog
    from SAULGui import Ui_SAUL
    print >>prerun, 'GUI files OK'
except ImportError:
    print >>prerun, 'Some or all GUI files missing, please check to make sure that you donwloaded the entire ' \
                    'package and re-run'
    exit()
# importer for pip module
print >>prerun, 'Checking pip'
try:
    import pip
    print >>prerun, 'pip OK'
except ImportError:
    print >>prerun, 'pip not found, will try to continue running program, if all other dependanceied are installed ' \
                    'program should run OK'

packages = ['import random', 'import matplotlib.pyplot as plt', 'import os', 'from PyQt4 import QtGui, QtCore',
            'import webbrowser', 'from astropy.io import fits', 'import sys', 'import time',
            'from matplotlib.backend_bases import key_press_handler', 'from pylab import *',
            'from matplotlib.widgets import CheckButtons', 'from PyQt4.uic import loadUiType', 'import jplephem',
            'import de423', 'import jdcal', 'from matplotlib.figure import Figure',
            'from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas,NavigationToolbar2QT as '
            'NavigationToolbar)',
            'import astropy.time as astrotime', 'import astropy.coordinates as coords', 'import astropy.units as unit',
            'import astropy.constants as const', 'from astropy.modeling import models,fitting',
            'from scipy import asarray as ar,exp', 'from scipy.optimize import curve_fit', 'import math',
            'import numpy as np', 'import ephem', 'from matplotlib import gridspec']

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
                    print >>prerun, 'An Unkown Error has occured while importing or installing', package, 'Please ' \
                                                                                                          'consider ' \
                                                                                                          'using ' \
                                                                                                          'annaconda'
                    code.append(0)
                    code.append(1)
                    code.append(0)
            cont = True
            if installpac == 'n':
                print >>prerun, package, 'will not be installed, the program cannot run without this packages and ' \
                                         'will now shutdown, please consider using anaconda'
                print package, 'will not be installed, the program cannot run without this packages and will now ' \
                               'shutdown, please consider using anaconda'
                cont = True
                code.append(0)
                code.append(0)
                code.append(0)
                exit()
            else:
                print 'Please Enter either Y or n'
print >>prerun, 'Trying other program dependancy files'
try:
    from GuiFunction import *
    from consolcontrol import *
except ImportError:
    print >>prerun, 'Some or all internal dependancies were not met, please make sure that you downloaded the entire ' \
                    'package and re-run'
    exit()
# Checks os for compatability
mac = PreChecks.oscheck()
for precode in range(len(code)):
    code[precode] = str(code[precode])
code = ''.join(code)
savecode = code
stringcode = str(code)
code = int(code, 2)
flip = False
for didget in stringcode:
    if didget != 1:
        flip = True
if flip is True:
    code = "ALL OKAY (1)"
else:
    code = 'Pakages were installed or not found [This is a standard completion messgage, there is nothign ' \
           'to fret about] ' + str(code)

print >>prerun, 'Pre-run Checks finished with code:', code, '(', savecode, ')'
prerun.close()
print 'Pre-run Checks finished with code:', code
# These are here to allow for global variables passe betweel all classes, at some point these
# Should be replaced by local namespace variables, however I have yet to get around to that
c = 299792.458
HJD = [0]
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
funcconf = [['1','Null', 'Function1'], ['2', 'Null', 'Function2'], ['3', 'Null', 'Function3'], ['4', 'Null',
                                                                                                'Function4']]
jumpcore = [False]
compare = [False]
simplefilearray = []
foundit = False
whilecounter = 0
masterfilearray = []
flist = os.listdir('.')
numorders = [62]
FullCC = [None] * numorders[0]
FullO = [None] * numorders[0]
FullGaus = [None] * numorders[0]
FullAmp = [None] * numorders[0]
global FullHJD
FullHCV = [None] * numorders[0]
allplots = [False]
checkPlots = [True]*62
velocity = []
namePass = ['GenericStar', 'GenericStar']
global OrbitlPeriod

centroids = [None] * numorders[0]
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
####################
# Insert Code here #
####################

class SAUL(QtGui.QMainWindow):
    def __init__(self, parent=None):
        # Ininitlazation of the Widget
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_SAUL()
        self.ui.setupUi(self)
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
        # if len(saverun) >= 1:
        #     UserFunctions[0] = lastrun[0][1]
        #
        #     self.ui.UseFunction1.clicked.connect(self.functiontie1)
        #     self.ui.UseFunction1.setText(lastrun[0][2])
        #     funcconf[0] = lastrun[0]
        # if len(saverun) >= 2:
        #     UserFunctions[1] = lastrun[1][1]
        #     self.ui.UserFunction2.clicked.connect(self.functiontie2)
        #     self.ui.UserFunction2.setText(lastrun[1][2])
        #     funcconf[1] = lastrun[1]
        # if len(saverun) >= 3:
        #     UserFunctions[2] = lastrun[2][1]
        #     self.ui.UserFuntion3.clicked.connect(self.functiontie3)
        #     self.ui.UserFuntion3.setText(lastrun[2][2])
        #     funcconf[2] = lastrun[2]
        # if len(saverun) == 4:
        #     UserFunctions[3] = lastrun[3][1]
        #     self.ui.userFuntion4.clicked.connect(self.functiontie4)
        #     self.ui.userFuntion4.setText(lastrun[3][2])
        #     funcconf[3] = lastrun[3]

        if len(masterfilearray) is not 0:
            pathbool = True
            for k in range(len(masterfilearray)):
                starname = masterfilearray[k][0][6:]
                self.ui.PathFilesBrowser.addItem('Star name: ' + starname)
                self.ui.PathFilesBrowser.addItem('File name: PathTo' + starname)
                for p in range(len(masterfilearray[k])):
                    if p is not 0:
                        self.ui.PathFilesBrowser.addItem(masterfilearray[k][p])
        # These control most of the button assignments in the main GUI
        self.ui.GeneralInfo.append('<font color = "green"> SAUL Version 0.6<br>Written by Paddy Clancy and Thomas Boudreaux '
                              ' - 2016</font><br>')
        self.ui.GeneralInfo.append('<font color = "blue"> Module and OS Checks OK</font><br>')
        self.ui.GeneralInfo.append('<font color = "blue"> type "lcom" for a list of avalibel commands</font><br>')
        if pathbool is True:
            self.ui.GeneralInfo.append('<font color = "green"> Path Files Successfully located in working directory</font>'
                                  '<br>')
            self.ui.GeneratePathFile.setStyleSheet("background-color: green; color: white")
        #self.ui.function1.setStyleSheet("background-color: red; color: black")
        # These are the GUI functional ties for the main window
        self.ui.GeneratePathFile.clicked.connect(self.generatepath)
        # attempting to replace some of these long functions with lambda statments in otder to clean up code
        self.ui.Quit.clicked.connect(lambda: exit())
        # self.ui.stackIm.stateChanged.connect(lambda: usearray.__setitem__(0, not usearray[0]))
        # self.ui.allStack.stateChanged.connect(lambda: usearray.__setitem__(1, not usearray[1]))
        self.ui.BSPPlot.clicked.connect(self.plot)
        self.ui.Secret.clicked.connect(self.secret)
        self.ui.Normalizeyn.stateChanged.connect(self.fitter)
        # self.ui.function1.clicked.connect(self.showfit)
        # self.ui.function2.clicked.connect(self.correlate)
        # self.ui.OrbitalFit.clicked.connect(self.orb)
        # self.ui.function4.clicked.connect(self.gaussian)
        # self.ui.info.clicked.connect(self.info)
        self.ui.Reload.clicked.connect(BSPSEss.reload)

        # These initialize the other windows as empty objects in the Main GUI controller
        self.window2 = None
        self.window3 = None
        self.window3 = None
        self.window4 = None
        self.window5 = None

        self.height1 = self.ui.PlotOne.height()
        self.width1 = self.ui.PlotOne.width()
        self.height2 = self.ui.PlotTwo.height()
        self.width2 = self.ui.PlotTwo.width()
        self.FigOne = Figure(figsize=(self.height1, self.width1), dpi=85, facecolor='w')
        self.FigTwo = Figure(figsize=(self.height2, self.width2), dpi=85, facecolor='w')
        self.CanvasOne = FigureCanvas(self.FigOne)
        self.CanvasTwo = FigureCanvas(self.FigTwo)
        self.CanvasOne.setParent(self.ui.PlotOne)
        self.CanvasTwo.setParent(self.ui.PlotTwo)
    ###########################
    #   GUI tie in functions  #
    ###########################
    #
    # def orb(self):
    #     self.window5 = OrbitalFitter()
    #     self.window5.show()

    # def gaussian(self):
    #     self.window4 = GaussianWindow(self)
    #     self.window4.show()

    # Easter Egg
    def secret(self):
        r = random.randrange(1, 5)
        if r == 1:
            self.ui.GeneralInfo.append('<font color = "green"> Displaying a possible Answer to life - Credit: http://d.justpo'
                                  '.st/images/2013/04/b83fb1b7222c18934e59c5b1bd2f43bd.jpg</font><br>')
            webbrowser.open('http://d.justpo.st/images/2013/04/b83fb1b7222c18934e59c5b1bd2f43bd.jpg')
        elif r == 2:
            self.ui.GeneralInfo.append('<font color = "green"> Displaying a possible Answer to life - Credit: http://sf.co.'
                                  'ua/id90453</font><br>')
            webbrowser.open('http://sf.co.ua/id90453')
        elif r == 3:
            self.ui.GeneralInfo.append('<font color = "green"> Displaying a possible Answer to life - Credit: https://s-media'
                                  '-cache-ak0.pinimg.com/236x/2f/88/26/2f8826f5a6a97006ecd350211eb584ee.jpg</font><br>')
            webbrowser.open('https://s-media-cache-ak0.pinimg.com/236x/2f/88/26/2f8826f5a6a97006ecd350211eb584ee.jpg')
        elif r == 4:
            self.ui.GeneralInfo.append('<font color = "green"> Displaying a possible Answer to life - Credit: '
                                  'http://nicolascage.us/wp-content/uploads/2013/09/Universe-Cupcake.jpg</font><br>')
            webbrowser.open('http://nicolascage.us/wp-content/uploads/2013/09/Universe-Cupcake.jpg')

    # This function controls all keyPresses, it runs at all times in the main window and grabs keypress from that
    def keyPressEvent(self, e):

        # Return controller for consol input
        if e.key() == QtCore.Qt.Key_Return:
            command = self.ui.Command.text()
            commandcomp = str.split(str(command))
            iscommand = commandcomp[0]
            commandcomp.pop(0)

            # Passes the parsed command and parameters into the consol control class routing function
            # the routing function returns a string
            string = BSPS.route(iscommand, commandcomp)

            # appends the entered command to the consol
            self.ui.Terminal.append('<font color = green>' + command + '</font>')

            # all these //word are the syntax for commands that have special functions
            # clears the terminal window
            if string == '//clear':
                self.ui.Terminal.clear()
                string = None

            elif string == '//PDC':
                string = None

            elif string == '//EIDP':
                string = '<font color = "red">unable to display standard plot, please make sure all parameters are' \
                         'correct, use -help or ? for assisnatnce</font>'
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

            elif string == '//setHET':
                numorders[0] = 44

            elif string == '//setCHIRON':
                numorders[0] = 62

            elif string == '//COMP':
                string = '<font color = "olive">Displaying Spectral comparison for ' + commandcomp[0]

            # Checks to make sure that the sring exists
            if string:
                # appends the sting returnes from the routing function to the consol, if it has not been deinitialized
                # in the command logic above
                self.ui.Terminal.append(string)
            self.ui.Command.clear()
            commands.append(command)

        # Next and previous command for consol input
        elif e.key() == QtCore.Qt.Key_Down:
            commandnum[0] -= 1
            self.ui.Command.setText(commands[commandnum[0]])
        elif e.key() == QtCore.Qt.Key_Up:
            commandnum[0] += 1
            self.ui.Command.setText(commands[commandnum[0]])
        elif e.key() == QtCore.Qt.Key_J:
            self.jumpTo()

    # Prints the info screen from the info.txt file in the directory tree to the consol
    def info(self):
        infofile = open('info.txt', 'rb')
        infotxt = infofile.read()
        self.ui.Terminal.append(infotxt)

    # Lists the directories in the working directory in the consol
    # This is due to be replaced when the language is implimented with the ls command built into the language

    def functiontie1(self):
        text = BSPSEss.pyrun(UserFunctions[0])
        self.ui.Terminal.append(text)

    def functiontie2(self):
        text = BSPSEss.pyrun(UserFunctions[1])
        self.ui.Terminal.append(text)

    def functiontie3(self):
        text = BSPSEss.pyrun(UserFunctions[2])
        self.ui.Terminal.append(text)

    def functiontie4(self):
        text = BSPSEss.pyrun(UserFunctions[3])
        self.ui.Terminal.append(text)

    def LS(self):
        dirs = os.listdir('.')
        for i in range(len(dirs)):
            self.ui.Terminal.append('<font color = "blue">' + dirs[i] + '</font>')
        self.ui.Terminal.append('<font color = "black"> ---------------------------- <font><br>')

    # General Not Implimented function

    # This generates the Path Files by searching through the directory tree for stars with different names
    # This is due to be replaced by a command in the language when the language is implimented
    def generatepath(self):
        count = 0
        namearray = []
        self.ui.PathFilesBrowser.clear()
        masterfilearray = None
        masterfilearray = []
        smallarray = []
        largearray = []
        # Generates a list with unique names for all objects
        for root, dirs, files in os.walk('.', topdown=True):
            for file in files:
                if 'achi' in file or 'bhrs' in file and '.fitsC' not in file:
                    filename = os.path.join(root, file)
                    sp = fits.open(filename)
                    hdu = sp[0].header
                    objname = (hdu['OBJECT'])
                    objname = objname.split(' ')[0]
                    if objname not in namearray:
                        namearray.append(objname)

        # Generates the Lists paths to stars, and addes those to the list widget
        for i in range(len(namearray)):
            starname = namearray[i]
            self.ui.PathFilesBrowser.addItem('Star name: ' + starname)
            self.ui.PathFilesBrowser.addItem('File name: PathTo' + starname)
            nameforfile = 'PathTo' + starname
            smallarray.append(nameforfile)
            printlist = open(nameforfile, 'w')
            for root, dirs, files in os.walk('.', topdown=True):
                for file in files:
                    if 'achi' in file or 'bhrs' in file and 'fitsC' not in file:
                        name = os.path.join(root, file)
                        sp = fits.open(name)
                        hdu = sp[0].header
                        objname1 = (hdu['OBJECT'])
                        if starname in objname1:
                            print >>printlist, name
                            self.ui.PathFilesBrowser.addItem(name)
                            smallarray.append(name)
                            count += 1
                            progress = (count/len(namearray))*100
                            # self.ui.PathFileProgress.setValue(progress)
                            masterfilearray.append(smallarray)

        if len(namearray) > 0:
            self.ui.Terminal.append('<font color = "green"> Path Files Successfully generated</font><br>')
            self.ui.GeneratePathFile.setStyleSheet("background-color: green; color: white")
        else:
            self.ui.Terminal.append('<font color = "red"> No Path Files Generated, is your data folder in the program '
                                  'direcotry?</font><br>')
            self.ui.GeneratePathFile.setStyleSheet("background-color: red; color: white")

    # This grabs the infomration for the plot function and then passed it to the Plotter class to plot the function
    # This could probably be cleaned up a bit, however thats a relativly low priority given that its not super
    #   as is right now
    def plotold(self):
        # Closes whatever figure is open so that the screen is not overrun with windows everytime Plot is pressed
        # the effect of this is that one can modify parmaters in the GUI and then replot by pressing plot
        plt.close(1)

        # Fetch the values and strings stored in relevent text fields
        degree = self.ui.DegreeBSP.value()
        plotparm[0] = degree
        try:
            FilePath = self.ui.BSPPath.text()
            if 'PathTo' in FilePath:
                numToStack = self.ui.NumToStack.value()
                plotparm[1] = FilePath; plotparm[2] = numToStack
                stack = True
            else:
                stack = False
                plotparm[3] = FilePath
        except IOError:
            stack = False
            self.ui.Terminal.append('<font color = "red"> No Such File found, please check spelling and try again </font>')

        order = 1  # starting order

        normalize = self.ui.Normalizeyn.isChecked()

        if normalize is True:
            if self.ui.ShowBoth.isChecked() is True:
                ax1 = self.FigOne.add_subplot(111, xlabel='wavelength' + '(' + u'\212B' + ')', ylabel='Flux', title='Spectrum')
                ax2 = self.FigTwo.add_subplot(111, xlabel='wavelength' + '(' + u'\212B' + ')', ylabel='Normalize Flux', title='Spectrum')
            elif self.ui.ShowNormOnly.isChecked() is True:
                ax1 = self.FigOne.add_subplot(111, xlabel='wavelength' + '(' + u'\212B' + ')', ylabel='Normalize Flux', title='Spectrum')
            elif self.ui.ShowNonNorm.isChecked() is True:
                ax1 = self.FigOne.add_subplot(111, xlabel='wavelength' + '(' + u'\212B' + ')', ylabel='Flux', title='Spectrum')
            else:
                self.ui.GeneralInfo.append("<font color='red'> An Unknown error has occured, please close SAUL and reopen </font>")
                raise IOError('ERROR - 42: AN UNKNOWN ERROR HAS OCCURECD WHEN EXECUTIG SAUL')

        # Determins whether to use stack plot or nstack plot, would like to figure out a better way to to this
        # than arrays but that is currently not a super high priority
        if stack is True:
            # Plotter.stackplot(FilePath, usearray[1], numToStack, order, degree, fit[0])
            offset = 0
            files = open(FilePath, 'w').readlines()
            met1 = ['Wavelength', 'Flux', 'Spectrum with ' + str(numToStack) + ' orders shown']
            met2 = ['Wavelength', 'Normalized Flux', 'Spectrum with ' + str(numToStack) + ' orders shown']
            for i in range(numToStack):
                data = GUIPlotter.spectra(files[i],order, degree, offset)
                data['f'] = [p + offset for p in data['f']]
                data['ypoly'] = [p + offset for p in data['ypoly']]
                data['ynew'] = [p + offset for p in data['ynew']]
                offset += 0.1
                self.plot(data['w'], data['f'], met1)
                self.plot(data['w'], data['ynew'], met2)
                self.plot(data['w'], data['ypoly'], None)
        else:

        jumpcore[0] = False
        # self.jumpTo()

    def plot(self, xdat, ydat, metadata, plotnum=1, clear=True):
        if metadata is not None:
            if plotnum == 1:
                ax = self.FigOne.add_subplot(111, xlabel=metadata[0], ylabel=metadata[1], title=metadata[2])
                ax.plot(xdat, ydat)
            elif plotnum == 2:
                ax = self.FigTwo.add_subplot(111, xlabel=metadata[0], ylabel=metadata[1], title=metadata[2])
                ax.plot(xdat, ydat)
            else:
                raise ValueError('ERROR - 1: ONLY TWO PLOTS PRESENT IN THE SAUL GUI, DID YOU DO SOMETHING WRONG WHEN '
                                 'CALLING THE FUNCTION')
        else:
            if plotnum == 1:
                ax = self.FigOne.add_subplot(111)
                ax.plot(xdat, ydat)
            elif plotnum == 2:
                ax = self.FigTwo.add_subplot(111)
                ax.plot(xdat, ydat)
            else:
                raise ValueError('ERROR - 1: ONLY TWO PLOTS PRESENT IN THE SAUL GUI, DID YOU DO SOMETHING WRONG WHEN '
                                 'CALLING THE FUNCTION')
    # This controls the "show fit" button, its color and the boolean behind it. Again I would like to come up with
    # a better way to store the booleans behind buttons, but that is for a latter date
    def showfit(self):
        if fit[0] is True:
            showfit[0] = not showfit[0]
            if showfit[0] is True:
                self.ui.function1.setStyleSheet("background-color: green; color: white")
            else:
                self.ui.function1.setStyleSheet("background-color: red; color: black")
        elif fit[0] is False:
                self.ui.consol.append('<font color = "red"> Cannot Show function unless a function is being fit</font>'
                                      '<br>')

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



class MPLPlotter():
    @staticmethod
    def orbplot(TimeArray, RVArray, ErrorArray, period, foldphase=True, linearT=False, SinT=False):
        residualArray = [None] * len(TimeArray)
        gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
        if linearT is True:
            # def cosine(x, amp, phase, offset):
            #     global OrbitlPeriod
            #     return amp * np.sin((((2*math.pi)*x)/OrbitlPeriod) + phase) + offset
            def othercosine(x, amp, phase, offset, P1):
                global OrbitlPeriod
                return P1*x + amp * np.sin((((2*math.pi)*x)/OrbitlPeriod) + phase) + offset
            diff = max(RVArray) - min(RVArray)
            if foldphase is False:
                meanTime = sum(TimeArray)/len(TimeArray)
                for x in range(len(TimeArray)):
                    TimeArray[x] -= meanTime
            OrbFig = plt.figure(figsize=(10, 10))
            RVplot = OrbFig.add_subplot(gs[0])
            ResidualPlot = OrbFig.add_subplot(gs[1])
            npTimeArray = np.array(TimeArray)
            RVplot.plot(TimeArray, RVArray, 'o')
            npRVArray = np.array(RVArray)
            # siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), float(period), 0, -50])
            # siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), 0, -50])
            siny, covar = curve_fit(othercosine, npTimeArray, npRVArray, p0=[float(diff/2), 0, -50, 0])
            perr = np.sqrt(np.diag(covar))
            if foldphase is False:
                clean = np.linspace(min(npTimeArray)-10, max(npTimeArray)+10, 5000)
            else:
                clean = np.linspace(min(npTimeArray)-1, max(npTimeArray)+1, 5000)
            # RVplot.plot(clean, cosine(clean, *siny), label='RV semiamplitude: ' + str(siny[0]) + '+-' + str(perr[0]))
            RVplot.plot(clean, othercosine(clean, *siny), label='RV semiamplitude: ' + str(siny[0]) + '+-' + str(perr[0]))
            if foldphase is False:
                RVplot.set_xlabel('Period (Days)')
            else:
                RVplot.set_xlabel('Period (Phase)')
            RVplot.set_ylabel('RV (Km*s^-1)')
            for i in range(len(RVArray)):
                # fitValue = cosine(TimeArray[i], *siny)
                fitValue = othercosine(TimeArray[i], *siny)
                residualArray[i] = fitValue - RVArray[i]
            RVplot.errorbar(npTimeArray, npRVArray, yerr=ErrorArray, fmt='o')
            ResidualPlot.plot(TimeArray, residualArray, 's')
            ResidualPlot.errorbar(TimeArray, residualArray, yerr=ErrorArray, fmt='s')
            ResidualPlot.set_title('Residuals')
            if foldphase is False:
                ResidualPlot.set_xlabel('Time (Days)')
            else:
                ResidualPlot.set_xlabel('Time (Phase)')
            ResidualPlot.set_ylabel('Function - Data Point')
            ResidualPlot.axhline(0, color='black', linestyle='--')
            RVplot.set_title('RV vs Phase')
            RVplot.legend(loc="best")
            RVplot.axhline(siny[2], color="black", linestyle='--')
            plt.show()

            print 'RV semiamplitude:', siny[0], '+-', perr[0]
            print 'System Velocity:', siny[2], '+-', perr[2]
            # return {'Xdata': npTimeArray, 'Ydata': npRVArray, 'function': cosine, 'smooth': clean, 'fit': siny}
            return {'Xdata': npTimeArray, 'Ydata': npRVArray, 'function': othercosine, 'smooth': clean, 'fit': siny}
        elif SinT is True:
            def SinTrendFit(x, amp1, phase1, offset1, LP, amp2, phase2):
                global OrbitlPeriod
                return amp2 * np.sin((((2*math.pi)*x)/LP) + phase2) + amp1 * np.sin((((2*math.pi)*x)/OrbitlPeriod) + phase1) + offset1
            diff = max(RVArray) - min(RVArray)
            if foldphase is False:
                meanTime = sum(TimeArray)/len(TimeArray)
                for x in range(len(TimeArray)):
                    TimeArray[x] -= meanTime
            OrbFig = plt.figure(figsize=(10, 10))
            RVplot = OrbFig.add_subplot(gs[0])
            ResidualPlot = OrbFig.add_subplot(gs[1])
            npTimeArray = np.array(TimeArray)
            RVplot.plot(TimeArray, RVArray, 'o')
            npRVArray = np.array(RVArray)
            # siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), float(period), 0, -50])
            # siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), 0, -50])
            siny, covar = curve_fit(SinTrendFit, npTimeArray, npRVArray, p0=[float(diff/2), 0, -50, 50, 10, 0])
            perr = np.sqrt(np.diag(covar))
            if foldphase is False:
                clean = np.linspace(min(npTimeArray)-10, max(npTimeArray)+10, 5000)
            else:
                clean = np.linspace(min(npTimeArray)-1, max(npTimeArray)+1, 5000)
            # RVplot.plot(clean, cosine(clean, *siny), label='RV semiamplitude: ' + str(siny[0]) + '+-' + str(perr[0]))
            RVplot.plot(clean, SinTrendFit(clean, *siny), label='RV semiamplitude: ' + str(siny[0]) + '+-' + str(perr[0]))
            if foldphase is False:
                RVplot.set_xlabel('Period (Days)')
            else:
                RVplot.set_xlabel('Period (Phase)')
            RVplot.set_ylabel('RV (Km*s^-1)')
            for i in range(len(RVArray)):
                # fitValue = cosine(TimeArray[i], *siny)
                fitValue = SinTrendFit(TimeArray[i], *siny)
                residualArray[i] = fitValue - RVArray[i]
            RVplot.errorbar(npTimeArray, npRVArray, yerr=ErrorArray, fmt='o')
            ResidualPlot.plot(TimeArray, residualArray, 's')
            ResidualPlot.errorbar(TimeArray, residualArray, yerr=ErrorArray, fmt='s')
            ResidualPlot.set_title('Residuals')
            if foldphase is False:
                ResidualPlot.set_xlabel('Time (Days)')
            else:
                ResidualPlot.set_xlabel('Time (Phase)')
            ResidualPlot.set_ylabel('Function - Data Point')
            ResidualPlot.axhline(0, color='black', linestyle='--')
            RVplot.set_title('RV vs Phase')
            RVplot.legend(loc="best")
            RVplot.axhline(siny[2], color="grey", linestyle='--')
            plt.show()

            print 'RV semiamplitude:', siny[0], '+-', perr[0]
            print 'System Velocity:', siny[2], '+-', perr[2]
            # return {'Xdata': npTimeArray, 'Ydata': npRVArray, 'function': cosine, 'smooth': clean, 'fit': siny}
            return {'Xdata': npTimeArray, 'Ydata': npRVArray, 'function': SinTrendFit, 'smooth': clean, 'fit': siny}
        else:
            def cosine(x, amp, phase, offset):
                global OrbitlPeriod
                return amp * np.sin((((2*math.pi)*x)/OrbitlPeriod) + phase) + offset
            diff = max(RVArray) - min(RVArray)
            if foldphase is False:
                meanTime = sum(TimeArray)/len(TimeArray)
                for x in range(len(TimeArray)):
                    TimeArray[x] -= meanTime
            OrbFig = plt.figure(figsize=(10, 10))
            RVplot = OrbFig.add_subplot(gs[0])
            ResidualPlot = OrbFig.add_subplot(gs[1])
            npTimeArray = np.array(TimeArray)
            RVplot.plot(TimeArray, RVArray, 'o')
            npRVArray = np.array(RVArray)
            # siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), float(period), 0, -50])
            # siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), 0, -50])
            siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), 0, -50])
            perr = np.sqrt(np.diag(covar))
            if foldphase is False:
                clean = np.linspace(min(npTimeArray)-10, max(npTimeArray)+10, 5000)
            else:
                clean = np.linspace(min(npTimeArray)-1, max(npTimeArray)+1, 5000)
            # RVplot.plot(clean, cosine(clean, *siny), label='RV semiamplitude: ' + str(siny[0]) + '+-' + str(perr[0]))
            RVplot.plot(clean, cosine(clean, *siny), label='RV semiamplitude: ' + str(siny[0]) + '+-' + str(perr[0]))
            if foldphase is False:
                RVplot.set_xlabel('Period (Days)')
            else:
                RVplot.set_xlabel('Period (Phase)')
            RVplot.set_ylabel('RV (Km*s^-1)')
            for i in range(len(RVArray)):
                # fitValue = cosine(TimeArray[i], *siny)
                fitValue = cosine(TimeArray[i], *siny)
                residualArray[i] = fitValue - RVArray[i]
            RVplot.errorbar(npTimeArray, npRVArray, yerr=ErrorArray, fmt='o')
            ResidualPlot.plot(TimeArray, residualArray, 's')
            ResidualPlot.errorbar(TimeArray, residualArray, yerr=ErrorArray, fmt='s')
            ResidualPlot.set_title('Residuals')
            if foldphase is False:
                ResidualPlot.set_xlabel('Time (Days)')
            else:
                ResidualPlot.set_xlabel('Time (Phase)')
            ResidualPlot.set_ylabel('Function - Data Point')
            ResidualPlot.axhline(0, color='black', linestyle='--')
            RVplot.set_title('RV vs Phase')
            RVplot.legend(loc="best")
            RVplot.axhline(siny[2], color="grey", linestyle='--')
            plt.show()

            print 'RV semiamplitude:', siny[0], '+-', perr[0]
            print 'System Velocity:', siny[2], '+-', perr[2]
            # return {'Xdata': npTimeArray, 'Ydata': npRVArray, 'function': cosine, 'smooth': clean, 'fit': siny}
            return {'Xdata': npTimeArray, 'Ydata': npRVArray, 'function': cosine, 'smooth': clean, 'fit': siny}

    # Corplot function that calls the ccofig function from GUI function to extract the required data
    # incidentaly this will be completely reorganized in the great reorganization of code to come
    # I wrote the comment like a week ago now and I have yet to begin the great reorganization of code
    # as my younger naive self called it, rather it has been a slow logical change in the code base
    # whatever, maybe one day.
    @staticmethod
    def corplot(degree, templatename, objectname, order, num, larger, smaller, show, value, doPlot, autofit, xcoord=None,
                ycoord=None, x1bound=5, x2bound=5):
        global FullHJD
        fitsobject = str(objectname)
        objectfits = fits.open(fitsobject)
        starname = objectfits[0].header['OBJECT']
        templatefits = fits.open(str(templatename))
        namePass[1] = templatefits[0].header['OBJECT']
        namePass[0] = starname
        # Creates a matplotlib figure of given size (will at some point be configuarble in the forcoming settings menu)
        # fig=plt.figure(figsize=(10, 7))
        # Adds the ccorfig subplot
        # ccorfig = fig.add_subplot(1, 1, 1)
        # fetches the data from the ccor function in Advanced Plotting by calling the function, data is returnted as a
        # 2 element dictionary, so then when its plotted below there its is called with the dictionaty nameing
        userFit = [False]
        if doPlot is True and order <= numorders[0]:
            global gcount
            gcount = 0
            global gdata
            gdata = [None, None]
            finished = [False]
            data = AdvancedPlotting.ccor(objectname, templatename, degree, order-1, num, larger, smaller, value)
            fig = plt.figure(figsize=(10, 10))
            if show is False:
                ccorfig = fig.add_subplot(1, 1, 1)
            else:
                ccorfig = fig.add_subplot(2, 1, 1)
                AdvancedPlotting.waveshower(fig, templatename, objectname, order, degree)
            index = 0
            maximum = data['correlation'][0]
            center = 0
            if autofit is True:
                for count in range(len(data['correlation'])):
                    if data['correlation'][count] > maximum:
                        maximum = data['correlation'][count]
                        center = data['offset'][count]
                        index = count
            else:
                try:
                    index = min(range(len(data['offset'])), key=lambda i: abs(data['offset'][i]-xcoord))
                    index = int(index)
                    center = data['offset'][index]
                    maximum = data['correlation'][index]
                except TypeError:
                    # CCWindow.ui.infobox.append('Unable to refit')
                    for count in range(len(data['correlation'])):
                        if data['correlation'][count] > maximum:
                            maximum = data['correlation'][count]
                            center = data['offset'][count]
                            index = count
            clean = np.linspace(-(value/2), value/2, 10*len(data['offset']))
            # print data['correlation']
            FitX = data['offset'][index-3:index+3]
            FitY = data['correlation'][index-3:index+3]
            try:
                gaussy, gaussx = curve_fit(data['fit'], FitX, FitY, p0=[maximum, center, 5, .05])
                # print 'Fit SUCSSES'
            except (RuntimeError, TypeError):
                maximumfalback = 0
                centerfallback = 0
                indexfallback = 0
                for count in range(len(data['correlation'])):
                    if data['correlation'][count] > maximumfalback:
                        maximumfalback = data['correlation'][count]
                        centerfallback = data['offset'][count]
                        indexfallback = count
                        # print 'Here are the parameters:', maximum falback, centerfallback, indexfallback
                FitXFallback = data['offset'][indexfallback-5:indexfallback+5]
                FitYFallback = data['correlation'][indexfallback-5:indexfallback+5]
                try:
                    gaussy, gaussx = curve_fit(data['fit'], FitXFallback, FitYFallback, p0=[maximumfalback,
                                                                                            centerfallback, 5, 0.05])
                except RuntimeError:
                    print 'Cross Correlation Failed'
                    Plotter.corplot(degree, templatename, objectname, order + 1, num, larger, smaller, compare[0],
                                    value, doPlot, not userFit[0])

            tempvelocity = gaussy[1] * data['dispersion']
            print 'centroid:', gaussy[1]
            print 'dispersion:', data['dispersion']
            print 'Converted to Angstrons (tempvelocity):', tempvelocity
            print 'average wavelength:', data['meantemp']
            print 'speed of light:', c
            UseVel = (tempvelocity/data['meantemp'])*c
            print 'Velocity Before Correction:', UseVel
            HelioCorrectedData = AdvancedPlotting.coordconvert(objectname, UseVel)
            print 'Velocity After Correction:', HelioCorrectedData['HCV']
            FullHJD = HelioCorrectedData['HJD']
            FullHCV[order-1] = HelioCorrectedData['HCV']
            FullCC[order-1] = data['correlation']
            FullO[order-1] = data['offset']
            FullGaus[order-1] = gaussy
            centroids[order-1] = gaussy[1]
            FullAmp[order-1] = gaussy[0]
            ccorfig.plot(data['offset'], data['correlation'], label='X-Cor Plot | Relative Velocity: ' + str(UseVel))
            ccorfig.plot(clean, data['fit'](clean, *gaussy),
                         label='Gaussian Fit | x at max: ' + str(gaussy[1]) + '\n Heliocentric Velocity: ' +
                         str(HelioCorrectedData['HCV']))
            ccorfig.set_xlabel('Offset')
            ccorfig.set_ylabel('Correlation Coefficient')
            ccorfig.set_title('Cross Correlation, order number: ' + str(order) + ' for star ' + starname)
            plt.legend(loc='best')
            # This allows one to move between orders in C

            def plotcontrol(event):
                keydown = event.key
                # A advances in the cross correlation, nothing is printed out as of yet, it just produced the plot
                # eventually this whole function if gonna be reorganized to allow for multiple figures to be displayed
                # over
                if keydown == 'a' or keydown == 'A':
                    plt.close()
                    userFit[0] = False
                    Plotter.corplot(degree, templatename, objectname, order + 1, num, larger, smaller, compare[0],
                                    value, doPlot, not userFit[0])
                elif keydown == 'c' or keydown == 'C':
                    plt.close()
                    compare[0] = not compare[0]
                    Plotter.corplot(degree, templatename, objectname, order, num, larger, smaller, compare[0], value,
                                    doPlot, not userFit[0], xcoord=xcoord, ycoord=ycoord, x1bound=x1bound, x2bound=x2bound)
                elif keydown == 'b' or keydown == 'b':
                    plt.close()
                    userFit[0] = False
                    Plotter.corplot(degree, templatename, objectname, order - 1, num, larger, smaller, compare[0],
                                    value, doPlot, not userFit[0])
                elif keydown == 'r' or keydown == 'R':
                    plt.close()
                    xloc, yloc = event.xdata, event.ydata
                    userFit[0] = True
                    Plotter.corplot(degree, templatename, objectname, order, num, larger, smaller, compare[0], value,
                                    doPlot, not userFit[0], xcoord=xloc, ycoord=yloc)
                elif keydown == 'g' or keydown == 'G':
                    if gdata[0] is None:
                        gdata[0] = event.xdata
                    elif gdata[1] is None:
                        gdata[1] = event.xdata
                    else:
                        pass
                    if gdata[0] is not None and gdata[1] is not None:
                        plt.close()
                        xdiff = abs(gdata[1] - gdata[0])
                        bound = xdiff/2
                        bound = int(bound)
                        xloc, yloc = event.xdata, event.ydata
                        Plotter.corplot(degree, templatename, objectname, order, num, larger, smaller, compare[0], value,
                                    doPlot, not userFit[0], xcoord=xcoord, ycoord=ycoord, x1bound=bound, x2bound=bound)
                    else:
                        pass
            # connects to the key press event function
            fig.canvas.mpl_connect('key_press_event', plotcontrol)
            plt.show()
        elif doPlot is False:
            del velocity[:]
            for i in range(numorders[0]):
                data = AdvancedPlotting.ccor(objectname, templatename, degree, i, num, larger, smaller, value)
                index = 0
                center = 0
                maximum = data['correlation'][0]
                for count in range(len(data['correlation'])):
                    if data['correlation'][count] > maximum:
                        maximum = data['correlation'][count]
                        center = data['offset'][count]
                        index = count
                FitX = data['offset'][index-5:index+5]
                FitY = data['correlation'][index-5:index+5]
                try:
                    gaussy,gaussx = curve_fit(data['fit'], FitX, FitY, p0=[maximum, center, 5, .05])
                except(RuntimeError, TypeError):
                    FullGaus[i] = 'UNABLE TO FIT GUASSIAN TO THIS ORDER'
                    FullO[i] = 'UNABLE TO FIT GUASSIAN TO THIS ORDER'
                    FullCC[i] = 'UNBALR TO FIT GUASSIAN TO THIS ORDER'
                    FullHCV[i] = 'UNABLE TO FIT GUASSIAN TO THIS ORDER'
                    FullHJD = 'UNABLE TO FIT GUASSIAN TO THIS ORDER'
                tempvelocity = gaussy[1] * data['dispersion']
                VelocityReal = (tempvelocity/data['meantemp'])*c
                velocity.append(VelocityReal)
                # print 'velocity at order number', i, 'is', VelocityReal
                FullCC[i] = data['correlation']
                FullO[i] = data['offset']
                FullGaus[i] = gaussy
                FullAmp[i] = gaussy[0]
                tempvelocity = gaussy[1] * data['dispersion']
                UseVel = (tempvelocity/data['meantemp'])*c
                HelioCorrectedData = AdvancedPlotting.coordconvert(objectname, UseVel)
                FullHJD = HelioCorrectedData['HJD']
                FullHCV[i] = HelioCorrectedData['HCV']
                centroids[i] = gaussy[1]
            if allplots[0] is False:
                CCWindow.window3 = MultiView()
                CCWindow.window3.show()
            order = 1
        else:
            order = 1
            CCWindow.window3 = MultiView()
            CCWindow.window3.show()

    # The plot controller for the plot that plots (enough plots for you yet?) stacked plots (there we go)
    @staticmethod
    def stackplot(stackfile, allimages, num, start, degree, shouldfit):

        # Initialized the matplotlib figure
        fig = plt.figure(figsize=(25, 10))

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
        # plt.tight_layout()
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
        fig = plt.figure(figsize=(25, 10))
        PlotFunctionality.plot(name, start, showfit[0], shouldfit, degree, fig, 0)
        # plt.tight_layout()
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


class GUIPlotter():

    @staticmethod
    def orbplot(TimeArray, RVArray, ErrorArray, period, foldphase=True, linearT=False, SinT=False):
        residualArray = [None] * len(TimeArray)
        gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
        if linearT is True:
            # def cosine(x, amp, phase, offset):
            #     global OrbitlPeriod
            #     return amp * np.sin((((2*math.pi)*x)/OrbitlPeriod) + phase) + offset
            def othercosine(x, amp, phase, offset, P1):
                global OrbitlPeriod
                return P1*x + amp * np.sin((((2*math.pi)*x)/OrbitlPeriod) + phase) + offset
            diff = max(RVArray) - min(RVArray)
            if foldphase is False:
                meanTime = sum(TimeArray)/len(TimeArray)
                for x in range(len(TimeArray)):
                    TimeArray[x] -= meanTime
            OrbFig = plt.figure(figsize=(10, 10))
            RVplot = OrbFig.add_subplot(gs[0])
            ResidualPlot = OrbFig.add_subplot(gs[1])
            npTimeArray = np.array(TimeArray)
            RVplot.plot(TimeArray, RVArray, 'o')
            npRVArray = np.array(RVArray)
            # siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), float(period), 0, -50])
            # siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), 0, -50])
            siny, covar = curve_fit(othercosine, npTimeArray, npRVArray, p0=[float(diff/2), 0, -50, 0])
            perr = np.sqrt(np.diag(covar))
            if foldphase is False:
                clean = np.linspace(min(npTimeArray)-10, max(npTimeArray)+10, 5000)
            else:
                clean = np.linspace(min(npTimeArray)-1, max(npTimeArray)+1, 5000)
            # RVplot.plot(clean, cosine(clean, *siny), label='RV semiamplitude: ' + str(siny[0]) + '+-' + str(perr[0]))
            RVplot.plot(clean, othercosine(clean, *siny), label='RV semiamplitude: ' + str(siny[0]) + '+-' + str(perr[0]))
            if foldphase is False:
                RVplot.set_xlabel('Period (Days)')
            else:
                RVplot.set_xlabel('Period (Phase)')
            RVplot.set_ylabel('RV (Km*s^-1)')
            for i in range(len(RVArray)):
                # fitValue = cosine(TimeArray[i], *siny)
                fitValue = othercosine(TimeArray[i], *siny)
                residualArray[i] = fitValue - RVArray[i]
            RVplot.errorbar(npTimeArray, npRVArray, yerr=ErrorArray, fmt='o')
            ResidualPlot.plot(TimeArray, residualArray, 's')
            ResidualPlot.errorbar(TimeArray, residualArray, yerr=ErrorArray, fmt='s')
            ResidualPlot.set_title('Residuals')
            if foldphase is False:
                ResidualPlot.set_xlabel('Time (Days)')
            else:
                ResidualPlot.set_xlabel('Time (Phase)')
            ResidualPlot.set_ylabel('Function - Data Point')
            ResidualPlot.axhline(0, color='black', linestyle='--')
            RVplot.set_title('RV vs Phase')
            RVplot.legend(loc="best")
            RVplot.axhline(siny[2], color="grey", linestyle='--')
            plt.show()

            print 'RV semiamplitude:', siny[0], '+-', perr[0]
            print 'System Velocity:', siny[2], '+-', perr[2]
            # return {'Xdata': npTimeArray, 'Ydata': npRVArray, 'function': cosine, 'smooth': clean, 'fit': siny}
            return {'Xdata': npTimeArray, 'Ydata': npRVArray, 'function': othercosine, 'smooth': clean, 'fit': siny}
        elif SinT is True:
            def SinTrendFit(x, amp1, phase1, offset1, LP, amp2, phase2):
                global OrbitlPeriod
                return amp2 * np.sin((((2*math.pi)*x)/LP) + phase2) + amp1 * np.sin((((2*math.pi)*x)/OrbitlPeriod) + phase1) + offset1
            diff = max(RVArray) - min(RVArray)
            if foldphase is False:
                meanTime = sum(TimeArray)/len(TimeArray)
                for x in range(len(TimeArray)):
                    TimeArray[x] -= meanTime
            OrbFig = plt.figure(figsize=(10, 10))
            RVplot = OrbFig.add_subplot(gs[0])
            ResidualPlot = OrbFig.add_subplot(gs[1])
            npTimeArray = np.array(TimeArray)
            RVplot.plot(TimeArray, RVArray, 'o')
            npRVArray = np.array(RVArray)
            # siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), float(period), 0, -50])
            # siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), 0, -50])
            siny, covar = curve_fit(SinTrendFit, npTimeArray, npRVArray, p0=[float(diff/2), 0, -50, 50, 10, 0])
            perr = np.sqrt(np.diag(covar))
            if foldphase is False:
                clean = np.linspace(min(npTimeArray)-10, max(npTimeArray)+10, 5000)
            else:
                clean = np.linspace(min(npTimeArray)-1, max(npTimeArray)+1, 5000)
            # RVplot.plot(clean, cosine(clean, *siny), label='RV semiamplitude: ' + str(siny[0]) + '+-' + str(perr[0]))
            RVplot.plot(clean, SinTrendFit(clean, *siny), label='RV semiamplitude: ' + str(siny[0]) + '+-' + str(perr[0]))
            if foldphase is False:
                RVplot.set_xlabel('Period (Days)')
            else:
                RVplot.set_xlabel('Period (Phase)')
            RVplot.set_ylabel('RV (Km*s^-1)')
            for i in range(len(RVArray)):
                # fitValue = cosine(TimeArray[i], *siny)
                fitValue = SinTrendFit(TimeArray[i], *siny)
                residualArray[i] = fitValue - RVArray[i]
            RVplot.errorbar(npTimeArray, npRVArray, yerr=ErrorArray, fmt='o')
            ResidualPlot.plot(TimeArray, residualArray, 's')
            ResidualPlot.errorbar(TimeArray, residualArray, yerr=ErrorArray, fmt='s')
            ResidualPlot.set_title('Residuals')
            if foldphase is False:
                ResidualPlot.set_xlabel('Time (Days)')
            else:
                ResidualPlot.set_xlabel('Time (Phase)')
            ResidualPlot.set_ylabel('Function - Data Point')
            ResidualPlot.axhline(0, color='black', linestyle='--')
            RVplot.set_title('RV vs Phase')
            RVplot.legend(loc="best")
            RVplot.axhline(siny[2], color="grey", linestyle='--')
            plt.show()

            print 'RV semiamplitude:', siny[0], '+-', perr[0]
            print 'System Velocity:', siny[2], '+-', perr[2]
            # return {'Xdata': npTimeArray, 'Ydata': npRVArray, 'function': cosine, 'smooth': clean, 'fit': siny}
            return {'Xdata': npTimeArray, 'Ydata': npRVArray, 'function': SinTrendFit, 'smooth': clean, 'fit': siny}
        else:
            def cosine(x, amp, phase, offset):
                global OrbitlPeriod
                return amp * np.sin((((2*math.pi)*x)/OrbitlPeriod) + phase) + offset
            diff = max(RVArray) - min(RVArray)
            if foldphase is False:
                meanTime = sum(TimeArray)/len(TimeArray)
                for x in range(len(TimeArray)):
                    TimeArray[x] -= meanTime
            OrbFig = plt.figure(figsize=(10, 10))
            RVplot = OrbFig.add_subplot(gs[0])
            ResidualPlot = OrbFig.add_subplot(gs[1])
            npTimeArray = np.array(TimeArray)
            RVplot.plot(TimeArray, RVArray, 'o')
            npRVArray = np.array(RVArray)
            # siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), float(period), 0, -50])
            # siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), 0, -50])
            siny, covar = curve_fit(cosine, npTimeArray, npRVArray, p0=[float(diff/2), 0, -50])
            perr = np.sqrt(np.diag(covar))
            if foldphase is False:
                clean = np.linspace(min(npTimeArray)-10, max(npTimeArray)+10, 5000)
            else:
                clean = np.linspace(min(npTimeArray)-1, max(npTimeArray)+1, 5000)
            # RVplot.plot(clean, cosine(clean, *siny), label='RV semiamplitude: ' + str(siny[0]) + '+-' + str(perr[0]))
            RVplot.plot(clean, cosine(clean, *siny), label='RV semiamplitude: ' + str(siny[0]) + '+-' + str(perr[0]))
            if foldphase is False:
                RVplot.set_xlabel('Period (Days)')
            else:
                RVplot.set_xlabel('Period (Phase)')
            RVplot.set_ylabel('RV (Km*s^-1)')
            for i in range(len(RVArray)):
                # fitValue = cosine(TimeArray[i], *siny)
                fitValue = cosine(TimeArray[i], *siny)
                residualArray[i] = fitValue - RVArray[i]
            RVplot.errorbar(npTimeArray, npRVArray, yerr=ErrorArray, fmt='o')
            ResidualPlot.plot(TimeArray, residualArray, 's')
            ResidualPlot.errorbar(TimeArray, residualArray, yerr=ErrorArray, fmt='s')
            ResidualPlot.set_title('Residuals')
            if foldphase is False:
                ResidualPlot.set_xlabel('Time (Days)')
            else:
                ResidualPlot.set_xlabel('Time (Phase)')
            ResidualPlot.set_ylabel('Function - Data Point')
            ResidualPlot.axhline(0, color='black', linestyle='--')
            RVplot.set_title('RV vs Phase')
            RVplot.legend(loc="best")
            RVplot.axhline(siny[2], color="grey", linestyle='--')
            plt.show()

            print 'RV semiamplitude:', siny[0], '+-', perr[0]
            print 'System Velocity:', siny[2], '+-', perr[2]
            # return {'Xdata': npTimeArray, 'Ydata': npRVArray, 'function': cosine, 'smooth': clean, 'fit': siny}
            return {'Xdata': npTimeArray, 'Ydata': npRVArray, 'function': cosine, 'smooth': clean, 'fit': siny}

    # Corplot function that calls the ccofig function from GUI function to extract the required data
    # incidentaly this will be completely reorganized in the great reorganization of code to come
    # I wrote the comment like a week ago now and I have yet to begin the great reorganization of code
    # as my younger naive self called it, rather it has been a slow logical change in the code base
    # whatever, maybe one day.
    @staticmethod
    def corplot(degree, templatename, objectname, order, num, larger, smaller, show, value, doPlot, autofit, xcoord=None,
                ycoord=None, x1bound=5, x2bound=5):
        global FullHJD
        fitsobject = str(objectname)
        objectfits = fits.open(fitsobject)
        starname = objectfits[0].header['OBJECT']
        templatefits = fits.open(str(templatename))
        namePass[1] = templatefits[0].header['OBJECT']
        namePass[0] = starname
        # Creates a matplotlib figure of given size (will at some point be configuarble in the forcoming settings menu)
        # fig=plt.figure(figsize=(10, 7))
        # Adds the ccorfig subplot
        # ccorfig = fig.add_subplot(1, 1, 1)
        # fetches the data from the ccor function in Advanced Plotting by calling the function, data is returnted as a
        # 2 element dictionary, so then when its plotted below there its is called with the dictionaty nameing
        userFit = [False]
        if doPlot is True and order <= numorders[0]:
            global gcount
            gcount = 0
            global gdata
            gdata = [None, None]
            finished = [False]
            data = AdvancedPlotting.ccor(objectname, templatename, degree, order-1, num, larger, smaller, value)
            fig = plt.figure(figsize=(10, 10))
            if show is False:
                ccorfig = fig.add_subplot(1, 1, 1)
            else:
                ccorfig = fig.add_subplot(2, 1, 1)
                AdvancedPlotting.waveshower(fig, templatename, objectname, order, degree)
            index = 0
            maximum = data['correlation'][0]
            center = 0
            if autofit is True:
                for count in range(len(data['correlation'])):
                    if data['correlation'][count] > maximum:
                        maximum = data['correlation'][count]
                        center = data['offset'][count]
                        index = count
            else:
                try:
                    index = min(range(len(data['offset'])), key=lambda i: abs(data['offset'][i]-xcoord))
                    index = int(index)
                    center = data['offset'][index]
                    maximum = data['correlation'][index]
                except TypeError:
                    # CCWindow.ui.infobox.append('Unable to refit')
                    for count in range(len(data['correlation'])):
                        if data['correlation'][count] > maximum:
                            maximum = data['correlation'][count]
                            center = data['offset'][count]
                            index = count
            clean = np.linspace(-(value/2), value/2, 10*len(data['offset']))
            # print data['correlation']
            FitX = data['offset'][index-3:index+3]
            FitY = data['correlation'][index-3:index+3]
            try:
                gaussy, gaussx = curve_fit(data['fit'], FitX, FitY, p0=[maximum, center, 5, .05])
                # print 'Fit SUCSSES'
            except (RuntimeError, TypeError):
                maximumfalback = 0
                centerfallback = 0
                indexfallback = 0
                for count in range(len(data['correlation'])):
                    if data['correlation'][count] > maximumfalback:
                        maximumfalback = data['correlation'][count]
                        centerfallback = data['offset'][count]
                        indexfallback = count
                        # print 'Here are the parameters:', maximum falback, centerfallback, indexfallback
                FitXFallback = data['offset'][indexfallback-5:indexfallback+5]
                FitYFallback = data['correlation'][indexfallback-5:indexfallback+5]
                try:
                    gaussy, gaussx = curve_fit(data['fit'], FitXFallback, FitYFallback, p0=[maximumfalback,
                                                                                            centerfallback, 5, 0.05])
                except RuntimeError:
                    print 'Cross Correlation Failed'
                    Plotter.corplot(degree, templatename, objectname, order + 1, num, larger, smaller, compare[0],
                                    value, doPlot, not userFit[0])

            tempvelocity = gaussy[1] * data['dispersion']
            print 'centroid:', gaussy[1]
            print 'dispersion:', data['dispersion']
            print 'Converted to Angstrons (tempvelocity):', tempvelocity
            print 'average wavelength:', data['meantemp']
            print 'speed of light:', c
            UseVel = (tempvelocity/data['meantemp'])*c
            print 'Velocity Before Correction:', UseVel
            HelioCorrectedData = AdvancedPlotting.coordconvert(objectname, UseVel)
            print 'Velocity After Correction:', HelioCorrectedData['HCV']
            FullHJD = HelioCorrectedData['HJD']
            FullHCV[order-1] = HelioCorrectedData['HCV']
            FullCC[order-1] = data['correlation']
            FullO[order-1] = data['offset']
            FullGaus[order-1] = gaussy
            centroids[order-1] = gaussy[1]
            FullAmp[order-1] = gaussy[0]
            ccorfig.plot(data['offset'], data['correlation'], label='X-Cor Plot | Relative Velocity: ' + str(UseVel))
            ccorfig.plot(clean, data['fit'](clean, *gaussy),
                         label='Gaussian Fit | x at max: ' + str(gaussy[1]) + '\n Heliocentric Velocity: ' +
                         str(HelioCorrectedData['HCV']))
            ccorfig.set_xlabel('Offset')
            ccorfig.set_ylabel('Correlation Coefficient')
            ccorfig.set_title('Cross Correlation, order number: ' + str(order) + ' for star ' + starname)
            plt.legend(loc='best')
            # This allows one to move between orders in C

            def plotcontrol(event):
                keydown = event.key
                # A advances in the cross correlation, nothing is printed out as of yet, it just produced the plot
                # eventually this whole function if gonna be reorganized to allow for multiple figures to be displayed
                # over
                if keydown == 'a' or keydown == 'A':
                    plt.close()
                    userFit[0] = False
                    Plotter.corplot(degree, templatename, objectname, order + 1, num, larger, smaller, compare[0],
                                    value, doPlot, not userFit[0])
                elif keydown == 'c' or keydown == 'C':
                    plt.close()
                    compare[0] = not compare[0]
                    Plotter.corplot(degree, templatename, objectname, order, num, larger, smaller, compare[0], value,
                                    doPlot, not userFit[0], xcoord=xcoord, ycoord=ycoord, x1bound=x1bound, x2bound=x2bound)
                elif keydown == 'b' or keydown == 'b':
                    plt.close()
                    userFit[0] = False
                    Plotter.corplot(degree, templatename, objectname, order - 1, num, larger, smaller, compare[0],
                                    value, doPlot, not userFit[0])
                elif keydown == 'r' or keydown == 'R':
                    plt.close()
                    xloc, yloc = event.xdata, event.ydata
                    userFit[0] = True
                    Plotter.corplot(degree, templatename, objectname, order, num, larger, smaller, compare[0], value,
                                    doPlot, not userFit[0], xcoord=xloc, ycoord=yloc)
                elif keydown == 'g' or keydown == 'G':
                    if gdata[0] is None:
                        gdata[0] = event.xdata
                    elif gdata[1] is None:
                        gdata[1] = event.xdata
                    else:
                        pass
                    if gdata[0] is not None and gdata[1] is not None:
                        plt.close()
                        xdiff = abs(gdata[1] - gdata[0])
                        bound = xdiff/2
                        bound = int(bound)
                        xloc, yloc = event.xdata, event.ydata
                        Plotter.corplot(degree, templatename, objectname, order, num, larger, smaller, compare[0], value,
                                    doPlot, not userFit[0], xcoord=xcoord, ycoord=ycoord, x1bound=bound, x2bound=bound)
                    else:
                        pass
            # connects to the key press event function
            fig.canvas.mpl_connect('key_press_event', plotcontrol)
            plt.show()
        elif doPlot is False:
            del velocity[:]
            for i in range(numorders[0]):
                data = AdvancedPlotting.ccor(objectname, templatename, degree, i, num, larger, smaller, value)
                index = 0
                center = 0
                maximum = data['correlation'][0]
                for count in range(len(data['correlation'])):
                    if data['correlation'][count] > maximum:
                        maximum = data['correlation'][count]
                        center = data['offset'][count]
                        index = count
                FitX = data['offset'][index-5:index+5]
                FitY = data['correlation'][index-5:index+5]
                try:
                    gaussy,gaussx = curve_fit(data['fit'], FitX, FitY, p0=[maximum, center, 5, .05])
                except(RuntimeError, TypeError):
                    FullGaus[i] = 'UNABLE TO FIT GUASSIAN TO THIS ORDER'
                    FullO[i] = 'UNABLE TO FIT GUASSIAN TO THIS ORDER'
                    FullCC[i] = 'UNBALR TO FIT GUASSIAN TO THIS ORDER'
                    FullHCV[i] = 'UNABLE TO FIT GUASSIAN TO THIS ORDER'
                    FullHJD = 'UNABLE TO FIT GUASSIAN TO THIS ORDER'
                tempvelocity = gaussy[1] * data['dispersion']
                VelocityReal = (tempvelocity/data['meantemp'])*c
                velocity.append(VelocityReal)
                # print 'velocity at order number', i, 'is', VelocityReal
                FullCC[i] = data['correlation']
                FullO[i] = data['offset']
                FullGaus[i] = gaussy
                FullAmp[i] = gaussy[0]
                tempvelocity = gaussy[1] * data['dispersion']
                UseVel = (tempvelocity/data['meantemp'])*c
                HelioCorrectedData = AdvancedPlotting.coordconvert(objectname, UseVel)
                FullHJD = HelioCorrectedData['HJD']
                FullHCV[i] = HelioCorrectedData['HCV']
                centroids[i] = gaussy[1]
            if allplots[0] is False:
                CCWindow.window3 = MultiView()
                CCWindow.window3.show()
            order = 1
        else:
            order = 1
            CCWindow.window3 = MultiView()
            CCWindow.window3.show()

    # The plot controller for the plot that plots (enough plots for you yet?) stacked plots (there we go)
    @staticmethod
    def spectra(path, order, degree, offset):
        data = PlotFunctionality.wfextract(path, order)
        flux = data['flux']
        wavelength = data['wavelength']
        fit = PlotFunctionality.fitfunction(degree, wavelength, flux, offset, False)
        y_poly = fit['y_poly']
        y_new = fit['y_new']

        return {'f': flux, 'w': wavelength, 'yp': y_poly, 'yn': y_new}







if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
