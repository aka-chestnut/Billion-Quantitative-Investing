import sys
import numpy as np
import sip
from WindowClass import *
import pandas as pd
import datetime
import copy
from PyQt5.QtWidgets import *
from WindowClass import *
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


class Plotly_PyQt5():
    def __init__(self, data=0):
        plotly_dir = 'plotly_html'
        if not os.path.isdir(plotly_dir):
            os.mkdir(plotly_dir)
        self.data = data
        self.path_dir_plotly_html = os.getcwd() + os.sep + plotly_dir

    def plotK(self, file_name='Kline.html'):
        tmp_date = self.data['Trddt']
        tmp_date = tmp_date.map(lambda x: datetime.datetime.strptime(str(x), '%Y%m%d'))
        path_plotly = self.path_dir_plotly_html + os.sep + file_name
        trace = go.Candlestick(x=tmp_date,
                               open=self.data['Opnprc'],
                               high=self.data['Hiprc'],
                               low=self.data['Loprc'],
                               close=self.data['Clsprc'],
                               name='Price',
                               increasing=dict(line=dict(color='#FF0000')),
                               decreasing=dict(line=dict(color='#00FF00')))

        data = [trace]
        layout = {
            'title': 'K线图'}
        fig = dict(data=data, layout=layout)
        pyof.plot(fig, filename=path_plotly, auto_open=False)
        return path_plotly

class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure, self).__init__(self.fig)


# 画图类
class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=200):
        self.fig = Figure(figsize=(width, height), dpi=dpi, frameon=False)
        super(MyFigure, self).__init__(self.fig) #此句必不可少，否则不能显示图形


# Stock Data Class
class StockData:

    def __init__(self, data_frame):
        self.initdata = data_frame
        self.stockID = data_frame['Stkcd'][0]
        self.date = pd.to_datetime(data_frame['Trddt'], format='%Y%m%d')
        self.clsprc = data_frame['Clsprc']
        self.opnprc = data_frame['Opnprc']
        self.hiprc = data_frame['Hiprc']
        self.loprc = data_frame['Loprc']
        self.aprc = self.clsprc / self.clsprc.iloc[-1]
        self.bprc = self.clsprc / self.clsprc.iloc[0]
        self.yld = self.clsprc / self.opnprc - 1

    def __len__(self):
        return len(self.clsprc)


class FileSaveThread(QThread):
    trigger = pyqtSignal()

    def __init__(self, filenames, datadict):
        super(FileSaveThread, self).__init__()
        self.filenames = filenames
        self.stocklist = datadict

    def run(self):
        for key in list(self.stocklist.keys()):
            self.stocklist[key].reset_index(drop=True).to_csv(self.filenames[0] + '/' + key + '.csv')
        self.trigger.emit()


# File Read Thread
class FileReadThread(QThread):
    trigger = pyqtSignal(dict)

    def __init__(self, filenames):
        super(FileReadThread, self).__init__()
        self.filenames = filenames
        self.stocklist = {}

    def run(self):
        try:
            self.data = pd.read_csv(self.filenames[0], encoding='utf-8')
            self.data.drop_duplicates(inplace=True)
        except:  # If the dataframe error, then MessageBox
            QMessageBox.information(self, "ListWidget", "数据格式不正确，请查阅帮助文档获得使用方法！")
        finally:
            stock_codes = self.data['Stkcd'].unique()
            for stock_code in stock_codes:
                tmp_table = self.data[self.data['Stkcd'] == stock_code]
                tmp_table = tmp_table.sort_values(by='Trddt').reset_index(drop=True)
                self.stocklist[format(str(stock_code), '0>6')] = tmp_table
            self.trigger.emit(self.stocklist)

class Plotly_Maback():
    def __init__(self, data=0):
        plotly_dir = 'plotly_html'
        if not os.path.isdir(plotly_dir):
            os.mkdir(plotly_dir)
        self.data = data
        self.path_dir_plotly_html = os.getcwd() + os.sep + plotly_dir
    def plotyield(self, file_name='Kline1.html'):
        path_plotly = self.path_dir_plotly_html + os.sep + file_name
        data = [go.Bar(
            x=list(self.data.index),
            y=self.data
        )]
        layout = dict(
            title='日收益率波动',
        )
        fig = dict(data=data, layout=layout)
        pyof.plot(fig, filename=path_plotly, auto_open=False)
        return path_plotly

    def plotcumyield(self, file_name='Kline2.html'):
        path_plotly = self.path_dir_plotly_html + os.sep + file_name
        data = [go.Scatter(x=list(self.data.index),y=self.data.cumsum())]
        layout = dict(
            title='净值图',
        )
        fig = dict(data=data, layout=layout)
        pyof.plot(fig, filename=path_plotly, auto_open=False)
        return path_plotly

