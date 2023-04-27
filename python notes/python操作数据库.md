```python
'''
1.链接mysql数据库
2。创建游标对象
3。准备sql
4。用游标对象执行sql
5。提取数据
6。关闭数据库链接
'''

import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='',
                     database='person',
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

sql = 'select version()'

cursor.execute(sql)

data = cursor.fetchall()

db.close()

print(data)
```

