# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableview.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_tableview(object):
    def setupUi(self, tableview):
        tableview.setObjectName("tableview")
        tableview.resize(765, 523)
        self.gridLayout = QtWidgets.QGridLayout(tableview)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(tableview)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)

        self.retranslateUi(tableview)
        QtCore.QMetaObject.connectSlotsByName(tableview)

    def retranslateUi(self, tableview):
        _translate = QtCore.QCoreApplication.translate
        tableview.setWindowTitle(_translate("tableview", "Form"))

