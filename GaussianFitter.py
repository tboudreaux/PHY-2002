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

class Ui_GuassianFitter(object):
    def setupUi(self, aurora):
        aurora.setObjectName(_fromUtf8("aurora"))
        aurora.resize(659, 449)
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
        aurora.setPalette(palette)
        aurora.setToolTip(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(aurora)
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
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 110, 104, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.fitall_2 = QtGui.QPushButton(self.centralwidget)
        self.fitall_2.setGeometry(QtCore.QRect(110, 180, 161, 31))
        self.fitall_2.setObjectName(_fromUtf8("fitall_2"))
        self.HydrogenA = QtGui.QCheckBox(self.centralwidget)
        self.HydrogenA.setGeometry(QtCore.QRect(10, 70, 141, 18))
        self.HydrogenA.setObjectName(_fromUtf8("HydrogenA"))
        self.HydrogenB = QtGui.QCheckBox(self.centralwidget)
        self.HydrogenB.setGeometry(QtCore.QRect(10, 90, 111, 18))
        self.HydrogenB.setObjectName(_fromUtf8("HydrogenB"))
        self.HeliumA = QtGui.QCheckBox(self.centralwidget)
        self.HeliumA.setGeometry(QtCore.QRect(10, 110, 85, 18))
        self.HeliumA.setObjectName(_fromUtf8("HeliumA"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 130, 85, 18))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        aurora.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(aurora)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuWindow = QtGui.QMenu(self.menubar)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        aurora.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(aurora)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        aurora.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())

        self.retranslateUi(aurora)
        QtCore.QMetaObject.connectSlotsByName(aurora)

    def retranslateUi(self, aurora):
        aurora.setWindowTitle(_translate("aurora", "MainWindow", None))
        self.pushButton.setToolTip(_translate("aurora", "Fits and plots a single line", None))
        self.pushButton.setText(_translate("aurora", "Fit and plot", None))
        self.label.setText(_translate("aurora", "Check the lines you want  \n"
"to fit a gaussian equation to", None))
        self.quit.setText(_translate("aurora", "Quit", None))
        self.label_2.setText(_translate("aurora", "Input the file name you \n"
"would like to analyze", None))
        self.comboBox.setToolTip(_translate("aurora", "Choose Helium line", None))
        self.comboBox.setItemText(0, _translate("aurora", "5875.621", None))
        self.comboBox.setItemText(1, _translate("aurora", "4685.9179", None))
        self.comboBox.setItemText(2, _translate("aurora", "4921.931", None))
        self.comboBox.setItemText(3, _translate("aurora", "5015.6779", None))
        self.comboBox.setItemText(4, _translate("aurora", "Fit all (will not return plot)", None))
        self.fitall_2.setToolTip(_translate("aurora", "Fits all lines and returns an averaged velocity", None))
        self.fitall_2.setText(_translate("aurora", "Fit all", None))
        self.HydrogenA.setText(_translate("aurora", "Hydrogen Alpha", None))
        self.HydrogenB.setText(_translate("aurora", "Hydrogen Beta ", None))
        self.HeliumA.setText(_translate("aurora", "Helium I", None))
        self.checkBox.setText(_translate("aurora", "Aurora", None))
        self.menuFile.setTitle(_translate("aurora", "File", None))
        self.menuEdit.setTitle(_translate("aurora", "Edit", None))
        self.menuWindow.setTitle(_translate("aurora", "Window", None))

