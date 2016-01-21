# This program is intened to make a file with the paths to all of the achi files, so that viewer can use them
import os
# TODO sort by star and not by file name, need to have folders for each star
searchName = 'achi'
pathArray = []
pathList = open('PathList', 'w')
for root, dirs, files in os.walk('.', topdown = True):
    for file in files:
        if searchName in file:
            pathArray.append(os.path.join(root, file))

for i in range(len(pathArray)):
    print >>pathList, pathArray[i]
