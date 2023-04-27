class Demo():
    list = [1, 2, 3]

    def __len__(self):
        return len(self.list)

    # def __str__(self):
    #     return 'nishiyigexiaoshagua'

    def __repr__(self):
        return 'summer真可爱'


demo = Demo()
# 返回对象某个属性的长度
# res = len(demo)
# res = str(demo)
# print(res)
print(demo)
