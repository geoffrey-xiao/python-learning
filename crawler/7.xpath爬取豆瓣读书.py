import requests,json

from lxml import etree

url = 'https://book.douban.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
}

res = requests.get(url=url, headers=headers)
# if res.status_code == 200:
# print(res.text)
# 将爬取的数据写入文件
# with open('./doubanbook.html','w') as fp:
#     fp.write(res.text)
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
print(arr)
with open('./doubanbook.text','w') as fp:
    json.dump(arr,fp)
