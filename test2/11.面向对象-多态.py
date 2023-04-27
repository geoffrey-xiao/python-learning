'''
多态
对于同一个方法，调用的对象不一样，实现了不同的结果
'''


class Computer():
    def usb(self, obj):
        obj.start()


class Mouse():
    def start(self):
        print('鼠标启动了。。。')


class Keyboard():
    def start(self):
        print('键盘启动了。。。')


class Udisk():
    def start(self):

        print('u盘启动了。。。')


m = Mouse()
k = Keyboard()
u = Udisk()

c = Computer()
c.usb(m)
c.usb(k)
c.usb(u)
