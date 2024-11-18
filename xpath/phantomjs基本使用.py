from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# path = 'chromedriver.exe'
# service = Service(path)
#
# # 配置 Chrome 选项以启用无头模式
# chrome_options = Options()
# chrome_options.add_argument('--headless')  # 启用无头模式
# # chrome_options.add_argument('--disable-gpu')  # 可选，提升兼容性
# # chrome_options.add_argument('--no-sandbox')  # 可选，避免沙盒问题
#
# # 目前不支持
# # browser = webdriver.PhantomJS(path)
#
# # 使用无头模式下的 Chrome 初始化浏览器
# browser = webdriver.Chrome( options=chrome_options)
#
# url = 'https://www.baidu.com/'
#
# browser.get(url)
#
# browser.save_screenshot('baidu.png')
#
# import time
# time.sleep(2)
#
# input = browser.find_element(By.XPATH, '//*[@id="kw"]')
#
# input.send_keys('周杰伦')
#
# time.sleep(2)
#
# browser.save_screenshot('周杰伦.png')

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 启用无头模式
    browser = webdriver.Chrome(options=chrome_options)
    return browser



