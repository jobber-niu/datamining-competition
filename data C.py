
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
def B():
    path = './不同地区数据'
    file_names = os.listdir(path)

    # 将所有数据表读入到一个字典中，键为 data1 到 data5
    data_dict = {}
    for i, file_name in zip(range(1, 6), file_names):
        df = pd.read_csv(os.path.join(path, file_name))
        data_dict["data{}".format(i)] = df
        time.sleep(2)
    return  data_dict
data_dict = B()

# 现在，您可以使用 data_dict['data1']，data_dict['data2'] 等等来引用每个数据表
print(data_dict['data1'].head())

'''=============开始分析！！=============='''
# pycharm 出不了图。。
'''i = 1
for i in data_dict:
    # print(i)
    df = data_dict[i]
    sns.scatterplot(x='item_price',y='ord_qty',data=df)
    time.sleep(5)'''