# 闭包函数  1.外部函数定义一个局部变量，内部函数使用外部函数的变量 2.外部函数返回一个内部函数，内函数就是闭包函数
def func():
    money = 0

    def work():
        nonlocal money
        money += 100
        print(money)

    return work


res = func()
res()
