vardict = {'a': 1, 'b': 2, 'c': 3}

res = len(vardict)

res = 'a' in vardict
# res = vardict.pop('a')
# res = vardict.popitem() 先进后出原则

# res = vardict.update(a=5555) 有的话会更新字典项 没有的话会追加
res = vardict.update({'d': 'summer'})
print(res)
print(vardict)
