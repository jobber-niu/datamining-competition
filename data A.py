import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
# 基本库

'''读取数据'''
origin_data = pd.read_csv('./B题-全部数据/order_train1.csv')
# df.head(5)
# df.info()
data_frame = origin_data[['item_price','ord_qty']].describe()
'''箱线图法剔除异常值'''
up = data_frame.loc['75%'] -1.5*(data_frame.loc['75%']-data_frame.loc['25%'])
down = data_frame.loc['75%'] +1.5*(data_frame.loc['75%']-data_frame.loc['25%'])

'''查看最大销量所在行以及附近的数据'''
'''i = 0
for i,j in zip(range(60000),origin_data['ord_qty']):
    if j == 12480:
        print(i)
    i = i + 1
# i = 33232
print(origin_data.loc[33232 - 5:33232 + 5,:])'''

'''将时间由object转换为datetime（ns）格式'''
origin_data['order_date'] = pd.to_datetime(origin_data['order_date'])
'''将购买方式替换为0-1'''
# dir = {'offline':0,'online':1}
# origin_data['sales_chan_name'].replace(dir,inplace=True)
'''删除重复值'''
changed_data = origin_data.drop_duplicates(subset=None,keep = 'first')
# print(origin_data.shape,changed_data.shape)
# 删除三条重复数据
'''删除异常值'''
# print(down.loc['item_price'])
dic_1 = {}
dic_2 = {}
for i,j in zip(changed_data['item_price'],changed_data['ord_qty']):
    if i > down.loc['item_price'] or i < up.loc['item_price']:
        dic_1[i] = None
    if j > down.loc['ord_qty'] or j < up.loc['ord_qty']:
        dic_2[j] = None
# print(dic_1,dic_2)
# changed_data[['item_price','ord_qty']] = changed_data[['item_price','ord_qty']].replace((dic_1,dic_2))
changed_data['item_price'] = changed_data['item_price'].replace(dic_1)
changed_data['ord_qty'] = changed_data['ord_qty'].replace(dic_2)

'''用平均值代替吧？？'''
# p = changed_data['item_price']
# q = changed_data['ord_qty']
# p.dropna(inplace = True)
# q.dropna(inplace = True)
# p_mean = np.mean(p)
# q_mean = np.mean(q)

def mean_to_change(x):
    need = changed_data[x]
    need.dropna(inplace = True)
    mean = np.mean(need)
    return mean
p_mean = mean_to_change('item_price')
q_mean = int(mean_to_change('ord_qty'))

changed_data['item_price'].fillna(p_mean,inplace = True)
changed_data['ord_qty'].fillna(q_mean,inplace = True)

'''计算营业额'''
changed_data['account'] = changed_data['item_price'] * changed_data['ord_qty']

import os
if not os.path.exists('./处理过的数据'):
    os.mkdir('./处理过的数据')
elif os.path.exists('./处理过的数据'):
    print("############################################################")
changed_data.to_csv('./处理过的数据/changed_data.csv',index=False)

# 更新