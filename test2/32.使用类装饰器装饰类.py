class Kuozhan():
    def __call__(self, cls):
        self.cls = cls
        return self.newfunc

    def newfunc(self):
        self.cls.name = '这是拓展的属性'
        self.cls.func2 = self.func2
        return self.cls()

    def func2(self):
        print('这是拓展的方法')


@Kuozhan()
class Demo():
    def func(self):
        print('这是类内部的函数')


demo = Demo()
demo.func()
demo.func2()
print(demo.name)