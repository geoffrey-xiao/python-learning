import time


class Views():
    def __init__(self):
        self.showIndex()
        time.sleep(1)
        print('正在查询中。。。')
        self.showOpts()

    def showIndex(self):
        varstr = '''
        *****************************
        *                           *
        *      welcome to Bank      *
        *                           *
        *****************************
        '''
        print(varstr)

    def showOpts(self):
        varstr = '''
        **********************************
        *                                *
        *      (1)注册    （2)查询         *           
        *     （3)存款    （4)取款         *
        *      (5)转账     (6)改密         *
        *      (7)锁卡     (8)接卡         *
        *      (9)补卡     (10)退出        *
        *                                 *
        *                                 *
        *********************************
        '''
        print(varstr)


if __name__ == '__main__':
    Views()
