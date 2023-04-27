import json
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--disable-blink-features=AutomationControlled")

web = Chrome(options=opt)

arr = []


def getdata(i):
    web.get(f'http://quotes.toscrape.com/page/{i + 1}')
    nextbtn = web.find_element_by_xpath('/html/body/div/div[2]/div[1]/nav/ul/li[@class="next"]/a')
    quotes = web.find_elements_by_xpath('/html/body/div/div[2]/div[1]/div')
    for i in quotes:
        obj = {
            'text': i.find_element_by_xpath('./span[1]').text,
            'author': i.find_element_by_xpath('./span[2]').text,
            'tags': i.find_element_by_xpath('./div').text
        }
        arr.append(obj)
    nextbtn.click()


for i in range(3):
    getdata(i)
    time.sleep(3)
with open('./toscrape.json', 'a+', encoding='utf-8') as fp:
    json.dump(arr, fp, ensure_ascii=False)

print(arr)
web.close()
