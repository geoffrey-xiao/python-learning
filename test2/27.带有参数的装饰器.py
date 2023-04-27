def kuozhan(man):
    def out(f):
        def inner1():
            print('妹子给了你微信')
            f()

        def inner2():
            print('妹子给你介绍了个大妈')
            f()

        if man == '高富帅':
            return inner1

        else:
            return inner2

    return out


@kuozhan('矮戳穷')
def love():
    print('聊聊人生，谈谈理想')


love()
