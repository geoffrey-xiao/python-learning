import requests
from lxml import etree
import os


def getdata():
    url = 'https://movie.douban.com/cinema/nowplaying/xian/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.text
        return data
    else:
        return None


def parsedata(data):
    try:
        html = etree.HTML(data)
        posts = html.xpath('//ul[@class="lists"]//img[@class=""]/@src')
        print(posts)
        return posts
    except:
        return None


def downloaddata(data, dir):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }
    if not os.path.exists(dir):
        os.mkdir(dir)
    x = 0
    for i in data:
        res = requests.get(url=i, headers=headers)
        with open(f'{dir}/{x}.jpg', 'wb') as fp:
            fp.write(res.content)
        x += 1


def main():
    html = getdata()
    if html:
        res = parsedata(html)
        downloaddata(res,'./douban')


main()
