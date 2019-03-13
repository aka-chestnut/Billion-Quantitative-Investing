import sys
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DataTableView import Ui_QTableOfData
from Help import Ui_Help
from statshow import Ui_Stat
from stockK import Ui_Kwindow
from pandasmodel import PandasModel
from tableview import Ui_tableview
from OtherClass import *
from maback import Ui_Maback
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5

import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

# child window1: show the initial datatable
class ChildrenDataTable(QWidget, Ui_QTableOfData):
    def __init__(self, stocklist):
        super(ChildrenDataTable, self).__init__()
        self.stocklist = stocklist
        self.setupUi(self)
        self.comboBox.addItems(list(self.stocklist.keys()))
        self.themodel = PandasModel(self.stocklist[list(self.stocklist.keys())[0]].reset_index(drop=True))
        self.tableView.setModel(self.themodel)
        self.comboBox.currentIndexChanged.connect(self.set_child_data)

    def set_child_data(self, i):
        self.label.setText("股票代码：" + list(self.stocklist.keys())[i])
        self.label.setFont(QFont("Roman times", 18, QFont.Bold))    # 显示数据
        del self.themodel
        self.themodel = PandasModel(self.stocklist[list(self.stocklist.keys())[i]].reset_index(drop=True))
        self.tableView.reset()
        self.tableView.setModel(self.themodel)


# child window 2: show stat imformation
class ChildrenStat(QWidget, Ui_Stat):
    def __init__(self, stocklist):
        super(ChildrenStat, self).__init__()
        self.setupUi(self)
        self.stocklist = stocklist
        self.CodeBox.addItems(list(self.stocklist.keys()))
        self.CodeBox.currentIndexChanged.connect(self.show_data)
        self.DateSlider.setMinimum(0)
        self.DateSlider.setMaximum(self.get_the_dictvaluelen()-1)
        self.DateSlider.valueChanged.connect(self.show_the_date)
        self.DateSlider.valueChanged.connect(self.show_data)
        self.timeset.clicked.connect(self.show_data)
        self.plotlayout = QGridLayout(self.PlotBox)

    def show_the_date(self):
        self.DataText.setText(str(self.maxlendateL[self.DateSlider.value()]))

    def get_the_dictvaluelen(self):
        maxlen = 0
        for stockcode in list(self.stocklist.keys()):
            if len(self.stocklist[stockcode]) > maxlen:
                maxlencode = stockcode
            maxlen = np.max([len(self.stocklist[stockcode]), maxlen])
        self.maxlendateL = self.stocklist[maxlencode].sort_values(by='Trddt')['Trddt']
        return maxlen

    def show_data(self):
        while self.plotlayout.count():
            child = self.plotlayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        # todo 日期调节处有bug，但具体实现逻辑我还没想好
        the_stock = self.stocklist[self.CodeBox.currentText()].sort_values(by='Trddt').reset_index(drop=True)
        the_stock = the_stock[the_stock['Trddt'] >= self.maxlendateL[self.DateSlider.value()]].reset_index(drop=True)
        the_stock = StockData(the_stock)
        self.MeanPriceLabel.setText(str(format(np.mean(the_stock.clsprc), '0.3f')))
        self.MaxPriceLabel.setText(str(format(np.max(the_stock.clsprc), '0.3f')))
        self.MinPriceLabel.setText(str(format(np.min(the_stock.clsprc), '0.3f')))
        self.StdLabel.setText(str(format(np.std(the_stock.clsprc), '0.3f')))
        self.YieldLabel.setText(str(format(100*(the_stock.clsprc.iloc[-1] / the_stock.clsprc[0] - 1), '0.2f') + '%'))
        tmp_year_yield = 100*(the_stock.clsprc.iloc[-1] / the_stock.clsprc[0] - 1) / ((the_stock.date.iloc[-1] - the_stock.date[0])/pd.to_timedelta('365 days'))
        self.YearYieldLabel.setText(str(format(tmp_year_yield, '0.3f')) + '%')
        tmp_sharp = 100*(the_stock.clsprc.iloc[-1]  / the_stock.clsprc[0] - 1 - 0.02) / np.std(the_stock.clsprc)
        self.SharpLabel.setText(str(format(tmp_sharp, '0.3f')))
        self.F1 = MyFigure(width=5, height=4, dpi=100)
        self.F1.fig.subplots_adjust(hspace=0.4)
        self.F1.axes1 = self.F1.fig.add_subplot(221)
        self.F1.axes1.hist(the_stock.yld)
        self.F1.axes1.set_title("收益率分布")
        self.F1.axes2 = self.F1.fig.add_subplot(222)
        self.F1.axes2.plot(the_stock.clsprc)
        self.F1.axes2.set_title("价格走势")
        self.F1.axes2.set_xticklabels(labels=[])
        self.F1.axes3 = self.F1.fig.add_subplot(223)
        self.F1.axes3.bar(list(range(len(the_stock.date))), the_stock.yld)
        self.F1.axes3.set_title("收益率波动")
        self.F1.axes3.set_xticklabels(labels=[])
        self.F1.axes4 = self.F1.fig.add_subplot(224)
        self.F1.axes4.plot(the_stock.aprc, label='后复权')
        self.F1.axes4.plot(the_stock.bprc, label='前复权')
        self.F1.axes4.set_title("前后复权")
        self.F1.axes4.set_xticklabels(labels=[])

        self.plotlayout.addWidget(self.F1)
        # todo: 控制间隔！


