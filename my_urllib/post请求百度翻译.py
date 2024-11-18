import urllib.request
import urllib.parse

from 请求对象的地址 import headers, request

url = "https://fanyi.baidu.com/sug"

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'}

data= {
    'kw':'spider'
}

data = urllib.parse.urlencode(data).encode('utf-8')

# print(data)

# post请求的参数不是拼接在url后面，而是放在请求对象定制的参数中
# post请求的参数，必须要进行编码
request = urllib.request.Request(url, data, headers)

response = urllib.request.urlopen(request)

# print(response)
content = response.read().decode('utf-8')

# print(content)
#
# print(type(content))
#
# import json
#
# obj = json.loads(content)
# print(obj)




