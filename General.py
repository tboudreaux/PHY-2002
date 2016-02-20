import platform
import matplotlib as mpl
import imp


class PreChecks(object):
    @staticmethod
    def oscheck():
        operatings = platform.system()
        print('Checking Operating System')
        if operatings == 'Windows':
            print('Program does not run on Windows machines, please use a UNIX Like system to run program')
            mac = False
            exit()
        elif operatings == 'Darwin':
            mpl.interactive(True)
            mac = True
            print('OS OK')
        else:
            print('OS OK')
            mac = False
        return mac

    @staticmethod
    def modimport():
        print 'Checking Modules'
        foundall = True
        modarray = ['astropy', 'numpy', 'matplotlib', 'sys', 'os', 'PyQt4', 'SecondGui', 'webbrowser', 'GuiFunction', 'BPlot']
        for i in range(len(modarray)):
            try:
                imp.find_module(modarray[i])
                print modarray[i] + ' OK'
            except ImportError:
                print 'Error ' + modarray[i] + ' is not installed'
                foundall = False
        return foundall


class Mathamatics(object):
    @staticmethod
    def smallest(array):
        smallestnum = array[0]
        for i in range(len(array)):
            if array[i] < smallestnum:
                smallestnum = array[i]
        return smallestnum

    @staticmethod
    def largest(array):
        largestnum = array[0]
        for i in range(len(array)):
            if array[i] > largestnum:
                largestnum = array[i]
        return largestnum