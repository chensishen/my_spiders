from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = 'chromedriver.exe'

browser= webdriver.Chrome()

url = 'https://www.baidu.com'

url = "https://miaosha.jd.com/"

browser.get(url)

content = browser.page_source

print(content)











