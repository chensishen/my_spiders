import scrapy
from IPython.core.formatters import format_display_data
import json

from doc.pycurl.examples.quickstart.response_headers import encoding


class TestpostSpider(scrapy.Spider):
    name = "testpost"
    allowed_domains = ["fanyi.baidu.com"]
    # post请求没有参数这个请求没有任何意义
    # 所以start_urls 也没有用
    # parse方法也没有用了
    # start_urls = ["https://fanyi.baidu.com/sug"]
    #
    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw':'final'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        obj = json.loads(content)
        print(obj)