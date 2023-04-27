import json

import requests
from bs4 import BeautifulSoup


class Reveiew():
    url = 'https://book.douban.com/review/best/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }

    html = None

    data = None

    def __init__(self):
        res = requests.get(url=self.url, headers=self.headers)
        if res.status_code == 200:
            self.html = res.text
            if self.parsedata():
                self.writedata()
        else:
            print('请求失败')

    def parsedata(self):
        soup = BeautifulSoup(self.html, 'lxml')
        try:
            data = soup.find_all('div', class_="main review-item")
            arr = []
            for i in data:
                bookurl = i.find('a', class_="subject-img")['href']
                author = i.find('a', class_="name").text
                publictime = i.find('span', class_="main-meta").text
                title = i.find('div', class_="main-bd").h2.a.text
                vardict = {'author': author, 'url': bookurl, 'title': title, 'publictime': publictime}
                arr.append(vardict)
            self.data = arr
            return True
        except:
            return False

    def writedata(self):
        # print(data)
        if self.data != []:
            with open('./douban1.json', 'w') as fp:
                json.dump(self.data, fp)
        else:
            print('写入失败')


if __name__ == '__main__':
    Reveiew()
