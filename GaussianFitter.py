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
        GaussianFitter.resize(659, 449)
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
        GaussianFitter.setToolTip(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(GaussianFitter)
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
        self.fitall_2 = QtGui.QPushButton(self.centralwidget)
        self.fitall_2.setGeometry(QtCore.QRect(110, 180, 161, 31))
        self.fitall_2.setObjectName(_fromUtf8("fitall_2"))
        self.HydrogenA = QtGui.QCheckBox(self.centralwidget)
        self.HydrogenA.setGeometry(QtCore.QRect(10, 70, 141, 18))
        self.HydrogenA.setObjectName(_fromUtf8("HydrogenA"))
        self.HydrogenB = QtGui.QCheckBox(self.centralwidget)
        self.HydrogenB.setGeometry(QtCore.QRect(10, 90, 111, 18))
        self.HydrogenB.setObjectName(_fromUtf8("HydrogenB"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 110, 85, 18))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.He5975 = QtGui.QCheckBox(self.centralwidget)
        self.He5975.setGeometry(QtCore.QRect(150, 70, 91, 20))
        self.He5975.setObjectName(_fromUtf8("He5975"))
        self.He4885 = QtGui.QCheckBox(self.centralwidget)
        self.He4885.setGeometry(QtCore.QRect(150, 90, 91, 18))
        self.He4885.setObjectName(_fromUtf8("He4885"))
        self.He4921 = QtGui.QCheckBox(self.centralwidget)
        self.He4921.setGeometry(QtCore.QRect(150, 110, 91, 18))
        self.He4921.setObjectName(_fromUtf8("He4921"))
        self.He5015 = QtGui.QCheckBox(self.centralwidget)
        self.He5015.setGeometry(QtCore.QRect(150, 130, 91, 18))
        self.He5015.setObjectName(_fromUtf8("He5015"))
        GaussianFitter.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GaussianFitter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuWindow = QtGui.QMenu(self.menubar)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        GaussianFitter.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GaussianFitter)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GaussianFitter.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())

        self.retranslateUi(GaussianFitter)
        QtCore.QMetaObject.connectSlotsByName(GaussianFitter)

    def retranslateUi(self, GaussianFitter):
        GaussianFitter.setWindowTitle(_translate("GaussianFitter", "MainWindow", None))
        self.pushButton.setToolTip(_translate("GaussianFitter", "Fits and plots a single line", None))
        self.pushButton.setText(_translate("GaussianFitter", "Fit and plot", None))
        self.label.setText(_translate("GaussianFitter", "Check the lines you want  \n"
"to fit a gaussian equation to", None))
        self.quit.setText(_translate("GaussianFitter", "Quit", None))
        self.label_2.setText(_translate("GaussianFitter", "Input the file name you \n"
"would like to analyze", None))
        self.fitall_2.setToolTip(_translate("GaussianFitter", "Fits all lines and returns an averaged velocity", None))
        self.fitall_2.setText(_translate("GaussianFitter", "Fit all", None))
        self.HydrogenA.setText(_translate("GaussianFitter", "Hydrogen Alpha", None))
        self.HydrogenB.setText(_translate("GaussianFitter", "Hydrogen Beta ", None))
        self.checkBox.setText(_translate("GaussianFitter", "Aurora", None))
        self.He5975.setText(_translate("GaussianFitter", "He 5875.62", None))
        self.He4885.setText(_translate("GaussianFitter", "He 4685.92", None))
        self.He4921.setText(_translate("GaussianFitter", "He 4921.93", None))
        self.He5015.setText(_translate("GaussianFitter", "He 5015.68", None))
        self.menuFile.setTitle(_translate("GaussianFitter", "File", None))
        self.menuEdit.setTitle(_translate("GaussianFitter", "Edit", None))
        self.menuWindow.setTitle(_translate("GaussianFitter", "Window", None))

