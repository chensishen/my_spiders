# urllib

# 1.一个类型和六个方法
# 2.get请求
# 3.post请求  百度翻译
# 4.ajax的get请求
# 5.ajax的post的请求
# 6.cookie登录
# 7.代理

# requests
# 1.一个类型六个属性
# 2.get请求
# 3.post请求
# 4.代理
# 5.cookie 验证码

import requests

url = 'https://www.baidu.com/s'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

data = {
    'wd':'北京'
}
# url 请求资源路径  params参数  kwargs字典
requests = requests.get(url,params=data, headers=headers)

content = requests.text

print(content)

# 总结
# 1.参数用params传递
# 2.参数不需要urlencode编码
# 3.不需要请求对象定制
# 4.请求资源路径中的？可以加也可以不加