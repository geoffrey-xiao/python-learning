import json
import time

import requests

from bs4 import BeautifulSoup


# 获取数据
def getdata(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }
    try:
        res = requests.get(url=url, headers=headers)
        if res.status_code == 200:
            data = res.text
            return data
    except:
        return None


# 解析数据
def parsedata(data):
    soup = BeautifulSoup(data, 'lxml')
    ol = soup.find('ol', class_="grid_view")
    ranks = ol.find_all('em', class_="")
    imgs = ol.find_all('img', class_="")
    titles = ol.find_all('span', class_="title")
    stars = ol.find_all('span', class_="rating_num")
    quotes = ol.find_all('span', class_="inq")
    arr = []
    for i in range(len(ranks)):
        mv = {
            'rank': ranks[i].text,
            'title': titles[i].text,
            'image': imgs[i]['src'],
            'start': stars[i].text,
            'quote': quotes[i].text,
        }
        arr.append(mv)
    print(arr)
    return arr


# 写入数据
def writedata(data):
    with open('./doubanmovie.json', 'a+', encoding='utf-8') as fp:
        json.dump(data, fp, ensure_ascii=False)
        fp.write('\n')


def main(num):
    url = f'https://movie.douban.com/top250?start={num * 25}&filter='
    res = getdata(url)
    if res:
        html = parsedata(res)
        for i in html:
            writedata(i)


if __name__ == '__main__':
    for i in range(3):
        main(i)
        time.sleep(3)
