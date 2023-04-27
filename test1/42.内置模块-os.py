import os
# 获取当前工作目录
res = os.getcwd()
# os.chcwd() 修改工作目录
# 获取当前工作目录下的所有项
# res = os.listdir()

# os.makedirs('/Users/doubilei/Desktop/python/test1/abc/a')
# 删除文件夹
# os.rmdir('./abc')
# 递归删除文件夹
# os.removedirs('./abc/a/fff')
# 修改文件夹 或文件名称
os.rename('./abc','./aaa')
# 执行操作系统的指令
# os.system()
# print(res)