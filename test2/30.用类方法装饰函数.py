class Outer():
    def newinner(func):
        Outer.func = func
        return Outer.inner

    def inner():
        print('加上妹子微信')
        Outer.func()
        print('去看电影')


@Outer.newinner
def love():
    print('和妹子谈谈人生聊聊理想')


love()
