import matplotlib.pyplot as plt
import matplotlib.font_manager
import pandas as pd

plt.rcParams['font.family'] = ['Arial Unicode MS']  # 设置可以显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
# a=sorted(([f.name for f in matplotlib.font_manager.fontManager.ttflist]))
# for i in a:
#     print(i)

olpc = pd.read_csv('Tokyo 2021 dataset.csv')
# print(olpc.info())
top5 = olpc[olpc.Rank <= 5]
top5.rename(columns={'Team/NOC': 'Team'}, inplace=True)
# print(top5)

# plt.figure()
# plt.plot(top5['NOCCode'],top5['Gold Medal'])
# plt.show()

plt.figure()
plt.bar(top5['NOCCode'], top5['Gold Medal'])
# plt.show()

plt.figure()
plt.barh(top5['NOCCode'], top5['Gold Medal'])

plt.figure()
plt.pie(top5['Gold Medal'])

plt.figure()
plt.scatter(top5['NOCCode'], top5['Gold Medal'])

plt.figure()
plt.hist(top5['Gold Medal'], bins=5)

plt.figure()
plt.plot(top5['NOCCode'], top5['Gold Medal'])
plt.ylim(20, 40)

plt.figure()
plt.plot(top5['NOCCode'], top5['Gold Medal'])
plt.xlabel('国家简称')
plt.ylabel('金牌数目')

plt.figure()
plt.plot(top5['NOCCode'], top5['Gold Medal'], label='金牌数目')
plt.legend()

plt.figure()
plt.plot(top5['NOCCode'], top5['Gold Medal'])
for x, y in zip(top5['NOCCode'], top5['Gold Medal']):
    plt.text(x, y + 0.1, '%d' % y, ha='center', va='bottom')
plt.show()
