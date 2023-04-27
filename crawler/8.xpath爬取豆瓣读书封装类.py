import requests, json

from lxml import etree


class Douban():
    url = 'https://book.douban.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    }

    data = None

    filepath = './doubanbook.text'

    def __init__(self):
        res = requests.get(url=self.url, headers=self.headers)
        if res.status_code == 200:
            with open('./doubanbook.html', 'w') as fp:
                fp.write(res.text)
            if self.parsedata():
                self.writedata()

    def parsedata(self):
        # 解析数据
        html = etree.parse('./doubanbook.html', etree.HTMLParser())
        author = html.xpath(
            '//div[@class="article"]/div[contains(@class,"popular-books")]//div[@class="info"]/p[@class="author"]/text()')
        title = html.xpath(
            '//div[@class="article"]/div[contains(@class,"popular-books")]//div[@class="info"]/h4[@class="title"]/a/text()')
        mark = html.xpath(
            '//div[@class="article"]/div[contains(@class,"popular-books")]//div[@class="info"]//span[@class="average-rating"]/text()')
        print(mark)
        arr = []
        for i in range(len(author)):
            obj = {'author': author[i], 'title': title[i], 'mark': mark[i]}
            arr.append(obj)
        self.data = arr
        return True

    def writedata(self):
        with open(self.filepath, 'w') as fp:
            json.dump(self.data, fp)

Douban()