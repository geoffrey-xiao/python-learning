'''
mixin
混合 扩展功能 实现单一功能
通过类继承实现 通常不单一使用，通常混合到其他类中，扩展功能
不依赖子类的实现
'''


class Vehicle():
    def lahuo(self):
        print('运输货物')

    def laren(self):
        print('搭载乘客')


# 定义混合类，扩展飞行功能呢
class FlyingMixin():
    def fly(self):
        print('可以飞行')


class Cart(Vehicle):
    pass


class Helicopter(Vehicle, FlyingMixin):
    pass


class Airplane(Vehicle, FlyingMixin):
    pass
