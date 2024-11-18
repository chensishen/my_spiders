from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from streamlit import button

path = "chromedriver.exe"
service = Service(path)
browser = webdriver.Chrome(service=service)

url = "https:www.baidu.com"
browser.get(url)

# 元素定位

# 根据id来找到对象
# button = browser.find_element(by=By.ID,value='su')
# print(button)

# 根据标签的属性来获取对象
# button = browser.find_element(by=By.NAME,value='wd')
# print(button)

# 根据标签的名字获取对象
# button = browser.find_element(By.TAG_NAME, "input")
# print(button)

# 根据xpath获取对象
# button = browser.find_elements('xpath','//input[@id="su"]')
# print(button)

# 使用bs4的语法获取对象
# button = browser.find_element(By.CSS_SELECTOR, "#su")
# print(button.text)

# 查找链接
button = browser.find_element(By.LINK_TEXT, "新闻")
print(button)



