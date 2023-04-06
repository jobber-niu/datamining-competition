import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
# 基本库

df = pd.read_csv('./示例数据/order_train0.csv')
df.head(5)
df.info()
df['order_date'] = pd.to_datetime(df['order_date'])

plt.figure(figsize=(10,5))
print(df.item_price.describe())
plt.subplot(1,2,1)
plt.plot(df['order_date'],df['item_price'])
print(df.ord_qty.describe())
plt.subplot(1,2,2)
plt.plot(df['order_date'],df['ord_qty'])
plt.show()

dirc = {'offline':0,'online':1}
df['sales_chan_name'].replace(dirc,inplace = True)

# 更新