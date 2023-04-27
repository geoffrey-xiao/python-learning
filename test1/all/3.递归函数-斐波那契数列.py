def feibo(num):
    if num == 1 or num == 2:
        return 1
    else:
        return feibo(num - 1) + feibo(num - 2)


res = feibo(6)
print(res)
