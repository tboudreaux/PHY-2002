# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MultiplotViewer.ui'
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

class Ui_MultiplotViewer(object):
    def setupUi(self, MultiplotViewer):
        MultiplotViewer.setObjectName(_fromUtf8("MultiplotViewer"))
        MultiplotViewer.resize(1155, 970)
        self.centralWidget = QtGui.QWidget(MultiplotViewer)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.Tabs = QtGui.QTabWidget(self.centralWidget)
        self.Tabs.setGeometry(QtCore.QRect(0, 0, 1141, 851))
        self.Tabs.setObjectName(_fromUtf8("Tabs"))
        self.firstTab = QtGui.QWidget()
        self.firstTab.setEnabled(True)
        self.firstTab.setObjectName(_fromUtf8("firstTab"))
        self.widget = QtGui.QWidget(self.firstTab)
        self.widget.setGeometry(QtCore.QRect(20, 20, 281, 250))
        self.widget.setMouseTracking(False)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget_2 = QtGui.QWidget(self.firstTab)
        self.widget_2.setGeometry(QtCore.QRect(20, 290, 281, 250))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.widget_3 = QtGui.QWidget(self.firstTab)
        self.widget_3.setGeometry(QtCore.QRect(20, 560, 281, 250))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.widget_4 = QtGui.QWidget(self.firstTab)
        self.widget_4.setGeometry(QtCore.QRect(430, 20, 281, 250))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.widget_5 = QtGui.QWidget(self.firstTab)
        self.widget_5.setGeometry(QtCore.QRect(430, 290, 281, 250))
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.widget_6 = QtGui.QWidget(self.firstTab)
        self.widget_6.setGeometry(QtCore.QRect(430, 560, 281, 250))
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.widget_7 = QtGui.QWidget(self.firstTab)
        self.widget_7.setGeometry(QtCore.QRect(800, 20, 281, 250))
        self.widget_7.setObjectName(_fromUtf8("widget_7"))
        self.widget_8 = QtGui.QWidget(self.firstTab)
        self.widget_8.setGeometry(QtCore.QRect(800, 290, 281, 250))
        self.widget_8.setObjectName(_fromUtf8("widget_8"))
        self.widget_9 = QtGui.QWidget(self.firstTab)
        self.widget_9.setGeometry(QtCore.QRect(800, 560, 281, 250))
        self.widget_9.setObjectName(_fromUtf8("widget_9"))
        self.line = QtGui.QFrame(self.firstTab)
        self.line.setGeometry(QtCore.QRect(360, 0, 20, 821))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.firstTab)
        self.line_2.setGeometry(QtCore.QRect(750, -10, 20, 831))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.Use_1 = QtGui.QCheckBox(self.firstTab)
        self.Use_1.setGeometry(QtCore.QRect(330, 120, 16, 20))
        self.Use_1.setText(_fromUtf8(""))
        self.Use_1.setChecked(True)
        self.Use_1.setObjectName(_fromUtf8("Use_1"))
        self.Use_2 = QtGui.QCheckBox(self.firstTab)
        self.Use_2.setGeometry(QtCore.QRect(330, 400, 16, 20))
        self.Use_2.setText(_fromUtf8(""))
        self.Use_2.setChecked(True)
        self.Use_2.setObjectName(_fromUtf8("Use_2"))
        self.Use_3 = QtGui.QCheckBox(self.firstTab)
        self.Use_3.setGeometry(QtCore.QRect(330, 670, 16, 20))
        self.Use_3.setText(_fromUtf8(""))
        self.Use_3.setChecked(True)
        self.Use_3.setObjectName(_fromUtf8("Use_3"))
        self.Use_4 = QtGui.QCheckBox(self.firstTab)
        self.Use_4.setGeometry(QtCore.QRect(730, 120, 16, 20))
        self.Use_4.setText(_fromUtf8(""))
        self.Use_4.setChecked(True)
        self.Use_4.setObjectName(_fromUtf8("Use_4"))
        self.Use_5 = QtGui.QCheckBox(self.firstTab)
        self.Use_5.setGeometry(QtCore.QRect(730, 400, 16, 20))
        self.Use_5.setText(_fromUtf8(""))
        self.Use_5.setChecked(True)
        self.Use_5.setObjectName(_fromUtf8("Use_5"))
        self.Use_6 = QtGui.QCheckBox(self.firstTab)
        self.Use_6.setGeometry(QtCore.QRect(730, 670, 16, 20))
        self.Use_6.setText(_fromUtf8(""))
        self.Use_6.setChecked(True)
        self.Use_6.setObjectName(_fromUtf8("Use_6"))
        self.Use_9 = QtGui.QCheckBox(self.firstTab)
        self.Use_9.setGeometry(QtCore.QRect(1100, 670, 16, 20))
        self.Use_9.setText(_fromUtf8(""))
        self.Use_9.setChecked(True)
        self.Use_9.setObjectName(_fromUtf8("Use_9"))
        self.Use_8 = QtGui.QCheckBox(self.firstTab)
        self.Use_8.setGeometry(QtCore.QRect(1100, 400, 16, 20))
        self.Use_8.setText(_fromUtf8(""))
        self.Use_8.setChecked(True)
        self.Use_8.setObjectName(_fromUtf8("Use_8"))
        self.Use_7 = QtGui.QCheckBox(self.firstTab)
        self.Use_7.setGeometry(QtCore.QRect(1100, 120, 16, 20))
        self.Use_7.setText(_fromUtf8(""))
        self.Use_7.setChecked(True)
        self.Use_7.setObjectName(_fromUtf8("Use_7"))
        self.Tabs.addTab(self.firstTab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.Use_10 = QtGui.QCheckBox(self.tab_3)
        self.Use_10.setGeometry(QtCore.QRect(330, 120, 16, 20))
        self.Use_10.setText(_fromUtf8(""))
        self.Use_10.setChecked(True)
        self.Use_10.setObjectName(_fromUtf8("Use_10"))
        self.Use_11 = QtGui.QCheckBox(self.tab_3)
        self.Use_11.setGeometry(QtCore.QRect(330, 400, 16, 20))
        self.Use_11.setText(_fromUtf8(""))
        self.Use_11.setChecked(True)
        self.Use_11.setObjectName(_fromUtf8("Use_11"))
        self.Use_12 = QtGui.QCheckBox(self.tab_3)
        self.Use_12.setGeometry(QtCore.QRect(330, 670, 16, 20))
        self.Use_12.setText(_fromUtf8(""))
        self.Use_12.setChecked(True)
        self.Use_12.setObjectName(_fromUtf8("Use_12"))
        self.widget_14 = QtGui.QWidget(self.tab_3)
        self.widget_14.setGeometry(QtCore.QRect(430, 290, 281, 250))
        self.widget_14.setObjectName(_fromUtf8("widget_14"))
        self.line_3 = QtGui.QFrame(self.tab_3)
        self.line_3.setGeometry(QtCore.QRect(360, 0, 20, 821))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.Use_13 = QtGui.QCheckBox(self.tab_3)
        self.Use_13.setGeometry(QtCore.QRect(730, 120, 16, 20))
        self.Use_13.setText(_fromUtf8(""))
        self.Use_13.setChecked(True)
        self.Use_13.setObjectName(_fromUtf8("Use_13"))
        self.Use_14 = QtGui.QCheckBox(self.tab_3)
        self.Use_14.setGeometry(QtCore.QRect(730, 400, 16, 20))
        self.Use_14.setText(_fromUtf8(""))
        self.Use_14.setChecked(True)
        self.Use_14.setObjectName(_fromUtf8("Use_14"))
        self.Use_15 = QtGui.QCheckBox(self.tab_3)
        self.Use_15.setGeometry(QtCore.QRect(730, 670, 16, 20))
        self.Use_15.setText(_fromUtf8(""))
        self.Use_15.setChecked(True)
        self.Use_15.setObjectName(_fromUtf8("Use_15"))
        self.widget_11 = QtGui.QWidget(self.tab_3)
        self.widget_11.setGeometry(QtCore.QRect(20, 290, 281, 250))
        self.widget_11.setObjectName(_fromUtf8("widget_11"))
        self.widget_13 = QtGui.QWidget(self.tab_3)
        self.widget_13.setGeometry(QtCore.QRect(430, 20, 281, 250))
        self.widget_13.setObjectName(_fromUtf8("widget_13"))
        self.widget_17 = QtGui.QWidget(self.tab_3)
        self.widget_17.setGeometry(QtCore.QRect(800, 290, 281, 250))
        self.widget_17.setObjectName(_fromUtf8("widget_17"))
        self.widget_18 = QtGui.QWidget(self.tab_3)
        self.widget_18.setGeometry(QtCore.QRect(800, 560, 281, 250))
        self.widget_18.setObjectName(_fromUtf8("widget_18"))
        self.widget_12 = QtGui.QWidget(self.tab_3)
        self.widget_12.setGeometry(QtCore.QRect(20, 560, 281, 250))
        self.widget_12.setObjectName(_fromUtf8("widget_12"))
        self.widget_15 = QtGui.QWidget(self.tab_3)
        self.widget_15.setGeometry(QtCore.QRect(430, 560, 281, 250))
        self.widget_15.setObjectName(_fromUtf8("widget_15"))
        self.line_4 = QtGui.QFrame(self.tab_3)
        self.line_4.setGeometry(QtCore.QRect(750, -10, 20, 831))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.Use_16 = QtGui.QCheckBox(self.tab_3)
        self.Use_16.setGeometry(QtCore.QRect(1100, 120, 16, 20))
        self.Use_16.setText(_fromUtf8(""))
        self.Use_16.setChecked(True)
        self.Use_16.setObjectName(_fromUtf8("Use_16"))
        self.Use_17 = QtGui.QCheckBox(self.tab_3)
        self.Use_17.setGeometry(QtCore.QRect(1100, 400, 16, 20))
        self.Use_17.setText(_fromUtf8(""))
        self.Use_17.setChecked(True)
        self.Use_17.setObjectName(_fromUtf8("Use_17"))
        self.widget_10 = QtGui.QWidget(self.tab_3)
        self.widget_10.setGeometry(QtCore.QRect(20, 20, 281, 250))
        self.widget_10.setObjectName(_fromUtf8("widget_10"))
        self.Use_18 = QtGui.QCheckBox(self.tab_3)
        self.Use_18.setGeometry(QtCore.QRect(1100, 670, 16, 20))
        self.Use_18.setText(_fromUtf8(""))
        self.Use_18.setChecked(True)
        self.Use_18.setObjectName(_fromUtf8("Use_18"))
        self.widget_16 = QtGui.QWidget(self.tab_3)
        self.widget_16.setGeometry(QtCore.QRect(800, 20, 281, 250))
        self.widget_16.setObjectName(_fromUtf8("widget_16"))
        self.Tabs.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.Use_19 = QtGui.QCheckBox(self.tab_4)
        self.Use_19.setGeometry(QtCore.QRect(330, 120, 16, 20))
        self.Use_19.setText(_fromUtf8(""))
        self.Use_19.setChecked(True)
        self.Use_19.setObjectName(_fromUtf8("Use_19"))
        self.Use_20 = QtGui.QCheckBox(self.tab_4)
        self.Use_20.setGeometry(QtCore.QRect(330, 400, 16, 20))
        self.Use_20.setText(_fromUtf8(""))
        self.Use_20.setChecked(True)
        self.Use_20.setObjectName(_fromUtf8("Use_20"))
        self.Use_21 = QtGui.QCheckBox(self.tab_4)
        self.Use_21.setGeometry(QtCore.QRect(330, 670, 16, 20))
        self.Use_21.setText(_fromUtf8(""))
        self.Use_21.setChecked(True)
        self.Use_21.setObjectName(_fromUtf8("Use_21"))
        self.widget_19 = QtGui.QWidget(self.tab_4)
        self.widget_19.setGeometry(QtCore.QRect(20, 20, 281, 250))
        self.widget_19.setObjectName(_fromUtf8("widget_19"))
        self.line_5 = QtGui.QFrame(self.tab_4)
        self.line_5.setGeometry(QtCore.QRect(360, 0, 20, 821))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.Use_22 = QtGui.QCheckBox(self.tab_4)
        self.Use_22.setGeometry(QtCore.QRect(730, 120, 16, 20))
        self.Use_22.setText(_fromUtf8(""))
        self.Use_22.setChecked(True)
        self.Use_22.setObjectName(_fromUtf8("Use_22"))
        self.Use_23 = QtGui.QCheckBox(self.tab_4)
        self.Use_23.setGeometry(QtCore.QRect(730, 400, 16, 20))
        self.Use_23.setText(_fromUtf8(""))
        self.Use_23.setChecked(True)
        self.Use_23.setObjectName(_fromUtf8("Use_23"))
        self.Use_24 = QtGui.QCheckBox(self.tab_4)
        self.Use_24.setGeometry(QtCore.QRect(730, 670, 16, 20))
        self.Use_24.setText(_fromUtf8(""))
        self.Use_24.setChecked(True)
        self.Use_24.setObjectName(_fromUtf8("Use_24"))
        self.widget_20 = QtGui.QWidget(self.tab_4)
        self.widget_20.setGeometry(QtCore.QRect(20, 290, 281, 250))
        self.widget_20.setObjectName(_fromUtf8("widget_20"))
        self.widget_21 = QtGui.QWidget(self.tab_4)
        self.widget_21.setGeometry(QtCore.QRect(20, 560, 281, 250))
        self.widget_21.setObjectName(_fromUtf8("widget_21"))
        self.widget_22 = QtGui.QWidget(self.tab_4)
        self.widget_22.setGeometry(QtCore.QRect(430, 20, 281, 250))
        self.widget_22.setObjectName(_fromUtf8("widget_22"))
        self.widget_23 = QtGui.QWidget(self.tab_4)
        self.widget_23.setGeometry(QtCore.QRect(430, 290, 281, 250))
        self.widget_23.setObjectName(_fromUtf8("widget_23"))
        self.widget_24 = QtGui.QWidget(self.tab_4)
        self.widget_24.setGeometry(QtCore.QRect(430, 560, 281, 250))
        self.widget_24.setObjectName(_fromUtf8("widget_24"))
        self.widget_25 = QtGui.QWidget(self.tab_4)
        self.widget_25.setGeometry(QtCore.QRect(800, 20, 281, 250))
        self.widget_25.setObjectName(_fromUtf8("widget_25"))
        self.line_6 = QtGui.QFrame(self.tab_4)
        self.line_6.setGeometry(QtCore.QRect(750, -10, 20, 831))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.Use_25 = QtGui.QCheckBox(self.tab_4)
        self.Use_25.setGeometry(QtCore.QRect(1100, 120, 16, 20))
        self.Use_25.setText(_fromUtf8(""))
        self.Use_25.setChecked(True)
        self.Use_25.setObjectName(_fromUtf8("Use_25"))
        self.Use_26 = QtGui.QCheckBox(self.tab_4)
        self.Use_26.setGeometry(QtCore.QRect(1100, 400, 16, 20))
        self.Use_26.setText(_fromUtf8(""))
        self.Use_26.setChecked(True)
        self.Use_26.setObjectName(_fromUtf8("Use_26"))
        self.widget_26 = QtGui.QWidget(self.tab_4)
        self.widget_26.setGeometry(QtCore.QRect(800, 290, 281, 250))
        self.widget_26.setObjectName(_fromUtf8("widget_26"))
        self.Use_27 = QtGui.QCheckBox(self.tab_4)
        self.Use_27.setGeometry(QtCore.QRect(1100, 670, 16, 20))
        self.Use_27.setText(_fromUtf8(""))
        self.Use_27.setChecked(True)
        self.Use_27.setObjectName(_fromUtf8("Use_27"))
        self.widget_27 = QtGui.QWidget(self.tab_4)
        self.widget_27.setGeometry(QtCore.QRect(800, 560, 281, 250))
        self.widget_27.setObjectName(_fromUtf8("widget_27"))
        self.Tabs.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.Use_28 = QtGui.QCheckBox(self.tab_5)
        self.Use_28.setGeometry(QtCore.QRect(330, 120, 16, 20))
        self.Use_28.setText(_fromUtf8(""))
        self.Use_28.setChecked(True)
        self.Use_28.setObjectName(_fromUtf8("Use_28"))
        self.Use_29 = QtGui.QCheckBox(self.tab_5)
        self.Use_29.setGeometry(QtCore.QRect(330, 400, 16, 20))
        self.Use_29.setText(_fromUtf8(""))
        self.Use_29.setChecked(True)
        self.Use_29.setObjectName(_fromUtf8("Use_29"))
        self.Use_30 = QtGui.QCheckBox(self.tab_5)
        self.Use_30.setGeometry(QtCore.QRect(330, 670, 16, 20))
        self.Use_30.setText(_fromUtf8(""))
        self.Use_30.setChecked(True)
        self.Use_30.setObjectName(_fromUtf8("Use_30"))
        self.widget_28 = QtGui.QWidget(self.tab_5)
        self.widget_28.setGeometry(QtCore.QRect(20, 20, 281, 250))
        self.widget_28.setObjectName(_fromUtf8("widget_28"))
        self.line_7 = QtGui.QFrame(self.tab_5)
        self.line_7.setGeometry(QtCore.QRect(360, 0, 20, 821))
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.Use_31 = QtGui.QCheckBox(self.tab_5)
        self.Use_31.setGeometry(QtCore.QRect(730, 120, 16, 20))
        self.Use_31.setText(_fromUtf8(""))
        self.Use_31.setChecked(True)
        self.Use_31.setObjectName(_fromUtf8("Use_31"))
        self.Use_32 = QtGui.QCheckBox(self.tab_5)
        self.Use_32.setGeometry(QtCore.QRect(730, 400, 16, 20))
        self.Use_32.setText(_fromUtf8(""))
        self.Use_32.setChecked(True)
        self.Use_32.setObjectName(_fromUtf8("Use_32"))
        self.Use_33 = QtGui.QCheckBox(self.tab_5)
        self.Use_33.setGeometry(QtCore.QRect(730, 670, 16, 20))
        self.Use_33.setText(_fromUtf8(""))
        self.Use_33.setChecked(True)
        self.Use_33.setObjectName(_fromUtf8("Use_33"))
        self.widget_29 = QtGui.QWidget(self.tab_5)
        self.widget_29.setGeometry(QtCore.QRect(20, 290, 281, 250))
        self.widget_29.setObjectName(_fromUtf8("widget_29"))
        self.widget_30 = QtGui.QWidget(self.tab_5)
        self.widget_30.setGeometry(QtCore.QRect(20, 560, 281, 250))
        self.widget_30.setObjectName(_fromUtf8("widget_30"))
        self.widget_31 = QtGui.QWidget(self.tab_5)
        self.widget_31.setGeometry(QtCore.QRect(430, 20, 281, 250))
        self.widget_31.setObjectName(_fromUtf8("widget_31"))
        self.widget_32 = QtGui.QWidget(self.tab_5)
        self.widget_32.setGeometry(QtCore.QRect(430, 290, 281, 250))
        self.widget_32.setObjectName(_fromUtf8("widget_32"))
        self.widget_33 = QtGui.QWidget(self.tab_5)
        self.widget_33.setGeometry(QtCore.QRect(430, 560, 281, 250))
        self.widget_33.setObjectName(_fromUtf8("widget_33"))
        self.widget_34 = QtGui.QWidget(self.tab_5)
        self.widget_34.setGeometry(QtCore.QRect(800, 20, 281, 250))
        self.widget_34.setObjectName(_fromUtf8("widget_34"))
        self.line_8 = QtGui.QFrame(self.tab_5)
        self.line_8.setGeometry(QtCore.QRect(750, -10, 20, 831))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.Use_34 = QtGui.QCheckBox(self.tab_5)
        self.Use_34.setGeometry(QtCore.QRect(1100, 120, 16, 20))
        self.Use_34.setText(_fromUtf8(""))
        self.Use_34.setChecked(True)
        self.Use_34.setObjectName(_fromUtf8("Use_34"))
        self.Use_35 = QtGui.QCheckBox(self.tab_5)
        self.Use_35.setGeometry(QtCore.QRect(1100, 400, 16, 20))
        self.Use_35.setText(_fromUtf8(""))
        self.Use_35.setChecked(True)
        self.Use_35.setObjectName(_fromUtf8("Use_35"))
        self.widget_35 = QtGui.QWidget(self.tab_5)
        self.widget_35.setGeometry(QtCore.QRect(800, 290, 281, 250))
        self.widget_35.setObjectName(_fromUtf8("widget_35"))
        self.Use_36 = QtGui.QCheckBox(self.tab_5)
        self.Use_36.setGeometry(QtCore.QRect(1100, 670, 16, 20))
        self.Use_36.setText(_fromUtf8(""))
        self.Use_36.setChecked(True)
        self.Use_36.setObjectName(_fromUtf8("Use_36"))
        self.widget_36 = QtGui.QWidget(self.tab_5)
        self.widget_36.setGeometry(QtCore.QRect(800, 560, 281, 250))
        self.widget_36.setObjectName(_fromUtf8("widget_36"))
        self.Tabs.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.Use_37 = QtGui.QCheckBox(self.tab_6)
        self.Use_37.setGeometry(QtCore.QRect(330, 120, 16, 20))
        self.Use_37.setText(_fromUtf8(""))
        self.Use_37.setChecked(True)
        self.Use_37.setObjectName(_fromUtf8("Use_37"))
        self.Use_38 = QtGui.QCheckBox(self.tab_6)
        self.Use_38.setGeometry(QtCore.QRect(330, 400, 16, 20))
        self.Use_38.setText(_fromUtf8(""))
        self.Use_38.setChecked(True)
        self.Use_38.setObjectName(_fromUtf8("Use_38"))
        self.Use_39 = QtGui.QCheckBox(self.tab_6)
        self.Use_39.setGeometry(QtCore.QRect(330, 670, 16, 20))
        self.Use_39.setText(_fromUtf8(""))
        self.Use_39.setChecked(True)
        self.Use_39.setObjectName(_fromUtf8("Use_39"))
        self.widget_37 = QtGui.QWidget(self.tab_6)
        self.widget_37.setGeometry(QtCore.QRect(20, 20, 281, 250))
        self.widget_37.setObjectName(_fromUtf8("widget_37"))
        self.line_9 = QtGui.QFrame(self.tab_6)
        self.line_9.setGeometry(QtCore.QRect(360, 0, 20, 821))
        self.line_9.setFrameShape(QtGui.QFrame.VLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.Use_40 = QtGui.QCheckBox(self.tab_6)
        self.Use_40.setGeometry(QtCore.QRect(730, 120, 16, 20))
        self.Use_40.setText(_fromUtf8(""))
        self.Use_40.setChecked(True)
        self.Use_40.setObjectName(_fromUtf8("Use_40"))
        self.Use_41 = QtGui.QCheckBox(self.tab_6)
        self.Use_41.setGeometry(QtCore.QRect(730, 400, 16, 20))
        self.Use_41.setText(_fromUtf8(""))
        self.Use_41.setChecked(True)
        self.Use_41.setObjectName(_fromUtf8("Use_41"))
        self.Use_42 = QtGui.QCheckBox(self.tab_6)
        self.Use_42.setGeometry(QtCore.QRect(730, 670, 16, 20))
        self.Use_42.setText(_fromUtf8(""))
        self.Use_42.setChecked(True)
        self.Use_42.setObjectName(_fromUtf8("Use_42"))
        self.widget_38 = QtGui.QWidget(self.tab_6)
        self.widget_38.setGeometry(QtCore.QRect(20, 290, 281, 250))
        self.widget_38.setObjectName(_fromUtf8("widget_38"))
        self.widget_39 = QtGui.QWidget(self.tab_6)
        self.widget_39.setGeometry(QtCore.QRect(20, 560, 281, 250))
        self.widget_39.setObjectName(_fromUtf8("widget_39"))
        self.widget_40 = QtGui.QWidget(self.tab_6)
        self.widget_40.setGeometry(QtCore.QRect(430, 20, 281, 250))
        self.widget_40.setObjectName(_fromUtf8("widget_40"))
        self.widget_41 = QtGui.QWidget(self.tab_6)
        self.widget_41.setGeometry(QtCore.QRect(430, 290, 281, 250))
        self.widget_41.setObjectName(_fromUtf8("widget_41"))
        self.widget_42 = QtGui.QWidget(self.tab_6)
        self.widget_42.setGeometry(QtCore.QRect(430, 560, 281, 250))
        self.widget_42.setObjectName(_fromUtf8("widget_42"))
        self.widget_43 = QtGui.QWidget(self.tab_6)
        self.widget_43.setGeometry(QtCore.QRect(800, 20, 281, 250))
        self.widget_43.setObjectName(_fromUtf8("widget_43"))
        self.line_10 = QtGui.QFrame(self.tab_6)
        self.line_10.setGeometry(QtCore.QRect(750, -10, 20, 831))
        self.line_10.setFrameShape(QtGui.QFrame.VLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.Use_43 = QtGui.QCheckBox(self.tab_6)
        self.Use_43.setGeometry(QtCore.QRect(1100, 120, 16, 20))
        self.Use_43.setText(_fromUtf8(""))
        self.Use_43.setChecked(True)
        self.Use_43.setObjectName(_fromUtf8("Use_43"))
        self.Use_44 = QtGui.QCheckBox(self.tab_6)
        self.Use_44.setGeometry(QtCore.QRect(1100, 400, 16, 20))
        self.Use_44.setText(_fromUtf8(""))
        self.Use_44.setChecked(True)
        self.Use_44.setObjectName(_fromUtf8("Use_44"))
        self.widget_44 = QtGui.QWidget(self.tab_6)
        self.widget_44.setGeometry(QtCore.QRect(800, 290, 281, 250))
        self.widget_44.setObjectName(_fromUtf8("widget_44"))
        self.Use_45 = QtGui.QCheckBox(self.tab_6)
        self.Use_45.setGeometry(QtCore.QRect(1100, 670, 16, 20))
        self.Use_45.setText(_fromUtf8(""))
        self.Use_45.setChecked(True)
        self.Use_45.setObjectName(_fromUtf8("Use_45"))
        self.widget_45 = QtGui.QWidget(self.tab_6)
        self.widget_45.setGeometry(QtCore.QRect(800, 560, 281, 250))
        self.widget_45.setObjectName(_fromUtf8("widget_45"))
        self.Tabs.addTab(self.tab_6, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.widget_54 = QtGui.QWidget(self.tab_7)
        self.widget_54.setGeometry(QtCore.QRect(800, 560, 281, 250))
        self.widget_54.setObjectName(_fromUtf8("widget_54"))
        self.widget_48 = QtGui.QWidget(self.tab_7)
        self.widget_48.setGeometry(QtCore.QRect(20, 560, 281, 250))
        self.widget_48.setObjectName(_fromUtf8("widget_48"))
        self.Use_46 = QtGui.QCheckBox(self.tab_7)
        self.Use_46.setGeometry(QtCore.QRect(330, 120, 16, 20))
        self.Use_46.setText(_fromUtf8(""))
        self.Use_46.setChecked(True)
        self.Use_46.setObjectName(_fromUtf8("Use_46"))
        self.widget_53 = QtGui.QWidget(self.tab_7)
        self.widget_53.setGeometry(QtCore.QRect(800, 290, 281, 250))
        self.widget_53.setObjectName(_fromUtf8("widget_53"))
        self.widget_49 = QtGui.QWidget(self.tab_7)
        self.widget_49.setGeometry(QtCore.QRect(430, 20, 281, 250))
        self.widget_49.setObjectName(_fromUtf8("widget_49"))
        self.widget_47 = QtGui.QWidget(self.tab_7)
        self.widget_47.setGeometry(QtCore.QRect(20, 290, 281, 250))
        self.widget_47.setObjectName(_fromUtf8("widget_47"))
        self.Use_54 = QtGui.QCheckBox(self.tab_7)
        self.Use_54.setGeometry(QtCore.QRect(1100, 670, 16, 20))
        self.Use_54.setText(_fromUtf8(""))
        self.Use_54.setChecked(True)
        self.Use_54.setObjectName(_fromUtf8("Use_54"))
        self.Use_51 = QtGui.QCheckBox(self.tab_7)
        self.Use_51.setGeometry(QtCore.QRect(730, 670, 16, 20))
        self.Use_51.setText(_fromUtf8(""))
        self.Use_51.setChecked(True)
        self.Use_51.setObjectName(_fromUtf8("Use_51"))
        self.Use_52 = QtGui.QCheckBox(self.tab_7)
        self.Use_52.setGeometry(QtCore.QRect(1100, 120, 16, 20))
        self.Use_52.setText(_fromUtf8(""))
        self.Use_52.setChecked(True)
        self.Use_52.setObjectName(_fromUtf8("Use_52"))
        self.line_11 = QtGui.QFrame(self.tab_7)
        self.line_11.setGeometry(QtCore.QRect(360, 0, 20, 821))
        self.line_11.setFrameShape(QtGui.QFrame.VLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.widget_52 = QtGui.QWidget(self.tab_7)
        self.widget_52.setGeometry(QtCore.QRect(800, 20, 281, 250))
        self.widget_52.setObjectName(_fromUtf8("widget_52"))
        self.Use_49 = QtGui.QCheckBox(self.tab_7)
        self.Use_49.setGeometry(QtCore.QRect(730, 120, 16, 20))
        self.Use_49.setText(_fromUtf8(""))
        self.Use_49.setChecked(True)
        self.Use_49.setObjectName(_fromUtf8("Use_49"))
        self.widget_46 = QtGui.QWidget(self.tab_7)
        self.widget_46.setGeometry(QtCore.QRect(20, 20, 281, 250))
        self.widget_46.setObjectName(_fromUtf8("widget_46"))
        self.widget_51 = QtGui.QWidget(self.tab_7)
        self.widget_51.setGeometry(QtCore.QRect(430, 560, 281, 250))
        self.widget_51.setObjectName(_fromUtf8("widget_51"))
        self.Use_50 = QtGui.QCheckBox(self.tab_7)
        self.Use_50.setGeometry(QtCore.QRect(730, 400, 16, 20))
        self.Use_50.setText(_fromUtf8(""))
        self.Use_50.setChecked(True)
        self.Use_50.setObjectName(_fromUtf8("Use_50"))
        self.line_12 = QtGui.QFrame(self.tab_7)
        self.line_12.setGeometry(QtCore.QRect(750, -10, 20, 831))
        self.line_12.setFrameShape(QtGui.QFrame.VLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.Use_48 = QtGui.QCheckBox(self.tab_7)
        self.Use_48.setGeometry(QtCore.QRect(330, 670, 16, 20))
        self.Use_48.setText(_fromUtf8(""))
        self.Use_48.setChecked(True)
        self.Use_48.setObjectName(_fromUtf8("Use_48"))
        self.widget_50 = QtGui.QWidget(self.tab_7)
        self.widget_50.setGeometry(QtCore.QRect(430, 290, 281, 250))
        self.widget_50.setObjectName(_fromUtf8("widget_50"))
        self.Use_53 = QtGui.QCheckBox(self.tab_7)
        self.Use_53.setGeometry(QtCore.QRect(1100, 400, 16, 20))
        self.Use_53.setText(_fromUtf8(""))
        self.Use_53.setChecked(True)
        self.Use_53.setObjectName(_fromUtf8("Use_53"))
        self.Use_47 = QtGui.QCheckBox(self.tab_7)
        self.Use_47.setGeometry(QtCore.QRect(330, 400, 16, 20))
        self.Use_47.setText(_fromUtf8(""))
        self.Use_47.setChecked(True)
        self.Use_47.setObjectName(_fromUtf8("Use_47"))
        self.Tabs.addTab(self.tab_7, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.Use_55 = QtGui.QCheckBox(self.tab)
        self.Use_55.setGeometry(QtCore.QRect(330, 120, 16, 20))
        self.Use_55.setText(_fromUtf8(""))
        self.Use_55.setChecked(True)
        self.Use_55.setObjectName(_fromUtf8("Use_55"))
        self.Use_56 = QtGui.QCheckBox(self.tab)
        self.Use_56.setGeometry(QtCore.QRect(330, 400, 16, 20))
        self.Use_56.setText(_fromUtf8(""))
        self.Use_56.setChecked(True)
        self.Use_56.setObjectName(_fromUtf8("Use_56"))
        self.Use_57 = QtGui.QCheckBox(self.tab)
        self.Use_57.setGeometry(QtCore.QRect(330, 670, 16, 20))
        self.Use_57.setText(_fromUtf8(""))
        self.Use_57.setChecked(True)
        self.Use_57.setObjectName(_fromUtf8("Use_57"))
        self.widget_55 = QtGui.QWidget(self.tab)
        self.widget_55.setGeometry(QtCore.QRect(20, 20, 281, 250))
        self.widget_55.setObjectName(_fromUtf8("widget_55"))
        self.line_13 = QtGui.QFrame(self.tab)
        self.line_13.setGeometry(QtCore.QRect(360, 0, 20, 821))
        self.line_13.setFrameShape(QtGui.QFrame.VLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.Use_58 = QtGui.QCheckBox(self.tab)
        self.Use_58.setGeometry(QtCore.QRect(730, 120, 16, 20))
        self.Use_58.setText(_fromUtf8(""))
        self.Use_58.setChecked(True)
        self.Use_58.setObjectName(_fromUtf8("Use_58"))
        self.Use_59 = QtGui.QCheckBox(self.tab)
        self.Use_59.setGeometry(QtCore.QRect(730, 400, 16, 20))
        self.Use_59.setText(_fromUtf8(""))
        self.Use_59.setChecked(True)
        self.Use_59.setObjectName(_fromUtf8("Use_59"))
        self.Use_60 = QtGui.QCheckBox(self.tab)
        self.Use_60.setGeometry(QtCore.QRect(730, 670, 16, 20))
        self.Use_60.setText(_fromUtf8(""))
        self.Use_60.setChecked(True)
        self.Use_60.setObjectName(_fromUtf8("Use_60"))
        self.widget_56 = QtGui.QWidget(self.tab)
        self.widget_56.setGeometry(QtCore.QRect(20, 290, 281, 250))
        self.widget_56.setObjectName(_fromUtf8("widget_56"))
        self.widget_57 = QtGui.QWidget(self.tab)
        self.widget_57.setGeometry(QtCore.QRect(20, 560, 281, 250))
        self.widget_57.setObjectName(_fromUtf8("widget_57"))
        self.widget_58 = QtGui.QWidget(self.tab)
        self.widget_58.setGeometry(QtCore.QRect(430, 20, 281, 250))
        self.widget_58.setObjectName(_fromUtf8("widget_58"))
        self.widget_59 = QtGui.QWidget(self.tab)
        self.widget_59.setGeometry(QtCore.QRect(430, 290, 281, 250))
        self.widget_59.setObjectName(_fromUtf8("widget_59"))
        self.widget_60 = QtGui.QWidget(self.tab)
        self.widget_60.setGeometry(QtCore.QRect(430, 560, 281, 250))
        self.widget_60.setObjectName(_fromUtf8("widget_60"))
        self.line_14 = QtGui.QFrame(self.tab)
        self.line_14.setGeometry(QtCore.QRect(750, -10, 20, 831))
        self.line_14.setFrameShape(QtGui.QFrame.VLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.Use_61 = QtGui.QCheckBox(self.tab)
        self.Use_61.setGeometry(QtCore.QRect(1100, 120, 16, 20))
        self.Use_61.setText(_fromUtf8(""))
        self.Use_61.setChecked(True)
        self.Use_61.setObjectName(_fromUtf8("Use_61"))
        self.widget_61 = QtGui.QWidget(self.tab)
        self.widget_61.setGeometry(QtCore.QRect(800, 20, 281, 250))
        self.widget_61.setObjectName(_fromUtf8("widget_61"))
        self.Use_62 = QtGui.QCheckBox(self.tab)
        self.Use_62.setGeometry(QtCore.QRect(1100, 400, 16, 20))
        self.Use_62.setText(_fromUtf8(""))
        self.Use_62.setChecked(True)
        self.Use_62.setObjectName(_fromUtf8("Use_62"))
        self.widget_62 = QtGui.QWidget(self.tab)
        self.widget_62.setGeometry(QtCore.QRect(800, 290, 281, 250))
        self.widget_62.setObjectName(_fromUtf8("widget_62"))
        self.Tabs.addTab(self.tab, _fromUtf8(""))
        self.Advance = QtGui.QPushButton(self.centralWidget)
        self.Advance.setGeometry(QtCore.QRect(10, 890, 1131, 20))
        self.Advance.setObjectName(_fromUtf8("Advance"))
        self.Toolbar = QtGui.QFrame(self.centralWidget)
        self.Toolbar.setGeometry(QtCore.QRect(0, 850, 1141, 41))
        self.Toolbar.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Toolbar.setFrameShadow(QtGui.QFrame.Raised)
        self.Toolbar.setObjectName(_fromUtf8("Toolbar"))
        MultiplotViewer.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MultiplotViewer)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1155, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuVersuib_IObe = QtGui.QMenu(self.menuBar)
        self.menuVersuib_IObe.setObjectName(_fromUtf8("menuVersuib_IObe"))
        MultiplotViewer.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MultiplotViewer)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MultiplotViewer.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MultiplotViewer)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MultiplotViewer.setStatusBar(self.statusBar)
        self.actionQuit = QtGui.QAction(MultiplotViewer)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuVersuib_IObe.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuVersuib_IObe.menuAction())

        self.retranslateUi(MultiplotViewer)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MultiplotViewer)

    def retranslateUi(self, MultiplotViewer):
        MultiplotViewer.setWindowTitle(_translate("MultiplotViewer", "TestWindow", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.firstTab), _translate("MultiplotViewer", "1-9", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_3), _translate("MultiplotViewer", "10-18", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_4), _translate("MultiplotViewer", "19-27", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_5), _translate("MultiplotViewer", "28-36", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_6), _translate("MultiplotViewer", "37-45", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_7), _translate("MultiplotViewer", "46-54", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab), _translate("MultiplotViewer", "55-62", None))
        self.Advance.setText(_translate("MultiplotViewer", "Advance", None))
        self.menuVersuib_IObe.setTitle(_translate("MultiplotViewer", "File", None))
        self.actionQuit.setText(_translate("MultiplotViewer", "Quit", None))

