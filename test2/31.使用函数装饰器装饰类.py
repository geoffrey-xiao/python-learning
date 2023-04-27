def dec(cls):
    cls.name = 'summer'

    def func2(cls):
        print('这是装饰器拓展的方法')

    cls.func2 = func2

    return cls


@dec
class Demo():
    def func(self):
        print('这是类内部的方法')


demo = Demo()
demo.func()
demo.func2()
print(demo.name)
