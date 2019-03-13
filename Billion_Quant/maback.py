# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maback.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
from PyQt5.QtCore import (QByteArray, QDataStream, QIODevice, QMimeData,
        QPoint, QSize, Qt)
from PyQt5.QtWidgets import (QApplication, QDialog,QGridLayout,
                             QLineEdit, QListWidget,QListWidgetItem, QWidget,QMenu)
from PyQt5.QtGui import QIcon,QColor,QPainter,QFontMetricsF,QDrag,QCursor


class QListWidgetPro(QtWidgets.QListWidget):
    def __init__(self, parent):
        super(QListWidgetPro, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.dropAction = Qt.CopyAction
        self.update()


    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-icon-and-text"):
            event.accept()
            self.update()
        else:
            event.ignore()
            self.update()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("application/x-icon-and-text"):
            event.setDropAction(Qt.MoveAction)
            event.accept()
            self.update()

        else:
            event.ignore()
            self.update()

    def dropEvent(self, event):
        if event.mimeData().hasFormat("application/x-icon-and-text"):
            data = event.mimeData().data("application/x-icon-and-text")
            stream = QDataStream(data, QIODevice.ReadOnly)
            text = ""
            icon = QIcon()
            text=stream.readQString()
            stream>>icon
            self.dropAction = Qt.MoveAction
            item = QListWidgetItem(text, self)
            item.setIcon(icon)
            event.setDropAction(self.dropAction)
            event.accept()
            self.update()
            return
        self.update()
        event.ignore()

    def startDrag(self, dropActions):
        item = self.currentItem()
        icon = item.icon()
        data = QByteArray()
        stream = QDataStream(data, QIODevice.WriteOnly)
        stream.writeQString(item.text())
        stream<<icon
        mimeData = QMimeData()
        mimeData.setData("application/x-icon-and-text", data)
        drag = QDrag(self)
        drag.setMimeData(mimeData)
        pixmap = icon.pixmap(24, 24)
        drag.setHotSpot(QPoint(12, 12))
        drag.setPixmap(pixmap)
        if (drag.exec(Qt.MoveAction|Qt.CopyAction) == Qt.MoveAction):
            self.takeItem(self.row(item))
            self.update()


class Ui_Maback(object):
    def setupUi(self, Maback):
        Maback.setObjectName("Maback")
        Maback.resize(1130, 791)
        self.gridLayout_5 = QtWidgets.QGridLayout(Maback)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Maback)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        #self.sameamount = QtWidgets.QRadioButton(Maback)
        #self.sameamount.setObjectName("sameamount")
        #self.horizontalLayout_2.addWidget(self.sameamount)
        self.samemoney = QtWidgets.QRadioButton(Maback)
        self.samemoney.setObjectName("samemoney")
        self.horizontalLayout_2.addWidget(self.samemoney)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Maback)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateEdit = QtWidgets.QDateEdit(Maback)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 4)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dayplot = QtWebEngineWidgets.QWebEngineView(Maback)
        self.dayplot.setUrl(QtCore.QUrl("about:blank"))
        self.dayplot.setObjectName("dayplot")
        self.gridLayout_3.addWidget(self.dayplot, 1, 1, 1, 1)
        self.yieldplot = QtWebEngineWidgets.QWebEngineView(Maback)
        self.yieldplot.setUrl(QtCore.QUrl("about:blank"))
        self.yieldplot.setObjectName("yieldplot")
        self.gridLayout_3.addWidget(self.yieldplot, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_14 = QtWidgets.QLabel(Maback)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.stockbtn = QtWidgets.QPushButton(Maback)
        self.stockbtn.setObjectName("stockbtn")
        self.gridLayout.addWidget(self.stockbtn, 2, 2, 2, 1)
        self.yearyieldlabel = QtWidgets.QLabel(Maback)
        self.yearyieldlabel.setText("")
        self.yearyieldlabel.setObjectName("yearyieldlabel")
        self.gridLayout.addWidget(self.yearyieldlabel, 3, 1, 1, 1)
        self.yieldlabel = QtWidgets.QLabel(Maback)
        self.yieldlabel.setText("")
        self.yieldlabel.setObjectName("yieldlabel")
        self.gridLayout.addWidget(self.yieldlabel, 2, 1, 1, 1)
        self.valuebtn = QtWidgets.QPushButton(Maback)
        self.valuebtn.setObjectName("valuebtn")
        self.gridLayout.addWidget(self.valuebtn, 6, 2, 2, 1)
        self.label_6 = QtWidgets.QLabel(Maback)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Maback)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.sharplabel = QtWidgets.QLabel(Maback)
        self.sharplabel.setText("")
        self.sharplabel.setObjectName("sharplabel")
        self.gridLayout.addWidget(self.sharplabel, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Maback)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Maback)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.backlabel = QtWidgets.QLabel(Maback)
        self.backlabel.setText("")
        self.backlabel.setObjectName("backlabel")
        self.gridLayout.addWidget(self.backlabel, 7, 1, 1, 1)
        self.stdlabel = QtWidgets.QLabel(Maback)
        self.stdlabel.setText("")
        self.stdlabel.setObjectName("stdlabel")
        self.gridLayout.addWidget(self.stdlabel, 4, 1, 2, 1)
        self.label_5 = QtWidgets.QLabel(Maback)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 2, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(5, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 1, 1, 2)
        self.label_13 = QtWidgets.QLabel(Maback)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 1, 1, 1)
        self.selectlist = QListWidgetPro(Maback)
        self.selectlist.setObjectName("selectlist")
        self.gridLayout_2.addWidget(self.selectlist, 1, 1, 2, 1)
        self.stralist = QListWidgetPro(Maback)
        self.stralist.setObjectName("stralist")
        self.gridLayout_2.addWidget(self.stralist, 1, 2, 2, 1)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 5)
        self.gridLayout_2.setRowStretch(2, 3)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 2, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setRowStretch(0, 2)
        self.gridLayout_3.setRowStretch(1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.retranslateUi(Maback)
        QtCore.QMetaObject.connectSlotsByName(Maback)

    def retranslateUi(self, Maback):
        _translate = QtCore.QCoreApplication.translate
        Maback.setWindowTitle(_translate("Maback", "Form"))
        self.label.setText(_translate("Maback", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">均线策略回测系统</span></p></body></html>"))
        #self.sameamount.setText(_translate("Maback", "每次买入等量"))
        self.samemoney.setText(_translate("Maback", "每次买入等值"))
        self.label_2.setText(_translate("Maback", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">策略开始日期    </span></p></body></html>"))
        self.label_14.setText(_translate("Maback", "<html><head/><body><p><span style=\" font-size:12pt;\">策略股池</span></p></body></html>"))
        self.stockbtn.setText(_translate("Maback", "持仓表"))
        self.valuebtn.setText(_translate("Maback", "净值表"))
        self.label_6.setText(_translate("Maback", "夏普比率"))
        self.label_4.setText(_translate("Maback", "年化收益"))
        self.label_3.setText(_translate("Maback", "累计收益"))
        self.label_7.setText(_translate("Maback", "最大回撤"))
        self.label_5.setText(_translate("Maback", "波动率"))
        self.label_13.setText(_translate("Maback", "<html><head/><body><p><span style=\" font-size:12pt;\">可选股票</span></p></body></html>"))

from PyQt5 import QtWebEngineWidgets
