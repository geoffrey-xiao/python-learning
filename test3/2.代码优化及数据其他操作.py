import pymysql
db = pymysql.connect(host='localhost',
                     user='root',
                     password='',
                     database='person',
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)
try:
    cursor = db.cursor()
    # sql = 'insert into user (name,age,sex) values("张三丰",100,"男");'
    # sql = 'update user set age=99 where id =11; '
    sql = 'delete from user where id=11;'
    row = cursor.execute(sql)
    print(row)
    db.commit()
    data = cursor.fetchall()
except:
    db.rollback()
finally:
    db.close()

print(data)
