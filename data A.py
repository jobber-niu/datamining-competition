import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

d = pd.read_csv('./示例数据/order_train0.csv')
d.head(5)
# d.iloc[:,0:1]
d.query("sales_region_code == 101")
d.info()
c = d['item_price']
max(c)
print(d.sales_region_code.unique())
print(d['item_code'].unique().size)

s = sum(d['item_price'])
print(s)
print(d['item_price']/s)