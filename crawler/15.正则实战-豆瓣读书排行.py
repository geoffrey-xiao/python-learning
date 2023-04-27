import json

import requests, re


class DoubanGroup():
    url = 'https://www.douban.com/group/explore'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }
    res_html = None

    def __init__(self):
        res = requests.get(self.url, headers=self.headers)
        if res.status_code == 200:
            self.res_html = res.text
            if self.parsedata():
                self.writedata()

    def parsedata(self):
        likesreg = '<div class="likes">(.*?)<br>'
        likes = re.findall(likesreg, self.res_html)
        titlereg = '<a href="https://www.douban.com/group/topic/.*/">(.*?)</a>'
        titles = re.findall(titlereg, self.res_html)
        groupreg = '<span class="from">来自<a href="https://www.douban.com/group/.*/">(.*?)</a></span>'
        groups = re.findall(groupreg, self.res_html)
        pubtimereg = '<span class="pubtime">(.*?)</span>'
        pubtimes = re.findall(pubtimereg, self.res_html)

        infos = list(zip(titles, groups, likes, pubtimes))
        print(infos)

        arr = []
        for i in infos:
            obj = {
                'title': i[0],
                'group': i[1],
                'like': i[2],
                'pubtime': i[3]
            }
            arr.append(obj)
        print(arr)
        self.data = arr;
        return True

    def writedata(self):
        with open('./doubangroup.json', 'w', encoding='utf-8') as fp:
            json.dump(self.data,fp)

DoubanGroup()