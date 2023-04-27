import requests

url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}
data = {
    'i': '你好世界',
    'doctype': 'json'
}

res = requests.post(url, headers=headers, data=data)
print(res.status_code)
if res.status_code == 200:
    content = res.json()
    if content['errorCode'] == 0:
        result = content['translateResult'][0][0]['tgt']
        print(result)
