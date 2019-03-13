# Billion-Quantitative-Investing
Quantitative Investing Tool

EasyQuant是作者借学校量化投资课而自行开发的量化Windows小程序，程序的初衷是对PyQt5进行练习，同时实现一些小功能满足个人的日常需要，由于这是作者第一次开发程序，也没有系统学习过软件开发的相关课程，一切都在一点一点摸索，因此程序中难免出现一些Bug和不完善的地方，希望您能谅解。

## 主界面
![image](https://github.com/huoyongkang/Billion-Quantitative-Investing/blob/master/images/1.jpg)

## 功能

### 文件

通过文件通道可以读取和保存文件，读取文件格式为csv，字段需要符合国泰安数据库的股票数据文件，在example文件夹下上传了一个样例文件。
![image](https://github.com/huoyongkang/Billion-Quantitative-Investing/blob/master/images/2.jpg)
通过保存，可以将csv中不同股票分开保存，每一个单独保存成一个csv文件。
![image](https://github.com/huoyongkang/Billion-Quantitative-Investing/blob/master/images/3.jpg)


### 行情

数据提供了对原始数据的浏览功能：
![image](https://github.com/huoyongkang/Billion-Quantitative-Investing/blob/master/images/4.jpg)

统计提供了简单统计指标的展示：
![image](https://github.com/huoyongkang/Billion-Quantitative-Investing/blob/master/images/5.jpg)


K线提供了股票K线图的绘制，利用Plotly库实现
![image](https://github.com/huoyongkang/Billion-Quantitative-Investing/blob/master/images/6.jpg)

### 指标

目前只提供了均线指标的图形查看
![image](https://github.com/huoyongkang/Billion-Quantitative-Investing/blob/master/images/7.jpg)

### 策略

策略部分，由于时间问题，目前只实现了5日、10日均线的金叉死叉策略。提供了多股查询，以及每日持仓和净值的查看。
![image](https://github.com/huoyongkang/Billion-Quantitative-Investing/blob/master/images/8.jpg)

## 帮助

帮助部分提供了数据字段要求

## 说明

由于时间关系，所以程序实现较为仓促，许多功能尚未实现，希望在未来的版本中能够对已知的问题进行修改以及对未来功能的追加。
