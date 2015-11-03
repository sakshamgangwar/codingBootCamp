from scrapy.spider import BaseSpider

class WebSpider1(BaseSpider):
    name = "spider1"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/Amazon.com"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)