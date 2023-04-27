import time
# 当前的时间戳 1631803116.920932
res = time.time()

# 当前的时间 字符串
res = time.ctime()

# 当前的时间 元祖
res = time.localtime()

res = time.strftime('%Y-%m-%d %H:%M:%S 周%w')
print(res)

# 计算程序运行的时间
start = time.perf_counter()
for i in range(10000):
    if 100 >90:
        pass

end = time.perf_counter()

print(end-start)