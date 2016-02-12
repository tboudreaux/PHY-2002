# Echel Spectra viewer & analizer
# Paddy Clancy and Thomas Boudreaux
from General import *

import matplotlib.pyplot as plt
import os
from PyQt4 import QtGui, QtCore
from consolcontrol import *
from SecondGui import Ui_Header
import webbrowser
from GuiFunction import *
from astropy.io import fits
import sys
from Correlation2 import Ui_CrossCore
from consolcontrol import *
from JumpToOrder import Ui_JumpToOrder
from Editor import Ui_MainWindow
import time
import random

# Checks os for compatability
PreChecks.oscheck()

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
plotparm = [None] * 10
funcconf = [['1','Null', 'Function1'], ['2', 'Null', 'Function2'], ['3', 'Null', 'Function3'], ['4', 'Null', 'Function4']]
jumpcore = [False]
compare = [False]

# The main GUI Class that controlles the rest og the program
class MyForm(QtGui.QMainWindow):
    #I nitilazation of the GUI
    def __init__(self, parent=None):
        # Ininitlazation of the Widget
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Header()
        self.ui.setupUi(self)
        self.com = Plotter()

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

        # These control most of the button assignments in the main GUI
        self.ui.consol.append('<font color = "green"> SAUL Version 0.5<br>Written by Paddy Clancy and Thomas Boudreaux  - 2016</font><br>')
        self.ui.consol.append('<font color = "blue"> Module and OS Checks OK</font><br>')
        self.ui.consol.append('<font color = "blue"> type "lcom" for a list of avalibel commands</font><br>')
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
        self.ui.function3.clicked.connect(self.LS)
        self.ui.function4.clicked.connect(self.NI)
        self.ui.info.clicked.connect(self.info)
        self.ui.Reset.clicked.connect(self.NI)

        # These initialize the other windows as empty objects in the Main GUI controller
        self.window2 = None
        self.window3 = None
        self.window3 = None

    ###########################
    ##  GUI tie in functions ##
    ###########################

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
                print funcconf
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
        plotparm[0] = degree
        try:
            if usearray[0] is True:
                pathfilename = self.ui.pathListInput.toPlainText()
                numToStack = self.ui.numStack.value()
                plotparm[1] = pathfilename; plotparm[2] = numToStack
            else:
               filename = self.ui.singleFileInput.toPlainText()
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
        if jumpcore[0] is False:
            if usearray[0] is True:
                plt.close()
                Plotter.stackplot(plotparm[1], usearray[1], plotparm[2], order, plotparm[0], fit[0])
            else:
                plt.close()
                Plotter.nstackplot(plotparm[3], order, plotparm[0], fit[0])
        else:
            plt.close()
            Plotter.corplot(plotparm[4], plotparm[5], plotparm[6], order, plotparm[7], plotparm[8], plotparm[9], compare[0])


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
        with open(self.ui.FileName.text(), 'wt') as file:
            file.write(self.ui.textEdit.toPlainText())


# this is the cross correlation GUI
class CCWindow(QtGui.QMainWindow):
    def __init__ (self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_CrossCore()
        self.ui.setupUi(self)

        self.smallerwaves = []
        self.largerwaves = []
        self.ranges = []

        try:
            self.profiles = {'CHIRON':'chiron.pconf'}
            profile1 =  open(self.profiles['CHIRON'], 'rb')
            self.ui.SystemProfiles.addItem('CHIRON')
            profile1 = profile1.readlines()
            self.length = len(profile1)
            self.window2 = None

            for i in range(self.length):
                profile1[i] = profile1[i].split('-')
                profile1[i][1] = profile1[i][1][:-1]
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
            templatename = self.ui.tempfilename.toPlainText()
            objectname = self.ui.targetfilename.toPlainText()

            try:
                Plotter.corplot(degree, templatename, objectname, 1, self.length, self.smallerwaves, self.largerwaves, compare[0])
                self.ui.infobox.append('<font color ="green">Cross Correlating Orders, use "a" to advance</font><br>')
                self.jumpTo()
            except ValueError:
                self.ui.infobox.append('<font color ="red">Please Make sure that file names are entered in the boxs</font>')
            except IOError:
                self.ui.infobox.append('<font color ="red">Please Make sure that file names are spelled correctly</font>')
            plotparm[4] = degree; plotparm[5] = templatename; plotparm[6] = objectname; plotparm[7] = self.length
            plotparm[8] = self.smallerwaves; plotparm[9] = self.largerwaves
            jumpcore[0] = True


# This is plotter code, at some point it may be nice to move this class (During the great reorginazation of code to come)

class Plotter():

    # Corplot function that calls the ccofig function from GUI function to extract the required data
    # incidentaly this will be completely reorganized in the great reorganization of code to come
    # I wrote the comment like a week ago now and I have yet to begin the great reorganization of code
    # as my younger naive self called it, rather it has been a slow logical change in the code base
    # whatever, maybe one day.
    @staticmethod
    def corplot(degree, templatename, objectname, order, num, larger, smaller, show):
        # Creates a matplotlib figure of given size (will at some point be configuarble in the forcoming settings menu)
        # fig=plt.figure(figsize=(10, 7))
        # Adds the ccorfig subplot
        # ccorfig = fig.add_subplot(1, 1, 1)
        # fetches the data from the ccor function in Advanced Plotting by calling the function, data is returnted as a
        #   2 element dictionary, so then when its plotted below there its is called with the dictionaty nameing
        data = AdvancedPlotting.ccor(objectname, templatename, degree, order, num, larger, smaller)
        fig = plt.figure(figsize=(10, 10))
        if show is False:
            ccorfig = fig.add_subplot(1, 1, 1)
        else:
            ccorfig = fig.add_subplot(2,1,1)
            AdvancedPlotting.waveshower(fig, templatename, objectname, order, degree)

        ccorfig.plot(data['offset'], data['correlation'])

        ccorfig.set_xlabel('Offset')
        ccorfig.set_ylabel('Correlation Coefficient')
        ccorfig.set_title('Cross Correlation, order number: ' + str(order))
        location = order
        # This allows one to move between orders in C
        def plotcontrol(event):
            keydown = event.key
            # A advances in the cross correlation, nothing is printed out as of yet, it just produced the plot
            # eventually this whole function if gonna be reorganized to allow for multiple figures to be displayed over
            if keydown == 'a' or keydown == 'A' and order < 62:
                plt.close()
                Plotter.corplot(degree, templatename, objectname, order + 1, num, larger, smaller, compare[0])
            elif keydown == 'c' or keydown == 'C':
                plt.close()
                compare[0] = not compare[0]
                Plotter.corplot(degree, templatename, objectname, order, num, larger, smaller, compare[0])
            elif keydown == 'r' or keydown == 'R':
                for i in range(62-order):
                    plt.close()
                    Plotter.corplot(degree, templatename, objectname, order+i, num, larger, smaller, compare[0])
                    plt.pause(0.25)
        # connects to the key press event function
        fig.canvas.mpl_connect('key_press_event', plotcontrol)
        plt.show()


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

        # This applies an offset to stacked / Nomralized orders to that the velocity offset can be more clearly seen
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
        fig.canvas.mpl_connect('key_press_event', plotcontrol)


# Bascically the most important section of code in the whole code because it makes everything start, its also the
# only section of code in this entire program I don't really understand (I got this section from a tutorial)
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
