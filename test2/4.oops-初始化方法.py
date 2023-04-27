'''
魔术方法：类的一种成员方法；
        在某种情况下自动触发，通常以__init__
        系统自带的方法，我们只能调用不能自己定义
'''


class Person():
    name = None
    age = None

    def __init__(self, n):
        self.name = n
        print(self.name)
        self.say()

    def say(self):
        print(f'我是{self.name}，我是个可爱的小狗狗')


summer = Person('summer')
