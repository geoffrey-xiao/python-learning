arr = ['张三', '李四', '王五', 'summer']

res = iter(arr)

print(type(res))

# 迭代器的调用
# 三种方法，调用一次少一次
res1 = next(res)
print(res1)
print(next(res))

# print(list(res))

for i in res:
    print(i)

# 判断是否为可迭代对象或者迭代器
# type()
# isinstance()
# next()
from collections.abc import Iterator, Iterable

print(isinstance(arr, Iterable))
print(isinstance(arr, Iterator))
print(isinstance(res, Iterable))
print(isinstance(res, Iterator))
