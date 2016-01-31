# This program controls the functions avalible to the user in the consol
from PyQt4 import QtCore, QtGui
import os, sys, stat
from subprocess import Popen, PIPE


class BSPS(object):

    @staticmethod
    def route(command, paramter):
        commandList = {'view':BSPSEss.view, 'ls':BSPSEss.ls, 'lcom':BSPSEss.lcom, 'pwd':BSPSEss.pwd, 'cd':BSPSEss.cd, 'clear':BSPSEss.clear, 'mkdir': BSPSEss.mkdir, 'edit': BSPSEss.edit, 'pyrun': BSPSEss.pyrun, 'tie': BSPSEss.tie, 'lfunc': BSPSEss.lfunc, 'reload': BSPSEss.reload, 'quit':BSPSEss.quit}
        if command in commandList:
            string = BSPSEss.strsend(command, paramter)
            return string

class Communicate(QtCore.QObject):
        returnsig = QtCore.pyqtSignal()

class BSPSEss(BSPS):

    def __init__(self):
        self.com = Communicate()

    @staticmethod
    def strsend(command, parameter):
        commandlist = {'view':BSPSEss.view, 'ls':BSPSEss.ls, 'lcom':BSPSEss.lcom, 'pwd':BSPSEss.pwd, 'cd':BSPSEss.cd, 'clear':BSPSEss.clear, 'mkdir': BSPSEss.mkdir, 'edit': BSPSEss.edit, 'pyrun':BSPSEss.pyrun, 'tie': BSPSEss.tie, 'lfunc': BSPSEss.lfunc, 'reload': BSPSEss.reload, 'quit': BSPSEss.quit}
        try:
            string = commandlist[command](parameter)
        except TypeError:
            string = commandlist[command]()
        BSPSEss.stremit(BSPSEss())
        return string

    @staticmethod
    def reload():
        python = sys.executable
        os.execl(python, python, * sys.argv)

    @staticmethod
    def quit():
        exit()

    @staticmethod
    def lfunc(parameter):
        parameter.append('Null')
        if parameter[0] == '-a':
            return '//lfuncall'
        else:
            return '//lfunc'

    @staticmethod
    def pyrun(parameter):
        if isinstance(parameter, list):
            prosses = Popen(["python", parameter[0]], stdout=PIPE, stderr=PIPE)
        else:
            prosses = Popen(["python", parameter], stdout=PIPE, stderr=PIPE)
        stdout, stderr = prosses.communicate()
        if len(stdout) > 0:
            stdout = '<font color = "purple">' + str(stdout) + '</font>'
        if len(stderr) > 0:
            stderr = '<font color = "orange">' + str(stderr) + '</font>'
        return stdout + stderr

    @staticmethod
    def tie(parameter):
        return '//tie'

    @staticmethod
    def edit():
        return '//edit'

    @staticmethod
    def mkdir(parameter):
        os.mkdir(parameter[0])

    @staticmethod
    def clear():
        return '//clear'

    @staticmethod
    def cd(parameter):
        try:
            os.chdir(parameter[0])
        except OSError:
            string = '<font color = "red">No such directory</font>'
            return string

    @staticmethod
    def ls():
        dirs = os.listdir('.')
        if len(dirs) != 0:
            string = ', '.join(dirs)
        else:
            string = '<font color = "red">Nothing Here</font>'
        return string

    @staticmethod
    def lcom():
        commands = open('CL.list','rb')
        commands = commands.read()
        return commands

    @staticmethod
    def pwd():
        directory = os.getcwd()
        return directory

    @staticmethod
    def view(filename):
        openfile = open(filename[0], 'rb')
        openfile = openfile.read()
        return openfile

    def stremit(self):
        self.com.returnsig.emit()

