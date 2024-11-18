from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = "chromedriver.exe"
service = Service(path)
browser = webdriver.Chrome(service=service)

url = "http://www.baidu.com"

browser.get(url)

input = browser.find_element(By.ID, "su")

print(input.get_attribute("class"))
print(input.get_attribute("value"))
print(input.tag_name)

button = browser.find_element(By.LINK_TEXT, "新闻")
print(button.text)















