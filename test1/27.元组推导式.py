# 元组推导式 和列表推导式 类似
# 元组推导式 得到的不是元组 而是一个生成器
# 生成器也是迭代器，不过可以自定义，可以采取获取迭代器的方法获取生成器的数据
# 1.用元组推导式 2。yield定义的函数 是生成器

varlist = [1, 2, 3, 4, 5, 6]

news = (i ** 2 for i in varlist)
# print(news)
# print(next(news))
# print(next(news))
print(tuple(news))

# for i in news:
#     print(i)
