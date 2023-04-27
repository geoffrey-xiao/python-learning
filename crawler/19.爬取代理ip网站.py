# 1.发送请求获取数据
import json
import time

import requests
from bs4 import BeautifulSoup


def getdata(num):
    print('获取数据')
    url = f'http://www.nimadaili.com/gaoni/{num}/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.text
        return data
    else:
        return False


# 2.处理数据
def parsedata(data):
    print('处理数据')
    soup = BeautifulSoup(data, 'lxml')
    table = soup.find_all("tr")
    arr = []
    for i in table:
        if i.td:
            arr.append(i.td.text)
    print(arr)
    return arr


# 3.写入数据
def writedata(data):
    print('写入数据')
    with open('./iptest.text', 'a+', encoding='utf-8') as fp:
        json.dump(data, fp)


if __name__ == '__main__':
    for i in range(1, 3):
        res = getdata(i)
        time.sleep(2)
        data = parsedata(res)
        writedata(data)
