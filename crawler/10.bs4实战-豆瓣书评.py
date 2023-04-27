import json

import requests
from bs4 import BeautifulSoup

url = 'https://book.douban.com/review/best/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

res = requests.get(url=url, headers=headers)
if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'lxml')
    data = soup.find_all('div', class_="main review-item")
    arr = []
    for i in data:
        bookurl = i.find('a', class_="subject-img")['href']
        author = i.find('a', class_="name").text
        publictime = i.find('span', class_="main-meta").text
        title = i.find('div', class_="main-bd").h2.a.text
        vardict = {'author': author, 'url': bookurl, 'title': title, 'publictime': publictime}
        arr.append(vardict)
        # print(data)
    with open('./douban.json', 'w') as fp:
        json.dump(arr, fp)
