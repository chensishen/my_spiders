from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "chromedriver.exe"
service = Service(path)
browser = webdriver.Chrome(service=service)

url = 'https://www.baidu.com'

browser.get(url)

import time
time.sleep(2)

# 获取文本框的对象
inuput = browser.find_element(By.XPATH, '//*[@id="kw"]')

# 输入周杰伦
inuput.send_keys('周杰伦')

time.sleep(2)

# 获取百度一下的按钮
button  = browser.find_element(By.XPATH, '//*[@id="su"]')

# 点击按钮
button.click()

time.sleep(2)

# 滑到底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

time.sleep(2)

# 获取下一页的按钮
next = browser.find_element(By.CLASS_NAME,"n")

# 点击下一页
next.click()

time.sleep(2)

# 回到上一页
browser.back()
time.sleep(2)

# 回去
browser.forward()

time.sleep(3)

# 推出
browser.quit()













