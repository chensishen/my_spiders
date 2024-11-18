import requests

url = 'http://www.baidu.com'

response = requests.get(url)

# 一个类型和六个属性

# Response类型
# print(type(response))

# 设置响应的编码格式
# response.encoding='utf-8'

# 以字符串的形式返回网页源码
# print(response.text)

# 返回url地址
# print(response.url)

# 返回二进制数据
# print(response.content)

# 返回响应状态码
# print(response.status_code)

# 返回响应头
# print(response.headers)

