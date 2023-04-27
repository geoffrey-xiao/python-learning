# 1.基本的推到式

# varlist = []
# for i in range(4):
#     varlist.append(i**2)
# print(varlist)
#
# newlist = [i**2 for i in range(4)]
# print(newlist)

# 2.条件判断的推到式
# varlist = []
# for i in range(10):
#     if (i % 2 == 0):
#         varlist.append((i * 2))
# print(varlist)
#
# newlist = [i * 2 for i in range(10) if i % 2 == 0]
# print(newlist)

# 3.双重for循环的推到式
# varlist = []
# alist = [1, 2, 3]
# blist = [5, 6, 7]
# for x in alist:
#     for y in blist:
#         if x != y:
#             varlist.append((x, y))
# print(varlist)
# newlist = [(x, y) for x in alist for y in blist if x != y]
# print(varlist)

# 4.循环和条件判断的推到式
# nlist = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# newlist = []
# for i in range(4):
#     vlist = []
#     for row in nlist:
#         vlist.append(row[i])
#     newlist.append(vlist)
# print(newlist)
#
# Newlist = [[row[i] for row in nlist] for i in range(4)]
# print(Newlist)

# 练习题
# obj = {'user': 'summer', 'age': 3, 'sex': 'female'}
# varlist = []
# for i in obj:
#     varlist.append(f'{i}={obj[i]}')
# print(varlist)
#
# newlist = [f'{i}={obj[i]}' for i in obj]
# print(newlist)

# 把列表的所有小写字母转为大写

# varlist = ['aaa', 'BBB', 'ccc', 'ddd']
# newlist = [i.upper() for i in varlist]
# print(newlist)

# x 0-5之间偶数 y 0-5之间奇数 将x,y组成元祖放到列表

varlist = [(x,y) for x in range(6) for y in range(6) if x % 2 == 0 and y % 2 != 0]
print(varlist)
