import numpy as np

# ndarray:N维组数组对象
arr1 = np.array([1, 2, 3, 4])
# print(type(arr1))

# 生成数组
arr2 = np.arange(1, 10)
# print(arr2)

# list转ndarray
arr3 = np.array(range(1, 10))
# print(arr3,type(arr3))

# 元素类型
dtype = np.arange(1, 4).dtype
# print(dtype)
# 元素类型转换
arr4 = np.arange(1, 4).astype('float')
# print(arr4)

# 形状
arr5 = np.array(range(0, 12))
# print(arr5,arr5.shape)

# 重塑 3行4列
new_arr = arr5.reshape(3, 4)
# print(new_arr,new_arr.shape)

# 行与列 axis=0 自上而下 axis=1 从左到右
arr6 = np.array(range(12)).reshape(3, 4)
# print(arr6.sum(axis=0))
# print(arr6.sum(axis=1))

# 数组运算
arr7 = np.array(range(12)).reshape(3, 4)
# print(f'{arr7},\n,{arr7+arr7}')

arr8 = np.arange(0, 3).reshape(3, 1)
# print(arr7+arr8)

# 逻辑运算
arr9 = np.array(range(12)).reshape(3, 4)
arr10 = np.arange(3, 15).reshape(3, 4)
# print(arr9==arr10)

# 索引与切片
arr11 = np.array([1, 2, 3, 4, 5])
# print(arr11[2:3])

arr12 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr12[2])
# print(arr12[2][1])
# print(arr12[:2])
# print(arr12[:2][1:])
# print(arr12[:2,1:])

# 神奇索引
arr13 = np.empty((4, 4))
for i in range(4):
    arr13[i] = (i + 1) ** 2
# print(arr13)
# print(arr13[[2,3,0]])
# print(arr13[[2,3,0]][[0,2,1]])

# 三元表达式where
xarr = np.array([1, 2, 3, 4, 5])
yarr = np.array([3, 4, 5, 6, 7])
res = np.where(xarr > 4, xarr, yarr)
# print(res)

temp = np.array([28, 24, 31, 27, 35])
choise = np.where(temp > 28, '走地下室', '走室外')
# print(choise)

# 基础统计方法
arr14 = np.arange(0, 12).reshape(3, 4)
# print(arr14,arr14.sum())
# print(arr14,arr14.mean())
# print(arr14,arr14.mean(axis=0))
# print(arr14,arr14.mean(axis=1))

# 排序
arr15 = np.random.randn(6)
arr15.sort()
print(arr15)
