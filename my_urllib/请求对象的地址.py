import urllib.request

url = "https://www.baidu.com"

# url的组成
#https://www.baidu.com/s?&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

#http/https    www.baidu.com   80/443     s   wd = 周杰伦        #
# 协议            主机           端口号      路径     参数        锚点
# http 80
# https 443
# mysql 3306
# oracle 1521
# redis 6379
# mongodb 27017

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'}

# 因为urlopen方法中不能存储字典 headers不能传递进去
# 请求对象定制
# 注意 因为参数顺序原因的问题 不能直接写url 和 headers  中间还有data  所以用关键字传参

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)





