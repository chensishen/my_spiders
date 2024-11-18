import scrapy
from scrapy_movie.items import ScrapyMovieItem

class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["www.dy2018.com"]
    start_urls = ["https://www.dy2018.com/1/"]

    def parse(self, response):
        a_list = response.xpath('//table[@class = "tbspan"]//a[@class="ulink"][2]')
        for a in a_list:
            # 获取第一页的name 和 要点击的链接
            name = a.xpath('text()').extract_first()
            href = a.xpath('@href').extract_first()
            url = 'https://www.dy2018.com/'+href

            # 对第二页的链接发起访问
            yield scrapy.Request(url = url,callback = self.parse_second,meta={'name':name})
        pass


    def parse_second(self,response):
        # 拿不到数据的情况下 一定检查xpath语句
        src = response.xpath('//div[@id="Zoom"]//img[1]/@src').extract_first()
        # 接受到请求那个meta参数的值
        name = response.meta['name']

        movie = ScrapyMovieItem(src = src, name = name)
        yield movie




