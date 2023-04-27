# sorted函数
# param1 要排序的数组
# param2 是否reverse 默认false
# param3 函数 按照此函数排序

arr = [9, 2, 8, 5, 7, 4]
arr1 = sorted(arr)
print(arr1)

arr2 = sorted(arr, reverse=True)
print(arr2)


def func(num):
    return num % 2


arr3 = sorted(arr, key=func)
print(arr3)
