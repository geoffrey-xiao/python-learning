import os
import time,threading
from multiprocessing import Process
from threading import Thread


def tel(who):
    print(f'给{who}打电话,进程号是{os.getpid()},线程号是{threading.current_thread()}')
    time.sleep(3)
    print(f'给{who}挂了电话,进程号是{os.getpid()},线程号是{threading.current_thread()}')


varlist = ['刘德华', '肖战', 'summer']
# for i in varlist:
#     tel(i)

# 多进程 === 创建多条流水线或者多个车间
# if __name__ == '__main__':
#     arr = []
#     for i in varlist:
#         # 创建进程
#         p = Process(target=tel, args=(i,))
#         # 生成进程
#         p.start()
#         # 把创建的进程添加到列表中
#         arr.append(p)
#     # 阻塞结束进程
#     [item.join() for item in arr]

# 多线程 === 添加多个工人
if __name__ == '__main__':
    arr = []
    for i in varlist:
        # 创建进程
        p = Thread(target=tel, args=(i,))
        # 生成进程
        p.start()
        # 把创建的进程添加到列表中
        arr.append(p)
    # 阻塞结束进程
    [item.join() for item in arr]
