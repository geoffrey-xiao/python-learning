'''
1.findall
按照正则规则在字符串中找到符合正则的所有元素 返回一个列表 如果没有返回空列表
2.finditer
按照正则规则在字符串中找到符合正则的所有元素 返回一个迭代器
3.sub 搜索替换
按照正则的规则 在字符串中找到匹配的字符 ，完成替换
re.sub(正则，替换的字符串，被替换的原始字符串)
4.compile
定义正则表达式
'''
import re

varstr = 'iloveyou521summer1314'
reg = '\d{3}'
res = re.findall(reg, varstr)
res = list(re.finditer(reg, varstr))
res = re.sub(reg, 'AAA', varstr)
print(res)

varstr2 = 'iloveyou521summer1314'
reg2 = re.compile('\d{3}')
res2 = reg2.findall(varstr2)
res2 = reg2.finditer(varstr2)
res2 = reg2.sub('BBB', varstr2)
print(res2)
