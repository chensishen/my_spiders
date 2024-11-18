import requests
from sqlalchemy.dialects.mssql.information_schema import views

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# 通过登录进入主页面
url = 'https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    'cookie': 'login=flase; ASP.NET_SessionId=loregu3afr5ustjucnqlo21w; gswZhanghao=911684381%40qq.com; wsEmail=911684381%40qq.com; ticketStr=200521909%7cgQHi8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAyQTZoLVFPbGVkN2kxbW5ndU5EMXAAAgSXwzZnAwQAjScA; codeyz=8dac80e0009315d9',
    'priority': 'u=0, i',
    'referer': 'https://www.gushiwen.cn/user/login.aspx?from=http//www.gushiwen.cn/user/collect.aspx',
    'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-'
}

# browser = webdriver.Chrome()
# browser.get(url)
# I1 = browser.find_element(By.ID,'__VIEWSTATE')
# _VIEWSTATE = I1.get_attribute('value')
# I2 = browser.find_element(By.ID,'__VIEWSTATEGENERATOR')
# _VIEWSTATEGENERATOR = I2.get_attribute('value')
# C = browser.find_element(By.ID,'imgCode')
# code = C.get_attribute('src')
# print(_VIEWSTATE)
# print(_VIEWSTATEGENERATOR)
# print(code)

# 通过登录接口发现，登录的时候需要的参数很多
# _VIEWSTATE: 7e/3ZT7DEioTwtrhXX4YxtqueKK3c+SAJmMGA4I9S4En8ykoKbvAew6S6hrgq+yFGHgla85LO4TPvO69JbhsTh2LGcn3Cq5QmQKnI5faHnbQ9ONktUFm+0hoQIWNTfLB5kQQxFonE3kdzE+XvLdFAXekiko=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://www.gushiwen.cn/user/collect.aspx
# email: 911684381@qq.com
# pwd: sasda123225
# code: 3YOU
# denglu: 登录

# 我们观察到_VIEWSTATE: __VIEWSTATEGENERATOR:  code: 是一个变化的量

# 难点:1._VIEWSTATE:  __VIEWSTATEGENERATOR: 一般情况下看不到的数据 都是页面源码中
#   观察到这俩个数据在页面的源码中，所以我们需要获取源码 然后进行解析就可以获取了
#        2.验证码

response = requests.get(url, headers=headers)
content = response.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(content, 'lxml')
_VIEWSTATEGENERATOR = soup.select('#__VIEWSTATEGENERATOR')[0].attrs['value']
_VIEWSTATE = soup.select('#__VIEWSTATE')[0].attrs['value']
code = soup.select('#imgCode')[0].attrs['src']

# 获取验证码图片

# import urllib.request
# urllib.request.urlretrieve(code_url, 'code.png')
# requests里有个方法session() 通过session的返回值 就能使用请求变成一个对象
code = 'https://www.gushiwen.cn' + code
print(code)

session = requests.Session()
response_code = session.get(code)
content_code = response_code.content
# wb的模式是二进制
with open('code.jpg', 'wb') as f:
    f.write(content_code)

# 获取验证码的图片之后 下载到本地 然后观察验证码 然后在控制台输入验证码 就可以将这个值给
# code参数 就可以登录

code_name = input('请输入你的验证码')

url_post = 'https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx'

data_post = {
    '__VIEWSTATE':_VIEWSTATE,
    '__VIEWSTATEGENERATOR':_VIEWSTATEGENERATOR,
    'from':'http://www.gushiwen.cn/user/collect.aspx',
    'email':'911684381@qq.com',
    'pwd':'chenyuhong0522',
    'code':code_name,
    'denglu':'登录',
}

response_post = session.post(url_post, data=data_post)
content_post = response_post.text

with open('gushiwen.html', 'w',encoding='utf-8') as f:
    f.write(content_post)

# 难点
# 1.隐藏域
# 2.验证码