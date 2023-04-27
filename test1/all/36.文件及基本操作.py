'''
文件基本操作：
1.打开文件 open()
    参数1：文件路径 url 统一资源定位符 相对路径 绝对路径（根路径）
    参数2：打开模式 w r x a
        x 异或模式 文件存在会报错，文件不存在会新建 防止文件覆盖
        a 追加模式 文件不存在会新建 文件存在会打开文件，但是写入文件不会覆盖，光标在文件末尾

        扩展模式：
            1. b bytes 二进制文件
            2.+ plus 增强模式
    可选参数：字符集 encodeing = 'utf-8'
2.读写文件 写入文件write()
3.关闭文件 close()
'''
# # 文件的写入 w模式
# # 打开文件 如果没有的话会在指定路径创建新文件
# fp = open('./1.txt','w',encoding='utf-8')
# print(fp,type(fp))
# # 写入文件 会把之前的文件内容清空，光标放到文件最开始
# fp.write('summer is a cute dog')
#
# # 关闭文件
# fp.close()

# 文件的读取 r模式 文件不存在会报错 FileNotFoundError: [Errno 2] No such file or directory: './2.txt'
# 文件的异或x模式，文件存在报错 FileExistsError: [Errno 17] File exists: './1.txt'
fp = open('./1.txt', 'a+', encoding='utf-8')
# print(fp,type(fp))
# 写入文件 光标放到文件最开始
# res = fp.read()
fp.write('啦啦啦!')
fp.seek(0)
res = fp.read()
print(res)
# 关闭文件
fp.close()
