class Man():
    num = 111

    def play(self):
        print('顿顿小烧烤')


class F(Man):
    num = 222

    def play(self):
        super().play()
        print('爱抽烟，爱喝酒')


class M(Man):
    num = 333

    def play(self):
        super().play()
        print('爱打麻将')


# super方法只能继承一个类
class C(F, M):
    num = 444

    def play(self):
        super().play()
        print(super().num)
        print('爱玩王者荣耀')


child = C()
child.play()

# MRO Method Relation Order 方法关系列表
# 先子类 后父类
# 子类继承父类 不是查找父类 而是在mro列表里向上寻找
# 子类调用super方法时，把self传到父类方法中
# [<class '__main__.C'>, <class '__main__.F'>, <class '__main__.M'>, <class '__main__.Man'>, <class 'object'>]
# print(C.mro())

# 检测一个类是否是另一个类的子类 issubclass()
res = issubclass(C,F)
res = issubclass(C,M)
res = issubclass(C,Man)

# print(res)
