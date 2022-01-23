import scrapy


class UniversitySpider(scrapy.Spider):
    name = 'university'
    allowed_domains = ['sample-university-site.herokuapp.com']
    start_urls = ['http://sample-university-site.herokuapp.com/']

    def parse(self, response):
        pass
