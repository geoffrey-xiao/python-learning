# 银行卡类

class Card():
    def __init__(self, cardid, pwd, money=10, islock=False):
        self.cardid = cardid
        self.pwd = pwd
        self.money = money
        self.islock = islock
