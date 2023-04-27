# 操作类
import random, os
from package.cardclass import Card
from package.personclass import Person
import pickle


class Controller():
    userid_cardobj_dict = {}
    cardid_userobj_dict = {}

    user_file_url = './databases/user.txt'
    card_file_url = './databases/card.txt'

    def __init__(self):
        self.__loaddata()

    # 读取数据
    def __loaddata(self):
        if os.path.exists(self.card_file_url):
            with open(self.card_file_url, 'rb') as fp:
                self.cardid_userobj_dict = pickle.load(fp)
        if os.path.exists(self.user_file_url):
            with open(self.user_file_url, 'rb') as fp:
                self.userid_cardobj_dict = pickle.load(fp)

    # 1.注册
    def register(self):
        print('注册')
        # 获取基本信息
        name = self.getInfo('姓名')
        pwd = self.getInfo('密码')
        userid = self.getInfo('身份证号')
        phone = self.getInfo('手机号')
        print(name, pwd, userid, phone)

        cardid = random.randint(100000, 999999)
        cardobj = Card(cardid, pwd)

        personobj = Person(name, phone, userid, cardobj)

        self.userid_cardobj_dict[userid] = cardobj
        self.cardid_userobj_dict[cardid] = personobj

        print(f'创建成功，用户名为{name},卡号为{cardid},余额为{cardobj.money}')

    # 2.查询
    def query(self):
        cardnum = int(input('请输入您的卡号：'))
        if cardnum not in self.cardid_userobj_dict:
            print(self.cardid_userobj_dict)
            print('卡号不存在')
            return
        else:
            cardobj = self.cardid_userobj_dict[cardnum].card
            if self.__checkpwd(cardobj):
                if cardobj.islock == True:
                    print('您的卡号已被锁定')
                else:
                    print(f'您卡内的余额为{cardobj.money}')

    # 3.存钱
    def save(self):
        print('存钱')

    # 4.取钱
    def withdraw(self):
        print('取钱')

    # 5. 转账
    def transfer(self):
        print('转账')

    # 6.改密
    def changePwd(self):
        print('改密')

    # 7.锁卡
    def lockCard(self):
        print('锁卡')

    # 8.解卡
    def unlockCard(self):
        print('解卡')

    # 9.补卡
    def makeupCard(self):
        print('补卡')

    # 10.退出
    def logout(self):
        with open(self.user_file_url, 'wb+') as fp:
            pickle.dump(self.userid_cardobj_dict, fp)
        with open(self.card_file_url, 'wb+') as fp:
            pickle.dump(self.cardid_userobj_dict, fp)

    def getInfo(self, info):
        while True:
            name = input(f'请输入您的{info}:')
            if not name:
                print('输入信息有误，请重新输入')
                continue
            else:
                return name

    def __checkpwd(self, cardobj):
        num = 3
        while True:
            pwd = input('请输入密码：')
            if pwd == cardobj.pwd:
                return True
            else:
                num -= 1
                if num == 0:
                    cardobj.islock = True
                    print('您的卡已经被锁定')
                    break
                print(f'密码错误，您还有{num}次机会')
                continue
