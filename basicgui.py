# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basigui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Header(object):
    def setupUi(self, Header):
        Header.setObjectName(_fromUtf8("Header"))
        Header.resize(393, 300)
        self.stackIm = QtGui.QCheckBox(Header)
        self.stackIm.setGeometry(QtCore.QRect(20, 30, 111, 22))
        self.stackIm.setObjectName(_fromUtf8("stackIm"))
        self.pathListInput = QtGui.QTextEdit(Header)
        self.pathListInput.setGeometry(QtCore.QRect(40, 70, 341, 21))
        self.pathListInput.setObjectName(_fromUtf8("pathListInput"))
        self.pathListLabel = QtGui.QLabel(Header)
        self.pathListLabel.setGeometry(QtCore.QRect(40, 50, 161, 17))
        self.pathListLabel.setObjectName(_fromUtf8("pathListLabel"))
        self.singleFileLabel = QtGui.QLabel(Header)
        self.singleFileLabel.setGeometry(QtCore.QRect(30, 100, 121, 17))
        self.singleFileLabel.setObjectName(_fromUtf8("singleFileLabel"))
        self.singleFileInput = QtGui.QTextEdit(Header)
        self.singleFileInput.setGeometry(QtCore.QRect(30, 120, 351, 21))
        self.singleFileInput.setObjectName(_fromUtf8("singleFileInput"))
        self.numStack = QtGui.QSpinBox(Header)
        self.numStack.setGeometry(QtCore.QRect(250, 190, 57, 21))
        self.numStack.setMinimum(1)
        self.numStack.setMaximum(62)
        self.numStack.setObjectName(_fromUtf8("numStack"))
        self.allStack = QtGui.QCheckBox(Header)
        self.allStack.setGeometry(QtCore.QRect(230, 150, 141, 22))
        self.allStack.setObjectName(_fromUtf8("allStack"))
        self.label_3 = QtGui.QLabel(Header)
        self.label_3.setGeometry(QtCore.QRect(250, 170, 121, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.generatePathFiles = QtGui.QPushButton(Header)
        self.generatePathFiles.setGeometry(QtCore.QRect(10, 240, 151, 27))
        self.generatePathFiles.setObjectName(_fromUtf8("generatePathFiles"))
        self.quitBut = QtGui.QPushButton(Header)
        self.quitBut.setGeometry(QtCore.QRect(240, 240, 61, 27))
        self.quitBut.setObjectName(_fromUtf8("quitBut"))
        self.plotBut = QtGui.QPushButton(Header)
        self.plotBut.setGeometry(QtCore.QRect(310, 240, 61, 27))
        self.plotBut.setObjectName(_fromUtf8("plotBut"))
        self.startOrd = QtGui.QSpinBox(Header)
        self.startOrd.setGeometry(QtCore.QRect(30, 180, 51, 31))
        self.startOrd.setMinimum(1)
        self.startOrd.setMaximum(62)
        self.startOrd.setObjectName(_fromUtf8("startOrd"))
        self.label_4 = QtGui.QLabel(Header)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 161, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Header)
        QtCore.QMetaObject.connectSlotsByName(Header)

    def retranslateUi(self, Header):
        Header.setWindowTitle(_translate("Header", "Basic Spectral Plotter", None))
        self.stackIm.setText(_translate("Header", "Stack Images", None))
        self.pathListLabel.setText(_translate("Header", "Path List File Name", None))
        self.singleFileLabel.setText(_translate("Header", "Single File Name", None))
        self.allStack.setText(_translate("Header", "Stack All Images", None))
        self.label_3.setText(_translate("Header", "Number To Stack", None))
        self.generatePathFiles.setText(_translate("Header", "Generate Path Files", None))
        self.quitBut.setText(_translate("Header", "Quit", None))
        self.plotBut.setText(_translate("Header", "Plot", None))
        self.label_4.setText(_translate("Header", "Starting Order Number", None))

