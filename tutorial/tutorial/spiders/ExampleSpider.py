__author__ = 'Xiaomin'

from scrapy.spider import BaseSpider
from tutorial.items import ArticleItem

import datetime

class ExampleSpider(BaseSpider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']

    def parse(self, response):
        return ArticleItem(title='X', body='x', likes=1, pub_date=datetime.datetime.now())

