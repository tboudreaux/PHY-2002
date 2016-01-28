# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JumpToOrder.ui'
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

class Ui_JumpToOrder(object):
    def setupUi(self, JumpToOrder):
        JumpToOrder.setObjectName(_fromUtf8("JumpToOrder"))
        JumpToOrder.resize(190, 94)
        self.order = QtGui.QSpinBox(JumpToOrder)
        self.order.setGeometry(QtCore.QRect(60, 10, 71, 41))
        self.order.setMinimum(1)
        self.order.setMaximum(62)
        self.order.setObjectName(_fromUtf8("order"))
        self.cancel = QtGui.QPushButton(JumpToOrder)
        self.cancel.setGeometry(QtCore.QRect(0, 60, 91, 31))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.replot = QtGui.QPushButton(JumpToOrder)
        self.replot.setGeometry(QtCore.QRect(100, 60, 91, 31))
        self.replot.setObjectName(_fromUtf8("replot"))

        self.retranslateUi(JumpToOrder)
        QtCore.QMetaObject.connectSlotsByName(JumpToOrder)

    def retranslateUi(self, JumpToOrder):
        JumpToOrder.setWindowTitle(_translate("JumpToOrder", "Jump To Order", None))
        self.cancel.setText(_translate("JumpToOrder", "Close", None))
        self.replot.setText(_translate("JumpToOrder", "Jump To", None))

