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
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(659, 449)
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
        mainWindow.setPalette(palette)
        mainWindow.setToolTip(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 180, 100, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 191, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.quit = QtGui.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(550, 0, 100, 29))
        self.quit.setObjectName(_fromUtf8("quit"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 80, 371, 29))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 30, 231, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(280, 110, 371, 291))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.infobox = QtGui.QTextBrowser(self.centralwidget)
        self.infobox.setGeometry(QtCore.QRect(10, 210, 261, 192))
        self.infobox.setObjectName(_fromUtf8("infobox"))
        self.HydrogenA = QtGui.QRadioButton(self.centralwidget)
        self.HydrogenA.setGeometry(QtCore.QRect(10, 70, 131, 21))
        self.HydrogenA.setObjectName(_fromUtf8("HydrogenA"))
        self.HydrogenB = QtGui.QRadioButton(self.centralwidget)
        self.HydrogenB.setGeometry(QtCore.QRect(10, 90, 121, 21))
        self.HydrogenB.setObjectName(_fromUtf8("HydrogenB"))
        self.HeliumA = QtGui.QRadioButton(self.centralwidget)
        self.HeliumA.setGeometry(QtCore.QRect(10, 110, 97, 21))
        self.HeliumA.setObjectName(_fromUtf8("HeliumA"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 110, 104, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.aurora = QtGui.QRadioButton(self.centralwidget)
        self.aurora.setGeometry(QtCore.QRect(10, 130, 97, 21))
        self.aurora.setObjectName(_fromUtf8("aurora"))
        self.fitall_2 = QtGui.QPushButton(self.centralwidget)
        self.fitall_2.setGeometry(QtCore.QRect(110, 180, 161, 31))
        self.fitall_2.setObjectName(_fromUtf8("fitall_2"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuWindow = QtGui.QMenu(self.menubar)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow", None))
        self.pushButton.setToolTip(_translate("mainWindow", "Fits and plots a single line", None))
        self.pushButton.setText(_translate("mainWindow", "Fit and plot", None))
        self.label.setText(_translate("mainWindow", "Check the lines you want  \n"
"to fit a gaussian equation to", None))
        self.quit.setText(_translate("mainWindow", "Quit", None))
        self.label_2.setText(_translate("mainWindow", "Input the file name you \n"
"would like to analyze", None))
        self.HydrogenA.setToolTip(_translate("mainWindow", "Fits the Hydrogen Alpha line", None))
        self.HydrogenA.setText(_translate("mainWindow", "Hydrogen Alpha", None))
        self.HydrogenB.setToolTip(_translate("mainWindow", "Fits the Hydrogen Beta line", None))
        self.HydrogenB.setText(_translate("mainWindow", "Hydrogen Beta", None))
        self.HeliumA.setToolTip(_translate("mainWindow", "Fits Helium line", None))
        self.HeliumA.setText(_translate("mainWindow", "Helium I", None))
        self.comboBox.setToolTip(_translate("mainWindow", "Choose Helium line", None))
        self.comboBox.setItemText(0, _translate("mainWindow", "5875.621", None))
        self.comboBox.setItemText(1, _translate("mainWindow", "4685.9179", None))
        self.comboBox.setItemText(2, _translate("mainWindow", "4921.931", None))
        self.comboBox.setItemText(3, _translate("mainWindow", "5015.6779", None))
        self.comboBox.setItemText(4, _translate("mainWindow", "Fit all (will not return plot)", None))
        self.aurora.setToolTip(_translate("mainWindow", "Checks the Aurora line", None))
        self.aurora.setText(_translate("mainWindow", "Aurora", None))
        self.fitall_2.setToolTip(_translate("mainWindow", "Fits all lines and returns an averaged velocity", None))
        self.fitall_2.setText(_translate("mainWindow", "Fit all", None))
        self.menuFile.setTitle(_translate("mainWindow", "File", None))
        self.menuEdit.setTitle(_translate("mainWindow", "Edit", None))
        self.menuWindow.setTitle(_translate("mainWindow", "Window", None))

