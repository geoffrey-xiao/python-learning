'''
json javascript object notation 是受javascript启发的轻量级数据交换格式
json.dumps() 将数据转为json格式
json.loads() 将json格式的数据转为一般数据
'''
import json

vardict = {'name': 'fengfeng', 'age': 18, 'sex': 'male'}
varlist = [1, 2, 3]
# res = json.dumps(varlist)
# print(res, type(res))

# json格式 写入/读取文件

# with open('./json1.txt', 'w') as fp:
#     json.dump(vardict, fp)

with open('./json1.txt','r') as fp:
    newres = json.load(fp)
print(newres)