# 1.列表 的长度 len()

varlist = [4, 5, 2, 9, 6, 7, 4, 8]
# res = len(varlist)
# print(res)

# 2.添加元素 append()
# varlist.append(10)
# print(varlist)

# 3.添加元素 insert()
# varlist.insert(1,22)
# print(varlist)

# 4.删除元素 remove()
# varlist.remove(5)
# print(varlist)

# pop() 列表中弹出某个元素 出栈
# res = varlist.pop(2)
# print(res,varlist)

# 5.reverse() 逆转列表里的元素
# varlist.reverse()
# print(varlist)

# 6.copy() 复制列表 复制的列表里如果包含iterable 修改这个列表里的iterable会影响另一个列表
varlist.append([99, 88, 77, 66])
# res = varlist.copy()
# res[-1][0] = 1111
# print(res, varlist)

# 7.深拷贝和浅拷贝
import copy

res = copy.deepcopy(varlist)
res[-1][0] = 1111
print(res, varlist)