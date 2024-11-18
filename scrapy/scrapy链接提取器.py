# Crawlspider
# 1.继承自scrapy.spider
# 2.独门秘笈
# crawlspider可以定义规则，再解析htm1内容的时候，可以根据链接规则提取出指定的链接，然后再向这些链接发送请求
# 所以，如果有需要跟进链接的需求，意思就是爬取了网页之后，需要提取链接再次爬取，使用crawlspider是非常合适的


# 3.提取链接
# 链接提取器，在这里就可以写规则提取指定链接
# scrapy.linkextractorg.LinkExtractor(
#                            allow=()，#正则表达式，提取符合正则的链接
#                            deny =()，#(不用)正则表达式不提取符合正则的链接
#                            allow domains =(),#(不用)允许的域名
#                            deny_domains=(),#(不用)不允许的域名
#                            restrict_xpaths=()，#xpath，提取符合xpath规则的链接
#                            restrict_css=(),#提取符合选择器规则的链接)
# 4.模拟使用正
# 则用法:links1=LinkExtractor(allow=r'list 23 \d+\.html')
# xpath用法:links2 =LinkExtractor(restrict xpaths=r'//div[@class="x"]')
# css用法:links3 =LinkExtractor(restrict css='.x')
# 5.提取连接
# link.extract links(response)
# 6.注意事项
# 【注1】callback只能写函数名字符串，callback='parse item'
# 【注2】在基本的spider中，如果重新发送请求，那里的callback写的是callback=self.parse item
# 【注.稍后看】follow=true 是否跟进 就是按照提取连接规则进行提取