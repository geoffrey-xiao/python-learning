# reduce()函数 第一个参数 处理方法，第二个函数可迭代器对象
# 先处理前两个值，得到结果后，与第三个值作为参数 参与函数运算，直到最后得到运算结果
from functools import reduce

varlist = [5, 2, 1, 1]


def func(x, y):
    return x * 10 + y


res = reduce(func, varlist)
print(res)
