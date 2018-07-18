#!/usr/bin/python
# -*- coding: utf-8 -*-
import tushare as ts
import time


def download_data():
    """"""
    stock_dict = ['300647', '300745', '002908', '603486']
    datas = ts.get_realtime_quotes(stock_dict)
    try:
        for indexs in datas.index:
            data = datas.loc[indexs]
            name = data[0]
            current_price = data[3]
            last_price = data[2]
            buy_1 = data[10]
            temp = ((float(current_price) - float(last_price)) /
                    float(last_price))*100
            print('{}, {}，{}，{}'.format(
                name, current_price, '%.2f' % temp+'%', buy_1))
    except Exception as e:
        print("执行异常")


while True:
    download_data()
    time.sleep(10)
    print('\n-------------------------------------------------\n')
