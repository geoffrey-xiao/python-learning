# 函数中有一个参数是函数 并且可以在函数内调用
def func(x, y, add):
    add(x, y)


def f(x, y):
    print(x + y)


res = func(1, 2, f)
print(res)
