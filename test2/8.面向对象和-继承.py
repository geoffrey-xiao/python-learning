'''
子类可以继承父类所有的属性和方法 除了私有属性或方法
子类继承父类后，可以重写父类的方法，叫做重写
也可以添加子类自己的方法，叫做扩展
子类也可以调用父类的方法 super()
'''


class maoke():
    maose = '猫纹'
    sex = 'female'

    def pao(self):
        print('跑的快')

    def walk(self):
        print('会走猫步')


class mao(maoke):

    def zhua(self):
        super().walk()
        print('会抓老鼠')

    pass


kittey = mao()
kittey.zhua()
# print(kittey, kittey.maose)
