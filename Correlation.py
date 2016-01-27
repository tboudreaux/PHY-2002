# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Correlation.ui'
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

class Ui_CrossCore(object):
    def setupUi(self, CrossCore):
        CrossCore.setObjectName(_fromUtf8("CrossCore"))
        CrossCore.resize(400, 399)
        self.label = QtGui.QLabel(CrossCore)
        self.label.setGeometry(QtCore.QRect(110, 10, 181, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(CrossCore)
        self.line.setGeometry(QtCore.QRect(-10, 20, 441, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.ynlist = QtGui.QCheckBox(CrossCore)
        self.ynlist.setGeometry(QtCore.QRect(10, 40, 96, 22))
        self.ynlist.setObjectName(_fromUtf8("ynlist"))
        self.listpath = QtGui.QTextEdit(CrossCore)
        self.listpath.setGeometry(QtCore.QRect(30, 60, 341, 31))
        self.listpath.setObjectName(_fromUtf8("listpath"))
        self.tempfilename = QtGui.QTextEdit(CrossCore)
        self.tempfilename.setGeometry(QtCore.QRect(30, 120, 341, 31))
        self.tempfilename.setObjectName(_fromUtf8("tempfilename"))
        self.line_2 = QtGui.QFrame(CrossCore)
        self.line_2.setGeometry(QtCore.QRect(-20, 210, 441, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.correlate = QtGui.QPushButton(CrossCore)
        self.correlate.setGeometry(QtCore.QRect(290, 360, 100, 29))
        self.correlate.setObjectName(_fromUtf8("correlate"))
        self.return_2 = QtGui.QPushButton(CrossCore)
        self.return_2.setGeometry(QtCore.QRect(10, 360, 100, 29))
        self.return_2.setObjectName(_fromUtf8("return_2"))
        self.infobox = QtGui.QTextBrowser(CrossCore)
        self.infobox.setGeometry(QtCore.QRect(10, 240, 381, 101))
        self.infobox.setObjectName(_fromUtf8("infobox"))
        self.label_2 = QtGui.QLabel(CrossCore)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 151, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.fitdegree = QtGui.QSpinBox(CrossCore)
        self.fitdegree.setGeometry(QtCore.QRect(210, 360, 71, 31))
        self.fitdegree.setMinimum(1)
        self.fitdegree.setObjectName(_fromUtf8("fitdegree"))
        self.label_3 = QtGui.QLabel(CrossCore)
        self.label_3.setGeometry(QtCore.QRect(140, 350, 71, 51))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.targetfilename = QtGui.QTextEdit(CrossCore)
        self.targetfilename.setGeometry(QtCore.QRect(30, 180, 341, 31))
        self.targetfilename.setObjectName(_fromUtf8("targetfilename"))
        self.label_4 = QtGui.QLabel(CrossCore)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 151, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(CrossCore)
        QtCore.QMetaObject.connectSlotsByName(CrossCore)

    def retranslateUi(self, CrossCore):
        CrossCore.setWindowTitle(_translate("CrossCore", "Cross Correlation", None))
        self.label.setText(_translate("CrossCore", "Cross Correlation Window", None))
        self.ynlist.setText(_translate("CrossCore", "Use List?", None))
        self.correlate.setText(_translate("CrossCore", "Correlate", None))
        self.return_2.setText(_translate("CrossCore", "Return", None))
        self.label_2.setText(_translate("CrossCore", "Path To Template file", None))
        self.label_3.setText(_translate("CrossCore", "Degree->", None))
        self.label_4.setText(_translate("CrossCore", "Path To Target file", None))

