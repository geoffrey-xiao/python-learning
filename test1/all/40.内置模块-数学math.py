import math

vars = -3.14
# 向上取整
res = math.ceil(vars)
# 向下取整
res = math.floor(vars)
# 绝对值
res = math.fabs(vars)
# 求和
res = math.fsum([1,2,3])
# 第二个参数的符号赋给第一参数
res = math.copysign(2,-10)
print(res)