class MaBackPlotThread(QThread):
    trigger = pyqtSignal(list)

    def __init__(self, stockseries):
        super(MaBackPlotThread, self).__init__()
        self.stockseries = stockseries

    def run(self):
        self.plotly_maback = Plotly_Maback(self.stockseries)
        self.trigger.emit([self.plotly_maback.plotyield(),self.plotly_maback.plotcumyield()])
# 多线程K线
class KPlotThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self, stocktable):
        super(KPlotThread, self).__init__()
        self.stocktable = stocktable

    def run(self):
        self.plotly_kline = Plotly_PyQt5()
        self.plotly_kline = Plotly_PyQt5(self.stocktable)
        self.trigger.emit(self.plotly_kline.plotK())

class Plotly_MA():
    def __init__(self, data=0):
        plotly_dir = 'plotly_html'
        if not os.path.isdir(plotly_dir):
            os.mkdir(plotly_dir)
        self.data = data
        self.path_dir_plotly_html = os.getcwd() + os.sep + plotly_dir

    def plotma(self, file_name='Kline.html'):
        self.data['Trddt'] = self.data['Trddt'].map(lambda x: datetime.datetime.strptime(str(x), '%Y%m%d'))
        params = [5, 10, 20]
        for p in params:
            self.data['ma' + str(p)] = self.data['Clsprc'].rolling(window=p).mean()
        self.data.dropna(inplace=True, how='any')
        path_plotly = self.path_dir_plotly_html + os.sep + file_name
        trace = go.Candlestick(x=self.data['Trddt'],
                               open=self.data['Opnprc'],
                               high=self.data['Hiprc'],
                               low=self.data['Loprc'],
                               close=self.data['Clsprc'],
                               name='price',
                               increasing=dict(line=dict(color='#FF0000')),
                               decreasing=dict(line=dict(color='#00FF00')))
        ma5 = go.Scatter(
            x=self.data['Trddt'],
            y=self.data['ma5'],
            name="MA5",
            line=dict(color='#FFFF00'),
            opacity=0.8)
        ma10 = go.Scatter(
            x=self.data['Trddt'],
            y=self.data['ma10'],
            name="MA10",
            line=dict(color='#00BFFF'),
            opacity=0.8)
        ma20 = go.Scatter(
            x=self.data['Trddt'],
            y=self.data['ma20'],
            name="MA20",
            line=dict(color='#696969'),
            opacity=0.8)
        data = [trace, ma5, ma10, ma20]
        layout = dict(
            title='均线图',
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label='1m',
                             step='month',
                             stepmode='backward'),
                        dict(count=6,
                             label='6m',
                             step='month',
                             stepmode='backward'),
                        dict(step='all')
                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
                type='date'
            )
        )
        fig = dict(data=data, layout=layout)
        pyof.plot(fig, filename=path_plotly, auto_open=False)
        return path_plotly

class MaPlotThread(QThread):
    trigger = pyqtSignal(str)

    def __init__(self, stocktable):
        super(MaPlotThread, self).__init__()
        self.stocktable = stocktable

    def run(self):
        self.plotly_maline = Plotly_MA()
        self.plotly_maline = Plotly_MA(self.stocktable)
        self.trigger.emit(self.plotly_maline.plotma())

