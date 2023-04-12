"""
作者：不看盘的量化交易员
日期：2023年04月10日
"""
import numpy as np
import pandas as pd

columns = ['date', 'open', 'high', 'low', 'close']
date = pd.date_range(start='20230101', end='20230331', freq='d')
print(date)
num = len(date)
def data_gen(size = num, high_price=20, low_price=15):
    data1 = np.random.rand(size)
    data2 = np.random.randint(size)
    data3 = data1 + data2
    return data3


if __name__ == '__main__':
    open = data_gen(high_price=22, low_price=20)
    high = data_gen(high_price=25, low_price=23)
    low = data_gen(high_price=20, low_price=18)
    close = data_gen(high_price=23, low_price=19)

    df_stock = pd.DataFrame(columns=columns)
    print(df_stock)
    df_stock['date'] = date
    df_stock['open'] = open
    df_stock['high'] = high
    df_stock['low'] = low
    df_stock['close'] = close

    print(df_stock)







