import requests
from conda.common.serialize import json_load

url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

data = {
    'kw':'love'
}

# url 请求地址
# data 请求参数
# kwargs 字典

response = requests.post(url, headers=headers, data=data)

content = response.text
print(content)

import json
obj = json_load(content)
print(obj)

# 总结
# 1.post请求不需要编解码
# 2.post请求的参数是data
# 3.不需要对象的定制








