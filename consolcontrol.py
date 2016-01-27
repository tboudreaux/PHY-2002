# This program controls the functions avalible to the user in the consol
from BPlot import MyForm
from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot
class BSPS(object):

    @staticmethod
    def route(command, paramter):
        commandlist = open('CL.list', 'rb')
        commandlist = commandlist.read()
        commandlist = str.split(commandlist)
        if command in commandlist:
            if command == 'view':
                BSPSEss.view(BSPSEss())

class BSPSEss(QObject):

    returnsig = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

    def view(self, filename):
        openfile = open(filename, 'rb')
        openfile = openfile.read()
        self.returnsig.em


