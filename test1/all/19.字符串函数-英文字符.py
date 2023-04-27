varstr = 'ILoveyou'

# res = varstr.capitalize()
#
# res = varstr.title()
#
# res =varstr.upper()
#
# res = varstr.swapcase()
# res1 = res.lower()
# print(res)

# 字符检测方法

res = varstr.isupper()
res =varstr.islower()
res = varstr.istitle()

# str.isalnum() 是否由字符（中英文，数字）组成
# res = varstr.isalnum()
# str.isalpha() 是否由字符（中英文）组成
# res = varstr.isalpha()
# str.isdigit() 是否由字符（数字）组成
# res = varstr.isdigit()
# str.startswith() 以某个字符开头
# res= varstr.startswith('I')
# str.endswith() 以某个字符结尾
res = varstr.endswith('you')
print(res)