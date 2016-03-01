# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SinglePlotWindow.ui'
#
# Created: Tue Mar  1 14:58:09 2016
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_Ploter(object):
    def setupUi(self, Ploter):
        Ploter.setObjectName(_fromUtf8("Ploter"))
        Ploter.resize(753, 615)
        self.centralWidget = QtGui.QWidget(Ploter)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 751, 521))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Plot = QtGui.QWidget(self.gridLayoutWidget)
        self.Plot.setObjectName(_fromUtf8("Plot"))
        self.gridLayout.addWidget(self.Plot, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 520, 751, 41))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.ToolBar = QtGui.QWidget(self.gridLayoutWidget_2)
        self.ToolBar.setObjectName(_fromUtf8("ToolBar"))
        self.gridLayout_2.addWidget(self.ToolBar, 0, 0, 1, 1)
        self.Data = QtGui.QWidget(self.gridLayoutWidget_2)
        self.Data.setObjectName(_fromUtf8("Data"))
        self.gridLayout_2.addWidget(self.Data, 0, 1, 1, 1)
        Ploter.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Ploter)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 753, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuWindow = QtGui.QMenu(self.menuBar)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        Ploter.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(Ploter)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        Ploter.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(Ploter)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        Ploter.setStatusBar(self.statusBar)
        self.actionQuit = QtGui.QAction(Ploter)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSave = QtGui.QAction(Ploter)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionNo_Help_Here = QtGui.QAction(Ploter)
        self.actionNo_Help_Here.setObjectName(_fromUtf8("actionNo_Help_Here"))
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionSave)
        self.menuHelp.addAction(self.actionNo_Help_Here)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuWindow.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Ploter)
        QtCore.QMetaObject.connectSlotsByName(Ploter)

    def retranslateUi(self, Ploter):
        Ploter.setWindowTitle(_translate("Ploter", "Ploter", None))
        self.menuFile.setTitle(_translate("Ploter", "File", None))
        self.menuEdit.setTitle(_translate("Ploter", "Edit", None))
        self.menuWindow.setTitle(_translate("Ploter", "Window", None))
        self.menuHelp.setTitle(_translate("Ploter", "Help", None))
        self.actionQuit.setText(_translate("Ploter", "Quit", None))
        self.actionSave.setText(_translate("Ploter", "Save", None))
        self.actionNo_Help_Here.setText(_translate("Ploter", "No Help Here", None))

