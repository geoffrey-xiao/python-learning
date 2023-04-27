import re

'''
match 从字符串的开头进行匹配，如果开头不符合，则匹配失败，返回None
search 从字符串开头到结尾进行搜索式匹配，如果在整个字符串中都没有匹配成功，则匹配失败
'''
vars = '1iloveyou2summer'

reg = 'ove'
reg = '\d'

# res = re.match(reg,vars)
res = re.search(reg, vars)
print(res)
# group 返回匹配的结果
print(res.group())
# span 返回匹配的区间
print(res.span())
