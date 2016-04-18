# This program controls the functions avalible to the user in the consol
from PyQt4 import QtCore, QtGui
import os, sys, stat
from subprocess import Popen, PIPE
import random
import matplotlib.pyplot as plt


#  This is the Routing class, it take input from the text input in the form of parssed string and returens a string
# That will be added to the consol by the MyForm Class
class BSPS(object):

    @staticmethod
    def route(command, paramter):
        commandList = {'view': BSPSEss.view, 'ls': BSPSEss.ls, 'lcom': BSPSEss.lcom, 'pwd': BSPSEss.pwd, 'cd': BSPSEss.cd,
                       'clear': BSPSEss.clear, 'mkdir': BSPSEss.mkdir, 'edit': BSPSEss.edit, 'pyrun': BSPSEss.pyrun,
                       'tie': BSPSEss.tie, 'lfunc': BSPSEss.lfunc, 'reload': BSPSEss.reload, 'quit': BSPSEss.quit,
                       'answer': BSPSEss.answer, 'setHET': BSPSEss.setHET, 'setCHIRON': BSPSEss.setCHIRON,
                       'comp': BSPSEss.comp, 'stanPlot': BSPSEss.stanPlot}
        if command in commandList:
            string = BSPSEss.strsend(command, paramter)
            return string


# This does nothing, its litterally never used I just hevent gotten around to deleting it yet, well
# we can dream can't we
class Communicate(QtCore.QObject):
        returnsig = QtCore.pyqtSignal()


# This is more or less the main consol control class, this take in the commands that have been confirmed to be real
# commands by cross referencing to a dictionary and then routes them to the appropriate functions
class BSPSEss(BSPS):

    def __init__(self):
        self.com = Communicate()

    # this is the function inside this class that acually does the routing and sting returning
    @staticmethod
    def strsend(command, parameter):

        # Command list, this at some point would be nice to impliment into a seperate file so that there is only one
        # and that there is not a super long annoying to add to line of code, I think that that may be best to do
        # with the pandas module
        commandlist = {'view': BSPSEss.view, 'ls': BSPSEss.ls, 'lcom': BSPSEss.lcom, 'pwd': BSPSEss.pwd, 'cd': BSPSEss.cd,
                       'clear': BSPSEss.clear, 'mkdir': BSPSEss.mkdir, 'edit': BSPSEss.edit, 'pyrun': BSPSEss.pyrun,
                       'tie': BSPSEss.tie, 'lfunc': BSPSEss.lfunc, 'reload': BSPSEss.reload, 'quit': BSPSEss.quit,
                       'answer': BSPSEss.answer, 'setHET': BSPSEss.setHET, 'setCHIRON': BSPSEss.setCHIRON,
                       'comp': BSPSEss.comp, 'stanPlot': BSPSEss.stanPlot}

        # This basically checks if the function takes a parameter or not, because some like close do not need parameters
        try:
            string = commandlist[command](parameter)
            print string
        except TypeError:
            string = commandlist[command]()

        # Nothing, does not do anything, yup
        BSPSEss.stremit(BSPSEss())

        # Returns the sting
        return string

    @staticmethod
    def stanPlot(parameter):
        print parameter[0]
        if parameter[0] == '-help' or parameter[0] is'?':
            string = 'standard Plot (stanPlot) opens an ascii delimited by whitespace file and plots the first ' \
                     'as x values and the second colum as y values, if there is a third colume it will plot that ' \
                     'as y errors, the syntax is [stanPlot filename xlabel ylabel]'
            return string
        else:
            try:
                datafile = open(parameter[0], 'rb')
                datafile = datafile.readlines()
                for i in range(len(datafile)):
                   datafile[i] = datafile[i].rsplit()
                first = []
                second = []
                third = []
                for element in datafile:
                    first.append(float(element[0]))
                    second.append(float(element[1]))
                    if len(element) is 3:
                        third.append(float(element[2]))
                    else:
                        pass
                plt.plot(first, second, 'o')
                try:
                    plt.xlabel(parameter[1])
                    plt.ylabel(parameter[2])
                except IndexError:
                    try:
                        plt.xlabel('x data')
                        plt.ylabel(parameter[2])
                    except IndexError:
                        try:
                            plt.xlabel(parameter[1])
                            plt.ylabel('y data')
                        except IndexError:
                            plt.xlabel('x data')
                            plt.ylabel('y data')
                if len(third) is not 0:
                    plt.errorbar(first, second, yerr=third, fmt='o')
                else:
                    pass
                plt.show()
                string = '//PDC'
                return string
            except IOError:
                string = '//EIDP'
                return string
    @staticmethod
    def comp(target):
        comfilename = 'CCorFitMetric' + target[0] + '.csv'
        try:
            compfile = open(comfilename, 'rb')
            compfile = compfile.readlines()
            compfile = [x.rsplit() for x in compfile]
            print compfile
            values = [x[2] for x in compfile]
            temps = [x[3] for x in compfile]
            plt.xlabel('Temperature (K)')
            plt.ylabel('Goodness of Fit (No Dimension)')
            plt.title('Spectral Type Analysis for ' + target[0])
            plt.plot(temps, values, 'o')
            string = '//COMP'
        except IOError as e:
            string = '<font color = "red">NO FILE FOUND, PLEASE MAKE SURE YOU HAVE CREATED THE FIT METRIC FILE ' \
                     'BY RUNNING XCOR FOR ALL TELLURIC STANDAD STARS</font><font color = "purple">' + str(e) + '</font>'
        return string

    @staticmethod
    def answer():
        r = random.randrange(1,3)
        if r == 1:
            variable = open('cage1.sec','rb')
            variable = variable.read()
            string = variable
        elif r == 2:
            variable = open('cage2.sec','rb')
            variable = variable.read()
            string = variable
        return string

