'''
   在一个脚本中，一个类只能创建一个对象

   1.需要有一个方法控制对象的创建过程
    __new__
    2。定义一个私有属性储存和表示是否有对象
    3.在构造方法中条件判断对象是否被创建
    没有对象就创建对象并存储起来，如果有对象就返回对象
'''


class Demo():
    __obj = None

    def __new__(cls, *args, **kwargs):
        if not cls.__obj:
            cls.__obj = object.__new__(cls)

        return cls.__obj


a = Demo()
b = Demo()
print(a, b)
