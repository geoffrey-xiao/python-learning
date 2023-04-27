import time

import requests
from bs4 import BeautifulSoup
import pymysql


def getdata(i):
    url = 'https://maoyan.com/board/4'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }
    params = {
        'offset': i * 10 + 10
    }
    res = requests.get(url=url, headers=headers, params=params)
    if res.status_code == 200:
        data = res.text
        return data


def parsedata(res):
    soup = BeautifulSoup(res, 'lxml')
    dd = soup.find_all('dd')
    mlist = []
    for i in dd:
        obj = {
            'rank': i.find('i', class_="board-index").text,
            'title': i.find('p', class_='name').a.text,
            'actor': i.find('p', class_="star").text.replace('\n', '').replace('\t', '').replace('\r', '').strip(),
            'releasetime': i.find('p', class_='releasetime').text,
            'score': i.find('i', class_="integer").text + i.find('i', class_="fraction").text,
            'img': i.find('img', class_="board-img")['data-src'],
        }
        mlist.append(obj)
    print(mlist)
    return mlist


def writedata(data):
    db = pymysql.connect(
        host='localhost',
        user="root",
        password='',
        database="movies",
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        cursor = db.cursor()
        sql = f'insert into maoyan values(null,"{data["rank"]}","{data["title"]}", "{data["actor"]}", "{data["score"]}", "{data["releasetime"]}", "{data["img"]}")'
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()


def main(item):
    html = getdata(item)
    res = parsedata(html)
    for i in res:
        writedata(i)


if __name__ == '__main__':
    for i in range(4, 9):
        main(i)
        time.sleep(5)
