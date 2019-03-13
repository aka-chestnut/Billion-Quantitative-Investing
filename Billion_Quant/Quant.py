# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Quant.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import icon

class Ui_esayQunat(object):
    def setupUi(self, esayQunat):
        esayQunat.setObjectName("esayQunat")
        esayQunat.resize(1101, 791)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(esayQunat.sizePolicy().hasHeightForWidth())
        esayQunat.setSizePolicy(sizePolicy)
        esayQunat.setAutoFillBackground(False)
        self.setWindowIcon(QtGui.QIcon(':/icon/icon/mainicon.ico'))
        self.MainBack = QtWidgets.QWidget(esayQunat)
        self.MainBack.setObjectName("MainBack")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.MainBack)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.Title = QtWidgets.QLabel(self.MainBack)
        self.Title.setEnabled(True)
        self.Title.setMinimumSize(QtCore.QSize(84, 70))
        self.Title.setTextFormat(QtCore.Qt.RichText)
        self.Title.setScaledContents(False)
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 0, 0, 1, 1)
        self.TopImage = QtWidgets.QLabel(self.MainBack)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.TopImage.sizePolicy().hasHeightForWidth())
        self.TopImage.setSizePolicy(sizePolicy)
        self.TopImage.setMinimumSize(QtCore.QSize(94, 72))
        self.TopImage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.TopImage.setBaseSize(QtCore.QSize(1053, 588))
        self.TopImage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TopImage.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TopImage.setText("")
        self.TopImage.setTextFormat(QtCore.Qt.PlainText)
        self.TopImage.setPixmap(QtGui.QPixmap(":/img/image/timg.jpg"))
        self.TopImage.setScaledContents(True)
        self.TopImage.setIndent(0)
        self.TopImage.setOpenExternalLinks(False)
        self.TopImage.setObjectName("TopImage")
        self.gridLayout.addWidget(self.TopImage, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        esayQunat.setCentralWidget(self.MainBack)
        self.menubar = QtWidgets.QMenuBar(esayQunat)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 26))
        self.menubar.setObjectName("menubar")
        self.File = QtWidgets.QMenu(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.File.sizePolicy().hasHeightForWidth())
        self.File.setSizePolicy(sizePolicy)
        self.File.setObjectName("File")
        self.Stock = QtWidgets.QMenu(self.menubar)
        self.Stock.setObjectName("Stock")
        self.Index = QtWidgets.QMenu(self.menubar)
        self.Index.setObjectName("Index")
        self.Back = QtWidgets.QMenu(self.menubar)
        self.Back.setObjectName("Back")
        self.About = QtWidgets.QMenu(self.menubar)
        self.About.setObjectName("About")
        esayQunat.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(esayQunat)
        self.statusbar.setObjectName("statusbar")
        esayQunat.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(esayQunat)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAuthor = QtWidgets.QAction(esayQunat)
        self.actionAuthor.setObjectName("actionAuthor")
        self.actionOpen = QtWidgets.QAction(esayQunat)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(esayQunat)
        self.actionSave.setObjectName("actionSave")
        self.actionStat = QtWidgets.QAction(esayQunat)
        self.actionStat.setObjectName("actionStat")
        self.actionKline = QtWidgets.QAction(esayQunat)
        self.actionKline.setObjectName("actionKline")
        self.actionMA = QtWidgets.QAction(esayQunat)
        self.actionMA.setObjectName("actionMA")
        self.actionMA_Stragedy = QtWidgets.QAction(esayQunat)
        self.actionMA_Stragedy.setObjectName("actionMA_Stragedy")
        self.actionData = QtWidgets.QAction(esayQunat)
        self.actionData.setObjectName("actionData")
        self.File.addAction(self.actionOpen)
        self.File.addAction(self.actionSave)
        self.Stock.addAction(self.actionData)
        self.Stock.addAction(self.actionStat)
        self.Stock.addAction(self.actionKline)
        self.Index.addAction(self.actionMA)
        self.Back.addAction(self.actionMA_Stragedy)
        self.About.addAction(self.actionHelp)
        self.About.addAction(self.actionAuthor)
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Stock.menuAction())
        self.menubar.addAction(self.Index.menuAction())
        self.menubar.addAction(self.Back.menuAction())
        self.menubar.addAction(self.About.menuAction())

        self.retranslateUi(esayQunat)
        QtCore.QMetaObject.connectSlotsByName(esayQunat)

    def retranslateUi(self, esayQunat):
        _translate = QtCore.QCoreApplication.translate
        esayQunat.setWindowTitle(_translate("esayQunat", "easyQuant v1.0"))
        self.Title.setText(_translate("esayQunat", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; color:#00007f;\">easyQuant v1.0</span></p></body></html>"))
        self.File.setTitle(_translate("esayQunat", "文件"))
        self.Stock.setTitle(_translate("esayQunat", "行情"))
        self.Index.setTitle(_translate("esayQunat", "指标"))
        self.Back.setTitle(_translate("esayQunat", "回测"))
        self.About.setTitle(_translate("esayQunat", "关于"))
        self.actionHelp.setText(_translate("esayQunat", "帮助"))
        self.actionAuthor.setText(_translate("esayQunat", "作者"))
        self.actionOpen.setText(_translate("esayQunat", "打开"))
        self.actionOpen.setShortcut(_translate("esayQunat", "Ctrl+O"))
        self.actionSave.setText(_translate("esayQunat", "保存"))
        self.actionSave.setShortcut(_translate("esayQunat", "Ctrl+S"))
        self.actionStat.setText(_translate("esayQunat", "统计"))
        self.actionKline.setText(_translate("esayQunat", "K线"))
        self.actionMA.setText(_translate("esayQunat", "均线"))
        self.actionMA_Stragedy.setText(_translate("esayQunat", "均线策略"))
        self.actionData.setText(_translate("esayQunat", "数据"))


import quantto