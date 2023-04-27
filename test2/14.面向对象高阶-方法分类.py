'''
1.对象方法
2。类方法
3。绑定类方法
4。静态方法
'''


class Demo():
    # 对象方法 只能通过对象调用 不能通过类调用
    def func1(self):
        print('object function')

    # 类方法 有@classmethod装饰器 对象和类都可以调用
    @classmethod
    def func2(self):
        print('class function')

    # 绑定类方法 只能通过类调用
    def func3():
        print('bind  class function')

    # 静态方法 用@staticmethod装饰 对象和类都可以调用
    @staticmethod
    def func4():
        print('static function')


demo = Demo()
# demo.func1()
# Demo.func1()

# demo.func2()
# Demo.func2()

# Demo.func3()
demo.func4()
Demo.func4()
