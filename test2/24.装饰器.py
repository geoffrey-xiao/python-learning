# 装饰器

# 使用@装饰方法，修改或者扩展原来函数的功能
# 利用闭包函数，将普通函数作为参数传入，内函数使用这个参数 并且返回这个内函数
def func(f):
    def inner():
        print('我是内函数1')
        f()
        print('我是 内函数2')

    return inner


@func
def old():
    print('我是一个普通的函数')


# old = func(old)
# 装饰器 @func等同于 old = func(old)
old()
