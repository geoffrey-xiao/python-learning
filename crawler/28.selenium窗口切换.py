from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

import time

web = Chrome()

web.get('https://lagou.com')

web.find_element_by_xpath('//*[@id="cboxClose"]').click()

time.sleep(1)

web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)

web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()

# 打开新窗口
web.switch_to.window(web.window_handles[-1])

#在新窗口获取数据
job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text

print(job_detail)

# 关闭新窗口
web.close()

web.switch_to.window(web.window_handles[0])
job_name = web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').text
print(job_name)