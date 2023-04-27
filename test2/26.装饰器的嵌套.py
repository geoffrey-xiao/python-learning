def sleep(f):
    def inner(name):
        print('summer上到床上')
        f(name)
        print('summer睡着了')

    return inner


# def fengsleep(f):
#     def finner():
#         print('峰峰上到床上')
#         f()
#         print('峰峰睡着了')
#
#     return finner


''' 先执行离的近的函数 返回inner
    再把inner作为参数传进去  返回finner
    执行love函数相当于执行finner函数
'''


# @fengsleep
@sleep
def love(name):
    print(f'{name}去睡觉')


love('summer')
