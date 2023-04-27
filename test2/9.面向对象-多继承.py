class F():
    def play(self):
        print('爱抽烟，爱喝酒')


class M():
    def play(self):
        print('爱打麻将')

# super方法只能继承一个类
class C(F,M):
    def play(self):
        super().play()
        print('爱玩王者荣耀')


child = C()
child.play()
