# urlencode 多个参数使用

# https://www.baidu.com/s?wd=周杰伦&sex=男
import urllib.request
import urllib.parse

from 请求对象的地址 import headers

data={
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}

a = urllib.parse.urlencode(data)
print(a)

base_url = 'https://www.baidu.com/s?'

url = base_url+a

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'}

request = urllib.request.Request(url, headers=headers)

response  = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)




