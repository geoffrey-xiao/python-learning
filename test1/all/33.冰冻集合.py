# 冰冻集合是特殊的集合，一旦定义不能更改，本身是一个强制类型转换的函数

varset = frozenset([1, 2, 3])
print(varset)

for i in varset:
    print(i)

# 冰冻集合推导式
res = frozenset({i << 1 for i in range(6)})
print(res)
