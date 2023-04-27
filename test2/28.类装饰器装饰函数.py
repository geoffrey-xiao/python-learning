class Demo():
    def __call__(self, func):
        self.func = func
        return self.newfunc

    def newfunc(self, who):
        print('拿到妹子微信')
        self.func(who)
        print('去看电影')


# @Demo() ==>@obj==> obj(love) ==>__call__
# 实例化一个对象，把对象当成方法去调用
@Demo()
def love(who):
    print(f'{who}和妹子谈谈人生，聊聊理想')


love('张三')
