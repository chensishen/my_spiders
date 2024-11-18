import urllib.request


url = 'https://www.baidu.com/'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)

# <input type="submit" value="百度一下" id="su" class="btn self-btn bg s_btn">

from lxml import etree

tree = etree.HTML(content)

# xpath的返回值是一个列表类型数据
result = tree.xpath('//input[@id ="su"]/@value')[0]

print(result)