# child window 3: show k line
class ChildrenKline(QWidget, Ui_Kwindow):
    def __init__(self, data):
        super(ChildrenKline, self).__init__()
        self.setupUi(self)
        self.stocklist = data
        self.comboBox.addItems(list(self.stocklist.keys()))
        self.comboBox.currentIndexChanged.connect(self.show_kline)

    def show_kline(self):
        tmp_data = self.stocklist[self.comboBox.currentText()]
        self.plotkthread = KPlotThread(tmp_data)
        self.plotkthread.trigger.connect(self.get_thread_plot)
        self.plotkthread.start()

    def get_thread_plot(self, path):
        self.webEngineView.load(QUrl.fromLocalFile(path))


# child window 4: help
class ChildrenHelp(QWidget, Ui_Help):
    def __init__(self,):
        super(ChildrenHelp, self).__init__()
        self.setupUi(self)

# child window 5: help
class ChildrenMa(QWidget, Ui_Kwindow):
    def __init__(self, data):
        super(ChildrenMa, self).__init__()
        self.setupUi(self)
        self.stocklist = data
        self.comboBox.addItems(list(self.stocklist.keys()))
        self.comboBox.currentIndexChanged.connect(self.show_maline)
    def show_maline(self):
        tmp_data = self.stocklist[self.comboBox.currentText()]
        self.plotmathread = MaPlotThread(tmp_data)
        self.plotmathread.trigger.connect(self.get_thread_plot)
        self.plotmathread.start()

    def get_thread_plot(self, path):
        self.webEngineView.load(QUrl.fromLocalFile(path))

