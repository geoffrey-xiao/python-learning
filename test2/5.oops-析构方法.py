# 析构方法
# 在对象被销毁时 会触发这个方法 __del__

'''
对象被销毁的条件：
1.程序结束后，所有的资源都会被销毁释放
2.删除这个对象，对象即被销毁
3.对象没有变量赋值
'''
class writeLog():
    fileurl = './'
    filename = 'summer'

    def __init__(self):
        print('对象初始化调用')
        self.file = open(self.fileurl + self.filename, 'a+', encoding='utf-8')

    def logContent(self):
        print('正在写入')

    def __del__(self):
        print('对象被销毁时触发')
        self.file.close()


# summer = writeLog()
writeLog()
# summer.logContent()
# del summer
print('000')