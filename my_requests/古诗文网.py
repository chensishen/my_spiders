import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
pytesseract.pytesseract.tesseract_cmd = r'G:\Tesseract-OCR\tesseract.exe'
# 使用 Selenium 获取动态参数
url = 'https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx'

browser = webdriver.Chrome()
browser.get(url)

# 提取动态参数
_VIEWSTATE = browser.find_element(By.ID, '__VIEWSTATE').get_attribute('value')
_VIEWSTATEGENERATOR = browser.find_element(By.ID, '__VIEWSTATEGENERATOR').get_attribute('value')
code_url = browser.find_element(By.ID, 'imgCode').get_attribute('src')

# 下载验证码图片
session = requests.Session()
response_code = session.get(code_url)
with open('code.jpg', 'wb') as f:
    f.write(response_code.content)

# 自动识别验证码
image = Image.open('code.jpg')
code_name = pytesseract.image_to_string(image).strip()

print(f"自动识别验证码为: {code_name}")
# 如果识别错误，可以手动输入验证码
if not code_name or len(code_name) != 4:  # 假设验证码为4位
    code_name = input('请输入验证码: ')

# 提交表单数据
url_post = 'https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE': _VIEWSTATE,
    '__VIEWSTATEGENERATOR': _VIEWSTATEGENERATOR,
    'from': 'http://www.gushiwen.cn/user/collect.aspx',
    'email': '911684381@qq.com',
    'pwd': 'chenyuhong0522',
    'code': code_name,
    'denglu': '登录',
}

response_post = session.post(url_post, data=data_post)

# 保存登录后的页面
with open('gushici.html', 'w', encoding='utf-8') as f:
    f.write(response_post.text)

print("登录完成！页面已保存为 gushici.html")
