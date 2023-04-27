import random

# 0-1随机小数 左闭右开
res = random.random()
# 指定范围内的随机整数 = random.randint()
res = random.randrange(5, 15, 2)
# 指定范围内的随机小数
res = random.uniform(4, 7)
# 指定容器中的随机值
# res = random.choice([1,8,7,3])
# 打乱顺序
varlist = [1, 9, 2, 5]
res = random.shuffle(varlist)
print(res,varlist)
