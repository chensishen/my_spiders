import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["gz.58.com"]
    start_urls = ["https://gz.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91"]

    def parse(self, response):
        content = response.text
        # content = response.body
        print(content)
        print('==============================')
        span = response.xpath('//div[@id="filter"]//span')[0]
        print(span.extract())

