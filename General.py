import platform
import matplotlib as mpl
import imp
import math
import numpy as np


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

    @staticmethod
    def mag3D(vector):
        mag = math.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)
        return mag

    @staticmethod
    def median(listi):
        return np.median(np.array(listi))

    @staticmethod
    def stdev(array):
        total = 0
        mean = sum(array)/len(array)
        for i in range(len(array)):
            diff = array[i] - mean
            diff *= diff
            total += diff
        total /= (len(array)-1)
        return math.sqrt(total)
