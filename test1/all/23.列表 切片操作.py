varlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 开始值，结束值，步进值
res = varlist[2:6:2]

res = varlist[::-1]
# 切片更新
varlist[2:4] = 'a'
# 切片删除
del varlist[2:4]
print(res)
print(varlist)
