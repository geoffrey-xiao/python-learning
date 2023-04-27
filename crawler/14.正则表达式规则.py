import re

# 1.普通字符串

# varstr = 'iloveyou152summer'
# reg = 'ilove'
#
# res = re.search(reg, varstr).group()
# print(res)

# 2.转义字符
varstr = ' _?*iloveyousummer5211314'
# \w 单个的字母，数字，下划线
# \W 单个的非字母，数字，下划线
# \d 单个的数字
# \D 单个的非数字
# \s 单个的空格或者制表符
# \S 单个的非空格或者制表符
# reg = '\S'
# res = re.search(reg, varstr).group()
# print(res)

# 3.特殊字符
'''
1. .点表示单个的任意字符，除了空格
2。 * 表示匹配的次数，可以是0次
3. + 表示匹配的次数，至少匹配一次
4. ? 拒绝贪婪，限制匹配次数
5. {}表示匹配次数,一个参数表示匹配次数，两个参数表示匹配区间
6. []表示字符的范围
7.() 表示子组，首先会作为正则的一部分进行匹配，另外会把里面的内容单独取出来
8. ^表示开始 $表示结尾
'''
varstr = '&iloveyou1314 summer521'

reg = '\w{3}(\d{3})'
res = re.search(reg, varstr).groups()
print(res)

title = u'<div>name</div><div>age</div>'

p1 = re.compile(r"<div>.*</div>")
p2 = re.compile(r"<div>.*?</div>")

m1 = p1.search(title)
print(m1.group())

m2 = p2.search(title)
print(m2.group())
