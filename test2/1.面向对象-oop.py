# 用class定义类

class Car():
    color = 'red'
    brand = '奥迪',
    pailiang = 2.4

    def zairen(self):
        print('带summer兜风')

    def lahuo(self):
        print('货拉拉去搬家')

    def showoff(self):
        print('在朋友面前装比')


#
# carObj = Car()
# print(carObj, type(carObj))
#
# print(carObj.color)
# print(carObj.zairen())
a = Car()
b = Car()

# 对象修改的属性或者方法只在对象本身生效，不会影响到类以及其他实例化的对象
a.color = 'black'
a.name = '奥迪a6'

# 'Car' object has no attribute 'name'
# 只能删除对象自己的属性
# del a.name

# 给对象添加方法
def func():
    print('summer is a beautiful dog')

a.comment = func;

# del a.comment

# 不能删除类的属性或者方法 AttributeError: lahuo
# del a.lahuo
# a.comment()
print(a.name, b.color)
