import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def tel(who):
    print(f'给{who}打电话，线程号为{threading.current_thread()},进程号为{os.getpid()}')
    time.sleep(3)
    print(f'给{who}挂断电话,线程号为{threading.current_thread()},进程号为{os.getpid()}')


userlist = ['summer', '笨笨', '豆豆', '天天', '酷飞']
# 创建线程池
# pool = ThreadPoolExecutor(max_workers=3)
# # 循环指派任务和参数
# [pool.submit(tel, user) for user in userlist]
# # 关闭线程池
# pool.shutdown()

# 创建进程池
if __name__ == '__main__':
    pool = ProcessPoolExecutor(max_workers=3)
    # 循环指派任务和参数
    [pool.submit(tel, i) for i in userlist]
    # 关闭进程池
    pool.shutdown()
