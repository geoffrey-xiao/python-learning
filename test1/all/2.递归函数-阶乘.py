def jiecheng(num):
    if (num == 1):
        return 1
    else:
        return num * jiecheng(num - 1)


print(jiecheng(6))
