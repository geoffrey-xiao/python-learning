'''
pickle.dumps() 序列化--将数据转为二进制数据类型
pickle.loads() 反序列化--将二进制数据类型转为普通数据类型
'''

import pickle

vars = {'name': 'summer', 'age': 3, 'sex': 'female'}
# with open('./data1.txt', 'wb') as fp:
#     fp.write(pickle.dumps(vars))

with open('./data1.txt', 'rb') as fp:
    res = fp.read()
    vardict = pickle.loads(res)
    print(vardict)
