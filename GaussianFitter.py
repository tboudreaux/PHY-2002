# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GaussianFitter.ui'
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

class Ui_GaussianFitter(object):
    def setupUi(self, GaussianFitter):
        GaussianFitter.setObjectName(_fromUtf8("GaussianFitter"))
        GaussianFitter.resize(606, 323)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 17, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 17, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 17, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        GaussianFitter.setPalette(palette)
        self.centralwidget = QtGui.QWidget(GaussianFitter)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.HydrogenA = QtGui.QCheckBox(self.centralwidget)
        self.HydrogenA.setGeometry(QtCore.QRect(40, 80, 141, 22))
        self.HydrogenA.setObjectName(_fromUtf8("HydrogenA"))
        self.HydrogenB = QtGui.QCheckBox(self.centralwidget)
        self.HydrogenB.setGeometry(QtCore.QRect(40, 100, 141, 22))
        self.HydrogenB.setObjectName(_fromUtf8("HydrogenB"))
        self.HeliumA = QtGui.QCheckBox(self.centralwidget)
        self.HeliumA.setGeometry(QtCore.QRect(40, 120, 141, 22))
        self.HeliumA.setObjectName(_fromUtf8("HeliumA"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 250, 100, 29))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 191, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.quit = QtGui.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(510, 0, 100, 29))
        self.quit.setObjectName(_fromUtf8("quit"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 80, 281, 29))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 30, 231, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(280, 110, 281, 181))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        GaussianFitter.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GaussianFitter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 606, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        GaussianFitter.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GaussianFitter)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GaussianFitter.setStatusBar(self.statusbar)

        self.retranslateUi(GaussianFitter)
        QtCore.QMetaObject.connectSlotsByName(GaussianFitter)

    def retranslateUi(self, GaussianFitter):
        GaussianFitter.setWindowTitle(_translate("GaussianFitter", "MainWindow", None))
        self.HydrogenA.setText(_translate("GaussianFitter", "Hydrogen Alpha", None))
        self.HydrogenB.setText(_translate("GaussianFitter", "Hydrogen Beta", None))
        self.HeliumA.setText(_translate("GaussianFitter", "Helium I", None))
        self.pushButton.setText(_translate("GaussianFitter", "Fit!", None))
        self.label.setText(_translate("GaussianFitter", "Check the lines you want  \n"
"to fit a gaussian equation to", None))
        self.quit.setText(_translate("GaussianFitter", "Quit", None))
        self.label_2.setText(_translate("GaussianFitter", "Input the file name you \n"
"would like to analyze", None))

