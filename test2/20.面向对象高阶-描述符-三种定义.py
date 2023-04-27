'''
三种定义方式
1。描述类
2。property()函数
3。@property修饰器
'''


# 1.描述类
# class Name():
#     __name = 'summer'
#
#     def __get__(self, instance, owner):
#         return self.__name
#
#     def __set__(self, instance, value):
#         pass
#
#     def __delete__(self, instance):
#         pass
#
#
# class Person():
#     name = Name()
#
#
# s = Person()
# print(s.name)

# 2.property函数
#
#
# class Person():
#
#     def getname(self):
#         return 'summer'
#
#     def setname(self, value):
#         print(value)
#
#     def deletename(self):
#         pass
#
#     name = property(getname, setname, deletename)
#
#
# s = Person()
# print(s.name)
# s.name = 'lei'

# 3.property装饰器
class Person():
    @property
    def name(self):
        return 'summer'

    @name.setter
    def name(self, value):
        print(value)

    @name.deleter
    def name(self):
        pass


s = Person()
print(s.name)
s.name = 'lei'
