# 1.什么是scrapy shell?
# Scrapy终端，是一个交互终端，供您在未启动spider的情况下尝试及调试您的爬取代码。
# 其本意是用来测试提取数据的代码，不过您可以将其作为正常的Python终端，
# 在上面测试任何的Python代码。该终端是用来测试xPath或css表达式，
# 查看他们的工作方式及从爬取的网页中提取的数据。
# 在编写您的spider时，该终端提供了交互性测试您的表达式代码的功能，
# 免去了每次修改后运行spider的麻烦。
# 一旦熟悉了scrapy终端后，您会发现其在开发和调试spider时发挥的巨大作用。
# 进入scrapy shell 直接进入window的终端中输入scrapy shell 域名
# 如果想看到一些高亮 或者 自动补全 可以安装ipython

import time

for i in range(10):
    print(int(time.time()))
    time.sleep(1)








