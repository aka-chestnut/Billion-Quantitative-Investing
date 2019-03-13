import sys
import numpy as np
import sip
from WindowClass import *
from OtherClass import *
import pandas as pd
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Quant import Ui_esayQunat
from DataTableView import Ui_QTableOfData
from statshow import Ui_Stat
from stockK import Ui_Kwindow
from pandasmodel import PandasModel
import os
import plotly.offline as pyof
import plotly.graph_objs as go
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号


# The Main Window
class MyMainWindow(QMainWindow, Ui_esayQunat):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.center()
        self.actionOpen.triggered.connect(self.open_file)
        self.actionData.triggered.connect(self.show_data)
        self.actionStat.triggered.connect(self.stat_data)
        self.actionKline.triggered.connect(self.plot_kline)
        self.actionSave.triggered.connect(self.save_data)
        self.actionHelp.triggered.connect(self.help_me)
        self.actionAuthor.triggered.connect(self.about_me)
        self.actionMA.triggered.connect(self.plot_maline)
        self.actionMA_Stragedy.triggered.connect(self.maback)
        self.stocklist = {}

    def maback(self):
        self.child_maback = ChildrenMaback(self.stocklist)
        while self.gridLayout.count():
            child = self.gridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.child_maback.setMinimumSize(QSize(94, 72))
        self.child_maback.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout.addWidget(self.child_maback, 0, 0, 2, 1)
        self.child_maback.show()

    def plot_maline(self):
        self.child_maline = ChildrenMa(self.stocklist)
        while self.gridLayout.count():
            child = self.gridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.child_maline.setMinimumSize(QSize(94, 72))
        self.child_maline.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout.addWidget(self.child_maline, 0, 0, 2, 1)
        self.child_maline.show()

    def about_me(self):
        dialog = QDialog()
        dialog.setMinimumSize(300, 100)
        label = QLabel(dialog)
        label.setText('邮箱：huoyongkang@outlook.com')
        label.move(20, 20)
        btn = QPushButton("确定", dialog)
        btn.move(80, 80)
        dialog.setWindowTitle("联系方式")
        btn.clicked.connect(dialog.close)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    def help_me(self):
        self.childrenHelp = ChildrenHelp()
        while self.gridLayout.count():
            child = self.gridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.childrenHelp.setMinimumSize(QSize(94, 72))
        self.childrenHelp.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout.addWidget(self.childrenHelp, 0, 0, 2, 1)
        self.childrenHelp.show()

    def open_file(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)

        if dlg.exec_():
            self.filenames = dlg.selectedFiles()
            self.statusBar().showMessage('正在读取' + self.filenames[0])
            self.filethread = FileReadThread(self.filenames)  # todo:多文件读取没有限制，bug
            self.filethread.trigger.connect(self.file_return)
            self.filethread.start()

    # Show the DataTable
    def show_data(self):
        print(self.stocklist)
        # create the childwindow with data-exchange
        self.child_datatable = ChildrenDataTable(self.stocklist)
        while self.gridLayout.count():
            child = self.gridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.child_datatable.setMinimumSize(QSize(94, 72))
        self.child_datatable.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout.addWidget(self.child_datatable, 0, 0, 2, 1)
        self.child_datatable.show()

    def stat_data(self):
        # create the stat window to stat
        self.child_stattable = ChildrenStat(self.stocklist)
        while self.gridLayout.count():
            child = self.gridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.child_stattable.setMinimumSize(QSize(94, 72))
        self.child_stattable.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout.addWidget(self.child_stattable, 0, 0, 2, 1)
        self.child_stattable.show()
    # return the dataread todo : done需要对返回的数据进行加工处理，应该在多线程部分，每次加工完成一个股票就返回一次

    def save_data(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.DirectoryOnly)

        if dlg.exec_():
            self.filenames = dlg.selectedFiles()
            self.statusBar().showMessage('保存到' + self.filenames[0], 3000)
            self.savethread = FileSaveThread(self.filenames, self.stocklist)  # todo:多文件读取没有限制，bug
            self.savethread.trigger.connect(self.file_save)
            self.savethread.start()

    def file_save(self):
        self.statusBar().showMessage('保存成功！', 3000)

    def plot_kline(self):
        # create the stat window to stat
        self.child_kline = ChildrenKline(self.stocklist)
        while self.gridLayout.count():
            child = self.gridLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.child_kline.setMinimumSize(QSize(94, 72))
        self.child_kline.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout.addWidget(self.child_kline, 0, 0, 2, 1)
        self.child_kline.show()

    def file_return(self, datadict):
        self.stocklist.update(datadict)
        self.statusBar().showMessage('读取完毕', 3000)

    # make the window center
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
