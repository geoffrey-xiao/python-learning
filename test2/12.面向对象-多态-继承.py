class USB():
    '''
    类的说明：
    定义一个接口规范类，需要子类继承并重新start方法
    '''

    def start(self):
        pass


class Mouse(USB):
    def start(self):
        print('鼠标启动了。。。')


class Keyboard(USB):
    def start(self):
        print('键盘启动了。。。')


class Udisk(USB):
    def start(self):
        print('u盘启动了。。。')


m = Mouse()
k = Keyboard()
u = Udisk()
m.start()
k.start()
u.start()
