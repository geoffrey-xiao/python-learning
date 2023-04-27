# 1.写入文件 write() writelines() 可以写入容器类数据 但是必须都是字符串
# 2.读取文件 read() readline()读取文件的一行 readlines()读取所有行，会放到一个列表中
vars = ['峰峰', '真帅']
# with open('./2.txt', 'w', encoding='utf-8') as fp:
#     fp.writelines(vars)
# with open('./2.txt', 'r', encoding='utf-8') as fp:
#     res = fp.readlines()
#     print(res)

# seek() 设置光标位置
# with open('./2.txt', 'a+', encoding='utf-8') as fp:
#     # fp.seek(0) 将光标移动到文件开头
#     # fp.seek(0,2) 将光标移动导文件末尾
#     res = fp.read()
#     print(res)

# truncate 截断文件内容 参数为截断的个数，只保留之前的 之后的删除
with open('./2.txt', 'a+', encoding='utf-8') as fp:
    # fp.seek(0) 将光标移动到文件开头
    # fp.seek(0,2) 将光标移动导文件末尾
    res = fp.truncate(20)
    print(res)
