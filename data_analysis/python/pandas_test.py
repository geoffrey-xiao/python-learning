import pandas as pd
import numpy as np

eva = {'summer': 0, 'leilei': 1}
eva_s = pd.Series(eva)
# print(eva_s)
# print(eva_s.values)
# print(eva_s.index)
# print(eva_s[0:1])
# eva_s==0
# print(eva_s[eva_s==0])

cpc = pd.read_csv('./cpc.csv', sep=',', encoding='gbk')
# print(cpc)
pd.Series(pd.unique((cpc['平台门店名称'])))
# print(cpc)
cpc['符号'] = '%'
cpc['下单率'] = (round(cpc.门店下单量 / cpc.门店访问量, 1) * 100).map(str).str.cat(cpc.符号)
# print(cpc[['平台门店名称','下单率']])

# res = cpc.query('gmvroi>7.0&gmvroi<8.0')[['门店ID','平台门店名称']]
# print(res)

# res1 = cpc[['门店ID','平台门店名称']][cpc.gmvroi.isin([7.0,8.0])]
# print(res1)

# res2 = cpc[['门店ID','平台门店名称','门店实收']][cpc.门店实收.isnull()]
# print(res2)

# res3 = cpc['平台门店名称'][cpc.平台门店名称.str.contains('宝山')].unique()
# print(pd.Series(res3))

# 聚合函数
# res4 = cpc.groupby('平台门店名称').agg(平均实收=('门店实收','mean'))
# print(res4)

# res5 = cpc.groupby('平台门店名称').agg(总和=('门店实收','sum')).query('总和>10000').sort_values(by='总和',ascending=False)
# print(res5)

# store = cpc[cpc.平台门店名称.str.contains('武宁路')]
# store.groupby(cpc.平台门店名称).agg(实收=('门店实收','sum')).sort_values(by='实收',ascending=False)
# print(store)

# limit
# res6 = cpc[5:10]
# print(res6)

# res7=cpc.loc[:5,'平台门店名称']
# print(res7)

# 子查询
# storeid = cpc.query('门店实收>1000').门店ID
# store = cpc['平台门店名称'][cpc['门店ID'].isin(storeid)].unique()
# print(pd.Series(store))

# 表连接
# shop = pd.read_csv('./shop.csv',encoding='gbk')
# m = pd.merge(cpc,shop,left_on=['门店ID','日期'],right_on=['门店ID','日期'],how='inner')
# res = m.groupby(['门店名称']).agg(门店实收=('门店实收','sum'))
# print(res)

# cpc['rank']=cpc.groupby('日期')['门店实收'].rank(method="min",ascending=False)
# cpc.sort_values(by=['日期','门店实收'],ascending=[True,False])[['日期','平台门店名称','门店实收','rank']]
# cpc['rank']=cpc.groupby(['日期','平台i'])['门店实收'].rank(method='min',ascending=False)
# print(cpc)

# excel数据透视表
# table = pd.pivot_table(cpc,values=['门店实收','cpc总费用'],index=['平台门店名称'],columns=['平台i'],aggfunc=np.sum).fillna(0)
# print(table)

# 数据探索处理
df = pd.read_csv('./cpc.csv', encoding='gbk')
# print(df.info())
# print(df.head(10))
# print(df.describe())
