import requests

url = 'http://httpbin.org/get'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}

proxies = {
    'http': '45.228.188.241:999',
    'https': '45.228.188.241:999'
}
try:
    res = requests.get(url, headers=headers, proxies=proxies,timeout=5)
    print(res.content)
    if res.status_code == 200:
        data = res.json()
        print(data['origin'])
except:
    print('请求异常')
