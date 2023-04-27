vars1 = {'赵四', '小沈阳', '宋小宝', '刘能', 'summer'}
vars2 = {'郭富城', '黎明', '张学友', '刘德华', 'summer'}
# 1.交集
# res = vars1 & vars2

# res = vars1.intersection(vars2)
# res = vars1.intersection_update(vars2) 返回结果为None,会把交集重新赋值给vars1

# 2.并集

# res = vars1 | vars2

# res = vars1.union(vars2)
# res = vars1.update(vars2)
# 3.差集
#
# res = vars1-vars2
# res = vars2-vars1

# res = vars1.difference(vars2)
# res = vars1.difference_update(vars2)

# 4.对称差集 vars1和vars2 并集去掉交集的部分

# res = vars1 ^ vars2
# res = vars1.symmetric_difference(vars2)
# res = vars1.symmetric_difference_update(vars2)

# 5.超集和子集
set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3}
# res = set1.issuperset(set2)
# res = set2.issubset(set1)
# 两个集合是否有交集 不相交返回True,相交返回False
res = set1.isdisjoint(set2)
print(res)
# print(vars1)
