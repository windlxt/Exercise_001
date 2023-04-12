"""
作者：不看盘的量化交易员
日期：2023年04月10日
"""
import numpy as np
arr = [ i for i in range(1, 21, 1)]
# 五日均线的计算函数
def moving_average(arr, n=5):
    print('arr:', arr)
    res = np.cumsum(arr)
    print('res:', res)
    res[n:] = res[n:] - res[:-n]
    print('res:', res)
    print('res/5:', res/5)
    return res[n-1:]/5

ma5 = moving_average(arr)
print(ma5)
print(ma5)
