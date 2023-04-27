'''
程序执行异常
1。语法错误
2。逻辑错误
'''

# 1。通过条件判断 预防异常

n1 = 33
if isinstance(n1, int):
    res = 10 + n1
    print(res)

# 2。发生不可知的异常，try...except... 是在错误发生后进行处理
try:
    with open('./summer.txt', 'r', encoding='utf-8') as myfile:
        res = myfile.read()
        print(res)
except:
    print('程序异常')
print('程序继续执行')
