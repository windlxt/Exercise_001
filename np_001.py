"""
作者：不看盘的量化交易员
日期：2023年04月10日
"""
import pandas as pd
import numpy as np

# ===================================================
# 忽略警告
import warnings
warnings.filterwarnings("ignore")
# 设置 DataFrame 输出格式
pd.set_option('display.max_columns', None)   # 显示完整的列
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.expand_frame_repr', False)  # 设置不折叠数据
pd.set_option('display.max_colwidth', 100)  # 设置每列宽度
pd.set_option('display.float_format', '{:.2f}'.format)  # 设置显示2位小数
pd.reset_option('display.float_format')  # 恢复小数原始设置
# ===================================================
np.set_printoptions(precision=6, linewidth=100, suppress=True)  # numpy 输出设置
# ===================================================

arr1 = np.random.rand(50)
print(type(arr1))
print(arr1)

# =========================================
arr2 = np.random.randint(1, 100, 50)
print(type(arr2))
print(arr2)

# arr3 = arr1 + arr2
arr3 = [i for i in range(1, 21, 1)]
print(arr1 + arr2)
maxindex = np.argmax(arr3)
print("The max number's index is ", maxindex)
print(np.argmax(arr3))
print(np.argmin(arr3))
print(np.argsort(arr3))
print(np.max(arr3))
print(np.sort(arr3))
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++===')

# 五日均线的计算函数
def moving_average(arr, n=5):
    print('arr:', arr)
    res = np.cumsum(arr)
    print('res:', res)
    res[n:] = res[n:] - res[:-n]
    print('res:', res)
    print('res/5:', res/5)
    return res[n-1:]/5

ma5 = moving_average(arr2)
print(ma5)

print('================================')
print(range(1, 21, 1))
print(np.arange(1, 21, 1))
# ===================================================
import matplotlib.pyplot as plt
import matplotlib as mpl

x = np.arange(0, 50, 1)
y = arr2 = np.random.randint(1, 100, 50)
print(y)
data_max = np.max(y)
data_max_index = np.argmax(y)
data_min = np.min(y)
data_min_index = np.argmin(y)
print(data_min, data_min_index, data_max, data_max_index)
text_max = f'[key:{data_max_index}, value:{data_max}]'
text_min = f'[key:{data_min_index}, value:{data_min}]'
# ====================================================
plt.plot(x, y, '--*r')
# plt.plot(x, y, marker='^')
plt.annotate(text_max, (data_max_index, data_max), (data_max_index, data_max+2))
plt.annotate(text_min, (data_min_index, data_min), (data_min_index, data_min-4))


# ========================================================
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 50)
# y = x * x

plt.plot(x, y, marker='o')
for xy in zip(x, y):
    plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), textcoords='offset points')
# plt.show()
# =========================================================
x_average = np.arange(4, 50, 1)
ma5 = moving_average(y)
plt.plot(x_average, ma5)

from matplotlib.font_manager import FontManager
import subprocess
mpl_fonts = set(f.name for f in FontManager().ttflist)
print('all font list get from matplotlib.font_manager:')
for f in sorted(mpl_fonts):
    print('\t' + f)

mpl.rc("font", family='Microsoft YaHei')

plt.title('五日均线图')
plt.savefig('./1.png')
plt.show()


