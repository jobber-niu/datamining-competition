
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import datetime
import time

pd.set_option('display.width', 300)  # 设置字符显示宽度
pd.set_option('display.max_rows', None)  # 设置显示最大行
pd.set_option('display.max_columns', None)

'''========读入文件======'''
path_1 = './不同地区数据/'
file_names = os.listdir(path_1)
l = []
for i in range(0,10,2):
    l.append(i)
file_names_1 = []
for i in l:
    file_names_1.append(file_names[i])

for file_name in file_names_1:
    path_2 = path_1 + file_name + '/'
    file_names = os.listdir(path_2)
    for name in file_names:
        exec('df_{} = pd.read_excel(path_2 + name)'.format(name))

        # 不太清楚是否正确
        ax = sns.scatterplot(x = 'item_price',y = 'ord_qty')
        plt.savefig(path_1)


