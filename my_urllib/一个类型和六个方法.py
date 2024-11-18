import urllib.request

url = "http://www.baidu.com"

response = urllib.request.urlopen(url)

# 一个类型和六个方法
# HTTPResponse类型
# print(type(response))

# 按照一个字节一个字节读
# content = response.read()
# print(content)

# content = response.read(5)
# print(content)

# 按行读取
# content = response.readline()
# print(content)

# content = response.readlines()
# print(content)

# 返回200就没有错
# print(response.getcode())
#
# print(response.geturl())
#
# print(response.getheaders())

# print(response.info())
