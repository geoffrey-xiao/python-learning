import time


class Mylog():
    fileurl = './'
    filename = time.strftime('%Y-%m-%d %H:%M:%S') + '.log'
    fileobj = None

    def __init__(self):
        self.fileobj = open(self.fileurl + self.filename, 'a+', encoding='utf-8')

    def wlog(self, content):
        date = time.strftime('%Y-%m-%d %H:%M:%S')
        msg = date + ' ' + content +'\n'
        self.fileobj.write(msg)

    def __del__(self):
        self.fileobj.close()


mlog = Mylog()
mlog.wlog('summer真淘气')
