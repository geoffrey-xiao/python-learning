# self 在类的方法中指向 当前对象
# 谁调用这个方法，self就指向谁

class Person():
    name = 'summer'
    age = 3

    # self指向调用这个方法的对象 非绑定类方法
    def sing(self):
        print(f'{self.name}会唱歌')
    # 没有形参的方法 不能被对象调用 只能被类调用 绑定类方法
    def func():
        print('我是没有self的方法')

summer = Person()

Person.func()
