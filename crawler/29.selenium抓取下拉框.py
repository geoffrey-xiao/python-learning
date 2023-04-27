# 抓取伊恩票房
import json

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
opt.add_argument("--disable-blink-features=AutomationControlled")
web = Chrome(options=opt)

web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')

sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')

sel = Select(sel_el)
arr = []
for i in range(len(sel.options)):
    sel.select_by_index(i)
    time.sleep(3)
    trs = web.find_elements_by_xpath('//*[@id="TableList"]/table/tbody/tr')
    for item in trs:
        obj = {
            'ranking': item.find_element_by_xpath('./td[1]').text,
            'title': item.find_element_by_xpath('./td[2]/a/p').text,
            'type': item.find_element_by_xpath('./td[3]').text,
            'total': item.find_element_by_xpath('./td[4]').text,
            'price': item.find_element_by_xpath('./td[5]').text,
            'persons': item.find_element_by_xpath('./td[6]').text,
            'region': item.find_element_by_xpath('./td[7]').text,
        }
        arr.append(obj)

print(arr)
print(len(arr))
web.close()
for i in arr:
    with open('./yienmovie.json', 'a+', encoding='utf-8') as fp:
        json.dump(i, fp, ensure_ascii=False)
        fp.write('\n')
