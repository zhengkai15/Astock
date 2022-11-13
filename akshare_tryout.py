# -*- encoding: utf-8 -*-
"""
@File    : akshare_tryout.py
@Time    : 2022/11/13 16:17
@Author  : ZhengKai
@Email   : 156252108@qq.com
@Software: PyCharm
"""


import akshare as ak
import mplfinance as mpf  # Please install mplfinance as follows: pip install mplfinance
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
'''
stock_daily_df = ak.stock_us_daily(symbol="AAPL", adjust="qfq")
stock_daily_df.index = stock_daily_df['date']
print(stock_daily_df.columns)
# print(stock_daily_df.index)
stock_daily_df = stock_daily_df[["open", "high", "low", "close", "volume"]]
stock_daily_df.columns = ["Open", "High", "Low", "Close", "Volume"]
stock_daily_df.index.name = "Date"
stock_daily_df = stock_daily_df.loc["2020-11-01": "2020-11-13"]
mpf.plot(stock_daily_df, type='candle', mav=(3, 6, 9), volume=True, show_nontrading=False)
'''

stock_daily_df = ak.stock_zh_a_hist(symbol="002594", period="daily",  adjust="")
print(stock_daily_df.columns)
stock_daily_df.index = pd.to_datetime(stock_daily_df['日期'])
# print(stock_daily_df.index)
stock_daily_df = stock_daily_df[['开盘',  '最高', '最低','收盘', '成交量']]
stock_daily_df.columns = ["Open", "High", "Low", "Close", "Volume"]
stock_daily_df.index.name = "Date"
stock_daily_df = stock_daily_df.loc["2020-10-01": "2020-11-14"]
# mpf.plot(stock_daily_df, type='candle', mav=(3, 6, 9), volume=True, show_nontrading=True)





# data是测试数据，可以直接下载后读取，在下例中只显示其中100个交易日的数据
plot_data = stock_daily_df
# 读取显示区间最后一个交易日的数据
last_data = plot_data.iloc[-1]
# 设置mplfinance的蜡烛颜色，up为阳线颜色，down为阴线颜色
my_color = mpf.make_marketcolors(up='r',
                                 down='g',
                                 edge='inherit',
                                 wick='inherit',
                                 volume='inherit')
# 设置图表的背景色
my_style = mpf.make_mpf_style(marketcolors=my_color,
                              figcolor='(0.82, 0.83, 0.85)',
                              gridcolor='(0.82, 0.83, 0.85)')
# 使用mpf.figure()函数可以返回一个figure对象，从而进入External Axes Mode，从而实现对Axes对象和figure对象的自由控制
fig = mpf.figure(style=my_style, figsize=(12, 8), facecolor=(0.82, 0.83, 0.85))
# 添加三个图表，四个数字分别代表图表左下角在figure中的坐标，以及图表的宽（0.88）、高（0.60）
ax1 = fig.add_axes([0.06, 0.25, 0.88, 0.60])
# 添加第二、三张图表时，使用sharex关键字指明与ax1在x轴上对齐，且共用x轴
ax2 = fig.add_axes([0.06, 0.15, 0.88, 0.10], sharex=ax1)
ax3 = fig.add_axes([0.06, 0.05, 0.88, 0.10], sharex=ax1)

# 设置三张图表的Y轴标签
ax1.set_ylabel('price')
ax2.set_ylabel('volume')
ax3.set_ylabel('macd')

# 调用mpf.plot()函数，注意调用的方式跟上一节不同，这里需要指定ax=ax1，volume=ax2，将K线图显示在ax1中，交易量显示在ax2中
mpf.plot(plot_data,
		 ax=ax1,
		 volume=ax2,
		 type='candle',
		 style=my_style)
fig.show()
