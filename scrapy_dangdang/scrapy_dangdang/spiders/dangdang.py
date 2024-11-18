import scrapy
from scrapy_dangdang.items import ScrapyDangdangItem


class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    # 如果多页下载，要调整范围
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/cp01.03.45.00.00.00.html"]
    # https://category.dangdang.com/pg2-cp01.03.45.00.00.00.html

    base_url = "https://category.dangdang.com/pg"
    page = 1

    def parse(self, response):
        # pipelines 下载数据
        # item 定义数据结构
        # 下载的数据都有什么
        # src = '//ul[@id="component_59"]/li//img/@src'
        # name = '//ul[@id="component_59"]/li//img/@alt'
        # price = '//ul[@id="component_59"]/li//p/span[@class="search_now_price"]/text()'
        # 所有的seletor的对象 都可以再次调用xpath方法
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            # 第一章图片和其他的图片的标签属性不一样
            src = li.xpath('.//img/@data-original').extract_first()
            if not src:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p/span[@class="search_now_price"]/text()').extract_first()
            book = ScrapyDangdangItem(src=src, name=name, price=price)
            # 获取一个book就将book交给管道
            yield book
        pass

        # 每一页的爬取的业务逻辑是一样的，使用我们只需要执行那个页的请求再次调用parse方法
        # 就可以了
        if self.page < 10:
            self.page += 1
            url = self.base_url + str(self.page) + '-cp01.03.45.00.00.00.html'
        # 怎么调用parse方法
        # scrapy.Request就是scrapy的get请求
        # url请求地址 callback是执行的函数
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
