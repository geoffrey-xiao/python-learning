userlist = []
pwdlist = []
blacklist = []


def readAll():
    with open('./user.txt', 'a+', encoding='utf-8') as fp:
        fp.seek(0)
        res = fp.readlines()
        for i in res:
            str = i.strip().split(':')
            userlist.append(str[0])
            pwdlist.append(str[1])
    with open('./black.txt', 'a+', encoding='utf-8') as fp:
        fp.seek(0)
        res = fp.readlines()
        for i in res:
            str = i.strip()
            blacklist.append(str)


def register():
    site = True
    while site:
        user = input('请输入用户名：')
        if user not in userlist:
            while True:
                pwd = input('请输入密码：')
                if len(pwd) >= 5:
                    repwd = input('请确认密码：')
                    if pwd == repwd:
                        print(user, pwd, repwd)
                        with open('./user.txt', 'a+', encoding='utf-8') as fp:
                            fp.write(f'{user}:{pwd}\n')
                        site = False
                        break
                    else:
                        print('两次输入的密码不一致')
                else:
                    print('密码格式不正确，请重新输入')
        else:
            print('用户名已存在')


# register()

def login():
    errornum = 3
    user = input('请输入用户名：')
    if user not in blacklist:
        if user in userlist:
            while True:
                pwd = input('请输入密码：')
                i = userlist.index(user)
                userpwd = pwdlist[i]
                if pwd == userpwd:
                    print('登陆成功')
                    break
                else:
                    errornum -= 1
                    if errornum == 0:
                        print('账号已被锁')
                        with open('./black.txt', 'a+', encoding='utf-8') as fp:
                            fp.write(f'{user}\n')
                    else:
                        print(f'密码错误，您还有{errornum}机会')
        else:
            print('用户不存在，请先注册')
    else:
        print('您的账号已被锁，请联系管理员')
        return


# login()

if __name__ == '__main__':
    readAll()
    while True:
        vars = '''
            注册（0）****登陆（1）
            '''
        print(vars)
        res = input('请选择体验的功能：')
        if res == '0':
            register()
        else:
            login()
