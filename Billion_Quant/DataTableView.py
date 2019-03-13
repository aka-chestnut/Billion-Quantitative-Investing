# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataTableView.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QTableOfData(object):
    def setupUi(self, QTableOfData):
        QTableOfData.setObjectName("QTableOfData")
        QTableOfData.resize(1101, 791)
        QTableOfData.setWindowTitle("")
        self.gridLayout = QtWidgets.QGridLayout(QTableOfData)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(QTableOfData)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(QTableOfData)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 3, 1, 1)
        self.tableView = QtWidgets.QTableView(QTableOfData)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 2, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(QTableOfData)
        QtCore.QMetaObject.connectSlotsByName(QTableOfData)

    def retranslateUi(self, QTableOfData):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("QTableOfData", "<html><head/><body><p><span style=\" font-size:16pt;\">股票代码</span></p></body></html>"))


