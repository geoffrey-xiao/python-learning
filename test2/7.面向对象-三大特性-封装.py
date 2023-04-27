'''
封装的级别 public 共有的 protected 受保护的 private 私有的
在类的内部     ok            ok               ok
在类的外部     ok             no              no

_name 受保护的 __name 私有的
'''


class Dog():
    name = None
    _age = None
    __sex = None

    def __init__(self, name, age, sex):
        self.name = name
        self._age = age
        self.__sex = sex

    def _eat(self):
        print('吃饭')

    def sleep(self):
        print('睡觉')

    def dadoudou(self):
        print('打豆豆')
summer = Dog('summer',3,'female')

# 获取对象的所有成员属性
print(summer.__dict__)
print(summer.__dir__())

# summer.eat()
print(summer.age)
