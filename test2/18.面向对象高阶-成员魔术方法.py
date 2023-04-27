class Demo():
    name = 'summer'
    age = 2
    sex = 'female'

    # 访问对象成员时自动触发 不能使用对象.成员访问 否则会引发递归
    # def __getattribute__(self, item):
    #     print(item)
    #     try:
    #         res = object.__getattribute__(self, item)
    #         return res[0] + '*' + res[2]
    #     except:
    #         return False

    # 访问对象成员不存在时触发
    # def __getattr__(self, item):
    #     print(item)

    # 给对象添加或者修改成员触发
    # def __setattr__(self, key, value):
    #     # print(key,value)
    #     object.__setattr__(self, key, value)

    # 删除对象成员时触发
    def __delattr__(self, item):
        print(item)
        object.__delattr__(self, item)

    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.sex = s


zs = Demo('张三丰', 88, 'man')
# print(zs.color)
zs.color = 'yellow'
# del zs.color
print(zs.color)
