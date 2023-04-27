# 1
# from package import a, b
#
# a.funca()
# b.funcb()

# 2.
# from package.a import funca
# from package.b import funcb
# funca()
# funcb()

# 3

from package import *
a.funca()
b.funcb()

# 当前脚本中查看搜索路径 sys.path
#['',
# '/opt/homebrew/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python39.zip',
# '/opt/homebrew/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9',
# '/opt/homebrew/Cellar/python@3.9/3.9.6/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload',
# '/opt/homebrew/lib/python3.9/site-packages']