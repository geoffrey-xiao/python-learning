import requests
from lxml import etree

# username = input('请输入用户名：')
# pwd = input('请输入密码:')

loginurl = 'https://api.lmonkey.com/api/login'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'authorization': 'Bearer',
}
data = {
    'password': "hard456abc",
    'username': "summer666"
}
req = requests.session()
res = req.post(url=loginurl, headers=headers, data=data)
print(res)
if res.status_code == 200:
    print(res)
