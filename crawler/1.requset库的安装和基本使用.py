import requests

url = 'https://baidu.com'

res=requests.get(url=url)
print(res)
print(res.content)
print(res.content.decode('utf-8'))
print(res.text)
print(res.headers)
print(res.status_code)
print(res.url)
print(res.request.headers)