# Below This are all the functions called by commands
    @staticmethod
    def setCHIRON():
        return '//setCHIRON'

    @staticmethod
    def setHET():
        return '//setHET'

    # relaunches the program from skratch, so code changed can be made while runnign and this command can be run
    # and then they will be implimented
    @staticmethod
    def reload():
        python = sys.executable
        os.execl(python, python, * sys.argv)

    # Closes the program, honestly that should be obvious
    @staticmethod
    def quit():
        exit()

    # This fuction provides infomration about the user functions
    @staticmethod
    def lfunc(parameter):
        # I dont know why I have this here actually
        parameter.append('Null')

        # this is the first instant of // syntax, // sytax is used for hidden commands in this program
        # Where -a is an option
        if parameter[0] == '-a':
            return '//lfuncall'
        else:
            return '//lfunc'

    # runs python programs (also kinda want to add Bash scrpits in here at some point)
    @staticmethod
    def pyrun(parameter):
        # Checks is parameter is a list type data structure of string type, this is down to the fact that I call this
        # from multiple places so I want needs some exception handeling because of different input types
        if isinstance(parameter, list):
            # this uses a subprossess.popen call to run the script and output as a standard UNIX pipe
            prosses = Popen(["python", parameter[0]], stdout=PIPE, stderr=PIPE)
        else:
            prosses = Popen(["python", parameter], stdout=PIPE, stderr=PIPE)
        # sets standard output and error to the array elements from communcation from the prosses
        stdout, stderr = prosses.communicate()

        # if nothing prined to standard error dont worry about it
        if len(stdout) > 0:
            stdout = '<font color = "purple">' + str(stdout) + '</font>'
        # if nothing printed to standard output dont worry about it
        if len(stderr) > 0:
            stderr = '<font color = "orange">' + str(stderr) + '</font>'

        # retuns a string addition of the two
        return stdout + stderr

        # In this function standard input is not yet working, some day, some day

    # calls the tie code, that is in BPlot if any one is interested, I know I am
    @staticmethod
    def tie(parameter):
        return '//tie'

    # Calles the edit code, same thing in BPlot
    @staticmethod
    def edit():
        return '//edit'

    # makes a directory using standard unix command structure, and unix suprosses
    @staticmethod
    def mkdir(parameter):
        os.mkdir(parameter[0])

    # claears the terminal
    @staticmethod
    def clear():
        string = '//clear'
        return string

    # changes directories, with some exception handeling
    @staticmethod
    def cd(parameter):
        # makes sure that the directory exists, this does this with execiton handeling and not a directory walk b/c
        # python exeption handeling is written in C, which executes loops faster than python, and the effect is the
        # same so this should end up running faster
        try:
            os.chdir(parameter[0])
        except OSError:
            string = '<font color = "red">No such directory</font>'
            return string

    # Prints out file structure, just like ls
    @staticmethod
    def ls():
        dirs = os.listdir('.')
        if len(dirs) != 0:
            string = ', '.join(dirs)
        else:
            string = '<font color = "red">Nothing Here</font>'
        return string

    # basically this codes version of help, but because I'm hipster I didn't want to call it help so lcom instead
    @staticmethod
    def lcom():
        # opens an ascii file in the directory and prints it out on screen
        commands = open('CL.list','rb')
        commands = commands.read()
        return commands

    # Print working directory
    @staticmethod
    def pwd():
        directory = os.getcwd()
        return directory

    # this is analogous to cat on unix, but view makes more sense in my head than cat and since im making this I can do
    # whatever I want, I'm crazy and I dont know what I'll do
    @staticmethod
    def view(filename):
        # structure wise this is identical to lcom, infact I will replace lcom with a view call very soon, again low
        # on the priority list, whatever lay off me.
        openfile = open(filename[0], 'rb')
        openfile = openfile.read()
        return openfile

    # nothing, a vesigial organ from a different simplier time
    def stremit(self):
        self.com.returnsig.emit()

