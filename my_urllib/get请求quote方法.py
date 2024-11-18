# https://www.baidu.com/s?wd=周杰伦
#https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

# 需求 获取 https://www.baidu.com/s?wd=周杰伦 的网页源码

import urllib.request
import urllib.parse


# 将字符串变为unicode编码的格式
name = urllib.parse.quote('周星驰')
print(name)

url = 'https://www.baidu.com/s?wd='

url = url + name

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)


















