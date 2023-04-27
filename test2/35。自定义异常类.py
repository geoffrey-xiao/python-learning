class Myexecption():
    def __init__(self):
        import traceback
        import logging
        logging.basicConfig(
            filename='./error.log',
            format='%(asctime)s  %(levelname)s\n  %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        errormsg = traceback.format_exc()
        print(errormsg)
        logging.error(errormsg)


import traceback

try:
    a = 'aa'
    a[4]
except:
    print('触发了异常')
    # errormsg = traceback.format_exc()
    # print(errormsg)
    Myexecption()
