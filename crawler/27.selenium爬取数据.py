from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

web = Chrome()
web.get('https://lagou.com')

btn = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
btn.click()

searchbox = web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)

itemlist = web.find_elements_by_xpath('//*[@id="jobList"]/div[1]/div')
for i in itemlist:
    # jobname = i.find_element_by_class_name('p-top__1F7CL').a.text
    jobname = i.find_element_by_xpath('./div[1]/div[1]/div[1]/a').text
    jobsalary = i.find_element_by_xpath('./div[1]/div[1]/div[2]/span').text
    jobrequire = i.find_element_by_xpath('./div[1]/div[1]/div[2]').text
    companyname = i.find_element_by_xpath('./div[1]/div[2]/div[1]/a').text
    print(jobname, jobsalary, jobrequire, companyname)
