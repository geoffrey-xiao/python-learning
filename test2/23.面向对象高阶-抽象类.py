import abc


# 通过metaclass = abc.ABCMeta定义抽象类
class WriteCode(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write_js(self):
        pass

    @abc.abstractmethod
    def write_python(self):
        pass


# 抽象类不能直接实例化 需要子类继承
class Demo(WriteCode):
    def write_js(self):
        print('开发js代码')

    def write_python(self):
        print('开发python代码')


# wr = WriteCode()
demo = Demo()
demo.write_js()
demo.write_python()