class MaTestThread(QThread):
    trigger = pyqtSignal(dict)
    def __init__(self, stocklist):
        super(MaTestThread, self).__init__()
        self.stocklist = copy.deepcopy(stocklist)
        for stockcode in list(self.stocklist.keys()):
            self.stocklist[stockcode]['Trddt'] = self.stocklist[stockcode]['Trddt'].map(lambda x: datetime.datetime.strptime(str(x), '%Y%m%d'))
        self.newlist = {}
        self.the_dict = {}
    def run(self):
        for stockcode in list(self.stocklist.keys()):
            params = [5, 10]
            for p in params:
                self.stocklist[stockcode]['ma' + str(p)] = self.stocklist[stockcode]['Clsprc'].rolling(window=p).mean()
            self.stocklist[stockcode].dropna(inplace=True, how='any')
            self.stocklist[stockcode].reset_index(drop=True, inplace=True)
            self.newlist[stockcode] = self.get_middle_dict(self.stocklist[stockcode])
        mindatelist = [0 for _ in range(len(self.newlist))]
        maxdatelist = [0 for _ in range(len(self.newlist))]
        i_count = 0
        for stockcode in list(self.newlist.keys()):
            i_count += 1
            mindatelist[i_count-1] = self.newlist[stockcode]['date'][0]
            maxdatelist[i_count-1] = self.newlist[stockcode]['date'].iloc[-1]
        self.the_dict['mindate'] = np.min(mindatelist)
        self.the_dict['maxdate'] = np.max(maxdatelist)
        stock_code = pd.Series(list(self.newlist.keys()))
        sigtable = pd.concat([pd.Series(list(x['sig']), index=list(x['date'])) for x in self.newlist.values()], axis=1, join='outer')
        yieldtable = pd.concat([pd.Series(list(x['yield']), index=list(x['date'])) for x in self.newlist.values()], axis=1, join='outer')
        opendict = {}
        closedict = {}
        posdict = {}
        yielddict = {}
        count_i = 0
        for date in list(sigtable.index):

            opendict[date] = list(stock_code[list(sigtable.iloc[count_i] == 1)])
            closedict[date] = list(stock_code[list(sigtable.iloc[count_i] == 3)])
            posdict[date] = list(stock_code[list(sigtable.iloc[count_i] == 2)])
            yielddict[date] = np.sum(yieldtable.iloc[count_i])
            count_i += 1
        self.the_dict['date'] = list(sigtable.index)
        self.the_dict['opendict'] = opendict
        self.the_dict['closedict'] = closedict
        self.the_dict['posdict'] = posdict
        self.the_dict['yielddict'] = yielddict
        self.the_dict['max_back'] = self.get_the_biggest_back(pd.Series(yielddict).cumsum())
        # 返回的字典包括
            # 1. 最小日期
            # 2. 最大日期
            # 3. 字典：每天的持仓
            # 4. 字典：每天的开仓
            # 5. 字典：每天的平仓
            # 6. 字典：每天的收益


        self.trigger.emit(self.the_dict)
    # 等金额股票
    def get_the_biggest_back(self, the_series):
        max_back = 0
        for i in range(len(the_series)):
            j = i + 1
            while j < len(the_series):
                max_back = np.min([the_series[j]-the_series[i],max_back])
                j += 1
        return max_back

    def get_middle_dict(self,mtable):
        stockamount = 0
        buy_sig = 0
        datelist = list(mtable['Trddt'])
        pricelist = list(mtable['Clsprc'])
        mystockvalue = [0 for _ in range(len(mtable))]
        siglist = [0 for _ in range(len(mtable))]
        mystockyield = [0 for _ in range(len(mtable))]
        for i in range(len(mtable)):
            #siglist 0 空仓 1 买入 2 持有 3 卖出
            if buy_sig==0:
                if mtable['ma5'][i]>=mtable['ma10'][i]:
                    buy_sig = 1
                    siglist[i] = 1
                    mystockvalue[i] = 100
                    stockamount = 100 / mtable['Clsprc'][i]
                    mystockyield[i] = 0
                    continue
                siglist[i] = 0
                mystockvalue[i] = 0
                mystockyield[i] = 0
                continue
            elif buy_sig==1:
                if mtable['ma5'][i]<=mtable['ma10'][i]:
                    buy_sig = 0
                    siglist[i] = 3
                    mystockvalue[i] = stockamount * mtable['Clsprc'][i]
                    mystockyield[i] = mystockvalue[i] / mystockvalue[i-1] - 1
                    mystockvalue[i] = 0
                    continue
                siglist[i] = 2
                mystockvalue[i] = stockamount * mtable['Clsprc'][i]

                mystockyield[i] = mystockvalue[i] / mystockvalue[i - 1] - 1

                continue

        return pd.DataFrame([datelist, pricelist, siglist, mystockvalue, mystockyield], index=['date', 'price', 'sig', 'value', 'yield']).T




