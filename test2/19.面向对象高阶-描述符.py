'''
当一个类中 包含了__get__  __set__ __delete三个魔术方法全部或者之一时，这个类被称为描述符类
作用：描述符类是对类中的某个成员进行一个详细的管理操作（获取，赋值，删除）
使用方法：把描述符类赋值给一个类的成员属性
'''


class PersonName():
    __name = 'zhaolei'

    def __get__(self, instance, owner):
        return self.__name

    def __set__(self, instance, value):
        self.__name = value

    def __delete__(self, instance):
        del self.__name


class Person():
    name = PersonName()


s = Person()

s.name = 'fengfeng'

del s.name
print(s.name)
