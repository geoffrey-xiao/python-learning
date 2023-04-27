from package.viewsclass import Views
from package.controllerclass import Controller


class Main():
    def __init__(self):
        view = Views()
        obj = Controller()

        while True:
            vars = input('请输入您需要的操作')
            code = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            if vars not in code:
                print('输入错误，请重新输入')
                view.showOpts()
                continue
            if vars == '1':
                obj.register()
            elif vars == '2':
                obj.query()
            elif vars == '3':
                obj.save()
            elif vars == '4':
                obj.withdraw()
            elif vars == '5':
                obj.transfer()
            elif vars == '6':
                obj.changePwd()
            elif vars == '7':
                obj.lockCard()
            elif vars == '8':
                obj.unlockCard()
            elif vars == '9':
                obj.makeupCard()
            else:
                obj.logout()


if __name__ == '__main__':
    Main()
