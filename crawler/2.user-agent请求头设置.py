import requests

# url = 'https://www.lmonkey.com/'
url = 'http://www.xiladaili.com/gaoni/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}
res = requests.get(url=url, headers=headers)
code = res.status_code
print(code)
if res.status_code == 200:
    with open('./test.html', 'w') as fp:
        fp.write(res.text)
