import requests

varstr = '''
**************************
**************************
***请输入需要翻译的内容 ：****
***输入字母q 退出翻译 *******
**************************
**************************
'''
print(varstr)


def translate(kw):
    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }
    data = {
        'i': kw,
        'doctype': 'json'
    }
    res = requests.post(url, headers=headers, data=data)
    if res.status_code == 200:
        content = res.json()
        if content['errorCode'] == 0:
            result = content['translateResult'][0][0]['tgt']
            print(result)
        else:
            print('翻译失败，请稍后重试')


while True:
    kw = input('请输入您需要翻译的内容：')
    if kw == 'q':
        break
    translate(kw)
