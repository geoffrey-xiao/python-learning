vardict = {'a': 1, 'b': 2, 'c': 3}

vardict = dict(name='summer', age=3, sex='female')

vardict = dict([['name', 'fengfeng'], ['age', 25], ['sex', 'male']])

var1 = ['a', 'b', 'c']
var2 = [1, 2, 3]

vardict = dict(zip(var1, var2))

res = len(vardict)
# print(vardict)
# print(res)

# 修改字典
vardict['name'] = 'leilei'
# 添加字典项 添加重复的key会被覆盖
vardict['height'] = '180'
# 删除字典项
# del vardict['height']
res = vardict.keys()
res = vardict.values()
res = vardict.items()
print(vardict)
print(res)
