import time

from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    data = model('select * from msgboard')
    print(data)
    return render_template('index.html', data=data)


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/insert', methods=['POST'])
def insert():
    data = request.form.to_dict()
    print(data)
    data['date'] = time.strftime('%Y-%m-%d %H:%M:%S')
    sql = f'insert into msgboard values(null,"{data["nickname"]}","{data["message"]}","{data["date"]}")'
    print(sql)
    res = model(sql)
    if res:
        return '<script>alert("留言成功");location.href="/"</script>'
    else:
        return '<script>alert("留言失败");location.href="/add"</script>'


@app.route('/delete')
def delete():
    id = request.args.get('id')
    print(id)
    sql = f'delete from msgboard where id={id}'
    res = model(sql)
    if res:
        return '<script>alert("删除留言成功");location.href="/"</script>'
    else:
        return '<script>alert("删除留言失败");location.href="/"</script>'


def model(sql):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='',
                         database='infoboard',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)

    try:
        cursor = db.cursor()
        row = cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        if data:
            return data
        else:
            return row
    except:
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port='8080')
