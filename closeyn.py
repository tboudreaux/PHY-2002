# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'closeyn.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 100)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.No = QtGui.QPushButton(Dialog)
        self.No.setObjectName(_fromUtf8("No"))
        self.gridLayout.addWidget(self.No, 1, 0, 1, 1)
        self.Yes = QtGui.QPushButton(Dialog)
        self.Yes.setObjectName(_fromUtf8("Yes"))
        self.gridLayout.addWidget(self.Yes, 1, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.No.setText(_translate("Dialog", "No", None))
        self.Yes.setText(_translate("Dialog", "Yes", None))
        self.label.setText(_translate("Dialog", "Close Without Saving?", None))

