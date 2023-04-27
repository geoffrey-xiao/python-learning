# return 和 yield的区别：

# 1.return 和 yiled 都能返回结果
# 2.return 之后的代码不再执行，yield调用之后会返回结果，并记住当前调用的位置，下一次执行时从当前位置继续往后执行
# 3.yield返回的是个生成器 需要用next(),list(),或者for循环去调用
def func():
    print('hello 1')
    return 1


# func()


def funcyield():
    print('hello 1')
    yield 1
    print('summer 2')
    yield 2


res = funcyield()


# print(next(res))
# print(next(res))
# print(list(res))
# for i in res:
#     print(i)


# 用生成器改写斐波那契数列
# def feibo(num):
#     a, b, i = 0, 1, 0
#     while i < num:
#         print(b)
#         a, b = b, a + b
#         i += 1
#
#
# feibo(6)
def feibo():
    a, b, i = 0, 1, 0
    while True:
        yield b
        a, b = b, a + b
        i += 1
# res = feibo(6)
# print(list(res))

num = int(input('请输入一个正整数：'))
res = feibo()
# print(list(res))
for i in range(8):
    print(next(res))
