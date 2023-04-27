class Cart():
    name = 'summer'


print(Cart.name)

# 添加类成员属性
Cart.sex = 'female'
# 删除类成员属性
# del Cart.sex
# 修改类成员属性
Cart.name='leilei'
print(Cart.name)
a = Cart()
print(a.sex)
