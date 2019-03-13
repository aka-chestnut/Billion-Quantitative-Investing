# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stockK.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Kwindow(object):
    def setupUi(self, Kwindow):
        Kwindow.setObjectName("Kwindow")
        Kwindow.resize(1101, 791)
        self.gridLayout_2 = QtWidgets.QGridLayout(Kwindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Kwindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(1, 8))
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 4, 1)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(Kwindow)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.gridLayout.addWidget(self.webEngineView, 4, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Kwindow)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 4, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 10)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 2)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 80)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Kwindow)
        QtCore.QMetaObject.connectSlotsByName(Kwindow)

    def retranslateUi(self, Kwindow):
        _translate = QtCore.QCoreApplication.translate
        Kwindow.setWindowTitle(_translate("Kwindow", "Kwindow"))
        self.label.setText(_translate("Kwindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">股票代码</span></p></body></html>"))


from PyQt5 import QtWebEngineWidgets
