# This program is intened to make a file with the paths to all of the achi files, so that viewer can use them
import os
from astropy.io import fits

#This File may become obsolete, know that

# random edit to the file


#Random Shit
class Generate(object):
    def search(self):
        pathArray = []
        nameArray = []
        pathList = open('PathList', 'w')
        for root, dirs, files in os.walk('.', topdown=True):
            for file in files:
                if 'achi' in file:
                    filename = os.path.join(root, file)
                    sp = fits.open(filename)
                    hdu = sp[0].header
                    objName = (hdu['OBJECT'])
                    if objName not in nameArray:
                        nameArray.append(objName)
        printArray = []
        for i in range(len(nameArray)):
            starName = nameArray[i]
            print starName, 'StarName'
            nameforFile = 'PathTo' + starName
            printList = open(nameforFile, 'w')
            for root, dirs, files in os.walk('.', topdown=True):
                for file in files:
                    if 'achi' in file:
                        name = os.path.join(root, file)
                        sp = fits.open(name)
                        hdu = sp[0].header
                        objName1 = (hdu['OBJECT'])
                        if starName in objName1:
                            print >>printList, name



