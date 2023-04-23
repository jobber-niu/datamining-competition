'''
数据拆分 定义一个时间序列模型
将不同维度的数据导入来建模
{
    一个地区一种大类一个维度
}
预测时，他妈的怎么预测啊。！？
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import datetime
import time

pd.set_option('display.width', 300)  # 设置字符显示宽度
pd.set_option('display.max_rows', None)  # 设置显示最大行
pd.set_option('display.max_columns', None)

'''===========读入处理过的数据============='''
changed_data = pd.read_excel('./处理过的数据/changed_data.xlsx')
# changed_data = changed_data.dropna(subset=['sales_region_code'])
changed_data.head(5)  # 看看表头


'''==========将不同地区的数据分开==========='''
region_names = changed_data['sales_region_code'].drop_duplicates(keep="first")
# region_names = region_names['0']

'''------出现读出表格均为空表的问题，遂放弃------
for region_name in region_names:
    exec("data_{} = changed_data.query('sales_region_code == \"{}\"')".format(region_name, region_name))'''
# 查询数据
data_101 = changed_data.query("sales_region_code == 101")
data_102 = changed_data.query("sales_region_code == 102")
data_103 = changed_data.query("sales_region_code == 103")
data_104 = changed_data.query("sales_region_code == 104")
data_105 = changed_data.query("sales_region_code == 105")
# print(data_101.head(10),data_101.tail(10))
# data_101.to_excel('./101地区数据看价格与销售关系.xlsx',index=False)

# 建个文件夹放数据
if not os.path.exists('./不同地区数据'):
    os.mkdir('./不同地区数据')
# 输出为csv文件
data_101.to_csv('./不同地区数据/101地区数据看价格与销售关系.csv',index=False)
data_102.to_csv('./不同地区数据/102地区数据看价格与销售关系.csv',index=False)
data_103.to_csv('./不同地区数据/103地区数据看价格与销售关系.csv',index=False)
data_104.to_csv('./不同地区数据/104地区数据看价格与销售关系.csv',index=False)
data_105.to_csv('./不同地区数据/105地区数据看价格与销售关系.csv',index=False)

'''========读入文件======'''
# file_names = os.listdir('./不同地区数据')
# # print(file_names)
# for i,file_name in zip(range(1,6),file_names):
#     # data{}. = pd.read_excel(file_name)
#     exec("data{} = pd.read_csv('./不同地区数据/' + file_name)".format(i))

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
# print(data_dict['data1'].head())

'''-------新的分类——将大类分出来--------'''
'''data1 = data_dict['data1']
data_101_301 = data1.query("first_cate_code == 301")
data_101_302 = data1.query("first_cate_code == 302")
data_101_303 = data1.query("first_cate_code == 303")
data_101_304 = data1.query("first_cate_code == 304")
data_101_305 = data1.query("first_cate_code == 305")
data_101_306 = data1.query("first_cate_code == 306")
data_101_307 = data1.query("first_cate_code == 307")
data_101_308 = data1.query("first_cate_code == 308")
data2 = data_dict['data2']
data_102_301 = data1.query("first_cate_code == 301")
data_102_302 = data1.query("first_cate_code == 302")
data_102_303 = data1.query("first_cate_code == 303")
data_102_304 = data1.query("first_cate_code == 304")
data_102_305 = data1.query("first_cate_code == 305")
data_102_306 = data1.query("first_cate_code == 306")
data_102_307 = data1.query("first_cate_code == 307")
data_102_308 = data1.query("first_cate_code == 308")'''
data1 = data_dict['data1']
data2 = data_dict['data2']
data3 = data_dict['data3']
data4 = data_dict['data4']
data5 = data_dict['data5']
# 创建一个字典来存储数据
data_dict_new = {}

# 定义需要查询的分类码
first_cate_codes = [301, 302, 303, 304, 305, 306, 307, 308]
first_cate_codes_d = [301, 304, 307, 308]

# 循环查询数据并存储到字典中

for code in first_cate_codes:
    data_dict_new[f"data_101_{code}"] = data1.query(f"first_cate_code == {code}")
    data_dict_new[f"data_102_{code}"] = data2.query(f"first_cate_code == {code}")
    data_dict_new[f"data_103_{code}"] = data3.query(f"first_cate_code == {code}")
    data_dict_new[f"data_105_{code}"] = data5.query(f"first_cate_code == {code}")

for code in first_cate_codes_d:
    data_dict_new[f"data_104_{code}"] = data4.query(f"first_cate_code == {code}")

'''导出不同大类的数据'''
for i in range(101,106):
    path = './不同地区数据/'+str(i)+'地区不同大类'
    if not os.path.exists(path):
        os.mkdir(path)






'''=============开始分析！！=============='''

'''i = 1
for i in data_dict:
    # print(i)
    df = data_dict[i]
    df = data_dict['data5']
    ax = sns.scatterplot(x='item_price',y='ord_qty',data=df)
    plt.show(ax)
    time.sleep(5)'''



