import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["car.autohome.com.cn"]
    start_urls = ["https://car.autohome.com.cn/price/brand-15.html"]

    def parse(self, response):
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//div[@class="main-lever"]//span/span/text()')
        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            print(name,price)
        print('=======================')
        pass
