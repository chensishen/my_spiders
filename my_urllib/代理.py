# 1.代理的常用功能?
#   1.突破自身IP访问限制，访问国外站点。
#   2.访问一些单位或团体内部资源
#   扩展:某大学FTP(前提是该代理地址在该资源的允许访问范围之内)，使用教育网内地址段免费代理服务器，就可以用于对教育网开放的各类FTP下载上传，以及各类资料查询共享等服务。
#   3.提高访问速度
#   扩展:通常代理服务器都设置一个较大的硬盘缓冲区，当有外界的信息通过时，同时也将其保存到缓冲区中，当其他用户再访问相同的信息时，则直接由缓冲区中取出信息，传给用户，以提高访问速度，4.隐藏真实IP
#   扩展:上网者也可以通过这种方法隐藏自己的IP，免受攻击，
# 2.代码配置代理
# 创建Reugest对象
# 创建ProxyHandler对象
# 用handler对象创建opener对象
# 使用opener.open函数发送请求

import urllib.request

from 请求对象的地址 import content, response

url = 'https://www.baidu.com/s?wd=ip'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
    }

request = urllib.request.Request(url, headers=headers)

# response = urllib.request.urlopen(request)
#
# content = response.read().decode('utf-8')

proxies = {
    'http':'202.101.213.14:17152'
}

handler = urllib.request.ProxyHandler(proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('ip.html', 'w',encoding='utf-8') as f:
    f.write(content)










