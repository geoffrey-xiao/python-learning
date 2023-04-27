class A():
    name = 'summer'


class B():
    age = 2


class C(A, B):
    pass


c = C()
# 检测是否是某个类的子类
res = issubclass(C, A)
# 检测对象是否是类的实例化
res = isinstance(c, C)
# 检测类/对象是否含有该属性
res = hasattr(c, 'pao')
# 设置类/对象的属性
res = setattr(c, 'color', 'white')
# 删除类/对象的属性
delattr(c, 'color')
print(res)
