# 1.指定错误类

# n1 = 'hello'
# try:
#     int(n1)
# except ValueError as e:
#     print('发生错误', e)

# 2.多分支异常类
# n1 = 'hello'
# try:
#     # int(n1)
#     n1[6]
# except IndexError as e:
#     print('IndexError ', e)
# except ValueError as e:
#     print('ValueError', e)

# 3.通用异常类
# n1 = 'hello'
# try:
#     # int(n1)
#     n1[6]
# except Exception as e:
#     print('exceptionError ', e)

# 4.try..except..else 没有发生异常
#
# n1 = 'hello'
# try:
#     # int(n1)
#     n1[2]
# except Exception as e:
#     print('exceptionError ', e)
# else:
#     print('程序正常执行')

# 5.try...except...finally... 有没有异常都会捕获 一般用于清理
# n1 = 'hello'
# try:
#     # int(n1)
#     n1[8]
# except Exception as e:
#     print('exceptionError ', e)
# finally:
#     print('程序正常执行')

# 6.使用raise主动抛出错误
# try:
#     raise Exception('程序错误了')
# except Exception as e:
#     print(e)

# 7.断言错误 AssertionError 主要用于代码调试
assert 1 == 1