# child window 6: maback
class ChildrenMaback(QWidget, Ui_Maback):
    def __init__(self, data):
        super(ChildrenMaback, self).__init__()
        self.setupUi(self)
        self.stocklist = data
        self.selectlist.addItems(list(self.stocklist.keys()))
        self.stralist.itemChanged.connect(self.start_backtest)
        self.selectlist.itemChanged.connect(self.start_backtest)
        self.stockbtn.clicked.connect(self.show_the_stock)
        self.valuebtn.clicked.connect(self.show_the_value)
        self.the_dict = {}
    def show_the_stock(self):
        if self.the_dict == {}:
            print('False')
            return
        need_data = pd.concat([pd.Series(self.the_dict['opendict']),pd.Series(self.the_dict['posdict']),pd.Series(self.the_dict['closedict'])],
                              axis=1,join='outer')
        need_data.index = self.the_dict['date']
        need_data.columns = ['开仓','持仓','平仓']
        self.newtable = ChildrenTable(need_data)
        self.newtable.show()
    def show_the_value(self):
        if self.the_dict == {}:
            return
        need_data = pd.concat([pd.Series(self.the_dict['yielddict']),pd.Series(self.the_dict['yielddict']).cumsum()],
                              axis=1, join='outer')
        need_data.index = self.the_dict['date']
        need_data.columns = ['日收益','净值']
        self.newtable = ChildrenTable(need_data)
        self.newtable.show()
    def start_backtest(self):
        tmp_stocklist = {}

        self.stralist.update()
        for i in range(self.stralist.count()):
            tmp_stocklist[self.stralist.item(i).text()] = self.stocklist[self.stralist.item(i).text()][self.stocklist[self.stralist.item(i).text()]['Trddt']>=int(self.dateEdit.date().toPyDate().strftime("%Y%m%d"))]
        self.backthread = MaTestThread(tmp_stocklist)
        self.backthread.trigger.connect(self.fill_the_table1)
        self.backthread.start()


    def fill_the_table1(self):
        self.yieldlabel.setText('正在努力计算中')
        self.sharplabel.setText('正在努力计算中')
        self.stdlabel.setText('正在努力计算中')
        self.yearyieldlabel.setText('正在努力计算中')
        self.backlabel.setText('正在努力计算中')
        if self.stralist.count() == 0:
            self.yieldlabel.setText('')
            self.sharplabel.setText('')
            self.stdlabel.setText('')
            self.yearyieldlabel.setText('')
            self.backlabel.setText('')

            return
        tmp_stocklist = {}
        self.stralist.update()
        for i in range(self.stralist.count()):
            tmp_stocklist[self.stralist.item(i).text()] = self.stocklist[self.stralist.item(i).text()][self.stocklist[self.stralist.item(i).text()]['Trddt']>=int(self.dateEdit.date().toPyDate().strftime("%Y%m%d"))]
        self.backthreadnew = MaTestThread(tmp_stocklist)
        self.backthreadnew.trigger.connect(self.fill_the_table)
        self.backthreadnew.start()


    def fill_the_table(self, the_dict):
        self.dateEdit.setMinimumDate(the_dict['mindate'])
        self.dateEdit.setMaximumDate(the_dict['maxdate'])

        self.the_dict = the_dict
        plot_data = pd.Series(the_dict['yielddict'], index=the_dict['date'])
        self.plotyieldthread = MaBackPlotThread(plot_data)
        self.plotyieldthread.trigger.connect(self.get_thread_plot)
        self.plotyieldthread.start()

        if self.stralist.count() == 0:
            self.yieldlabel.setText('')
            self.sharplabel.setText('')
            self.stdlabel.setText('')
            self.yearyieldlabel.setText('')
            self.backlabel.setText('')

            return

        self.yieldlabel.setText(str(format(pd.Series(the_dict['yielddict']).cumsum().iloc[-1]*100 / self.stralist.count(), '0.3f'))+'%')
        self.yearyieldlabel.setText(str(format(pd.Series(the_dict['yielddict']).cumsum().iloc[-1]*100 / self.stralist.count() /
                                        ((the_dict['maxdate'] - the_dict['mindate'])/datetime.timedelta(days=365)), '0.3f'))+'%')
        self.stdlabel.setText(str(format(np.std(pd.Series(the_dict['yielddict'])), '0.4f')))
        self.sharplabel.setText(str(format(pd.Series(the_dict['yielddict']).cumsum().iloc[-1]*100 / self.stralist.count() / np.std(pd.Series(the_dict['yielddict'])), '0.3f'))+'%')
        self.backlabel.setText(str(format(the_dict['max_back']*100, '0.3f'))+'%')

    def get_thread_plot(self, path):
        self.yieldplot.load(QUrl.fromLocalFile(path[0]))
        self.dayplot.load(QUrl.fromLocalFile(path[1]))


class ChildrenTable(QWidget, Ui_tableview):
    def __init__(self,datatable):
        super(ChildrenTable, self).__init__()
        self.setupUi(self)
        self.datatable = datatable
        self.themodel = PandasModel(datatable)
        self.tableView.setModel(self.themodel)
