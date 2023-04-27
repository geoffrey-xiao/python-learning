import time


# 定义一个装饰器
def runtime(f):
    def inner():
        start = time.perf_counter()
        f()
        counttime = time.perf_counter() - start
        print(f'函数的执行时间是{counttime}')
    return inner


@runtime
def func():
    for i in range(0, 10):
        print(i, end=' ')
        time.sleep(1)


func()
