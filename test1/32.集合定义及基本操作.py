# 1.集合是无序的 数据集合 用{}或者set定义，集合中的元素不能重复
# 2.在集合中True等于1，False等于0，随机出现，不能重复

varset = {123, 'a', 'b', 'c', True, ('g', 'k', 'l')}
# res = len(varset)
# res = 'ggg' in varset

# 向集合添加元素
res = varset.add('summer')
# 删除集合中的元素

# res = varset.pop()

# res = varset.remove(123) 没有会报错

# res = varset.discard(123) 没有不会报错
# 更新集合中的元素

# res = varset.update({'8888', '666'})

# 清空集合
# res = varset.clear()

# 集合浅拷贝
# res = varset.copy()
# varset.add('999')

# 冰冻集合
varsetfrozen = frozenset((1,2,3))
print(varset)

# print(res)
print(varsetfrozen)
