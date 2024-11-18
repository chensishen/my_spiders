# 1.Selenium
# 1.什么是selenium?
# (1)selenium是一个用于web应用程序测试的工具。
# (2)selenium 测试直接运行在浏览器中，就像真正的用户在操作一样。
# (3)支持通过务种driver(firfoxDriver,IternetExplorerDriver,0peraDriver，chromeDriver)驱动真实浏览器完成测试。
# (4)selenium也是支持无界面浏览器操作的,
# 2.为什么使用selenium?模拟浏览器功能，自动执行网页中的js代码，实现动态加载
# python

import urllib.request

url = 'https://www.jd.com/'

response = urllib.request.urlopen(url)

content = response.read().decode("utf-8")

print(content)

