# a = 2
# b = a * 8
# print(b)

# 递归函数一定要有条件，否则一直执行下去，造成内存溢出
def degui(num):
    print(num)
    if (num > 0):
        degui(num - 1)
    print(num)


degui(5)
