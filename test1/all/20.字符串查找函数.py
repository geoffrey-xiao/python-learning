vars = 'iloveyousummer'

# res = 'i' in vars
#
# res = len(vars)
# print(res)

# str.find() 查找字符是否在字符串中，没有则返回-1

res = vars.find('u', 0, 10)
res = vars.rfind(('u'))

# str.index() 和find方法一样，找不到会报错 ValueError: substring not found
# res = vars.index('g')
print(res)
