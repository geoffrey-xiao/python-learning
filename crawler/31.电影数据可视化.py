from selenium.webdriver import Chrome

web = Chrome()

web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')

trs = web.find_elements_by_xpath('//*[@id="TableList"]/table/tbody/tr')

fp = open('./movie.csv', 'a')
for i in trs:
    tds = i.find_elements_by_xpath('./td')
    for td in tds:
        fp.write(td.text.replace(',', ''))
        fp.write(',')
    fp.write('\n')
