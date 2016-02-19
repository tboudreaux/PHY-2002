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
        JumpToOrder.resize(291, 152)
        self.gridLayout = QtGui.QGridLayout(JumpToOrder)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget = QtGui.QWidget(JumpToOrder)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.order = QtGui.QSpinBox(self.widget)
        self.order.setMinimum(1)
        self.order.setMaximum(62)
        self.order.setObjectName(_fromUtf8("order"))
        self.gridLayout_2.addWidget(self.order, 0, 0, 1, 2)
        self.replot = QtGui.QPushButton(self.widget)
        self.replot.setObjectName(_fromUtf8("replot"))
        self.gridLayout_2.addWidget(self.replot, 1, 0, 1, 1)
        self.cancel = QtGui.QPushButton(self.widget)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.gridLayout_2.addWidget(self.cancel, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(JumpToOrder)
        QtCore.QMetaObject.connectSlotsByName(JumpToOrder)

    def retranslateUi(self, JumpToOrder):
        JumpToOrder.setWindowTitle(_translate("JumpToOrder", "Jump To Order", None))
        self.replot.setText(_translate("JumpToOrder", "Jump To", None))
        self.cancel.setText(_translate("JumpToOrder", "Close", None))

