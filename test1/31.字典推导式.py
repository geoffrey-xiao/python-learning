# 字典键值对互换
vardict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

newdict = {
}
# 普通方法
# for k, v in vardict.items():
#     newdict[v] = k
# 字典推导式
# newdict = {v: k for k, v in vardict.items()}

# 判断如果是偶数的话键值对互换

newdict = {v: k for k, v in vardict.items() if v % 2 == 0}
print(newdict)
