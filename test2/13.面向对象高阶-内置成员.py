class F():
    pass


class Demo(F):
    '''
    我是说明文档
    '''
    name = 'summer'
    age = 2

    def pao(self):
        print('跑的快')


demo = Demo()
demo.color = 'white'
# 获取类的所有属性和方法
res = Demo.__dict__
# 获取对象的属性和方法
res = demo.__dict__
# 获取类的说明文档
res = Demo.__doc__
# __module__获取类所在的文件 如果是本文件则为__main__
res = Demo.__module__
# 获取类的父类列表 __bases__
res = Demo.__bases__
print(res)
