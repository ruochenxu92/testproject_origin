__author__ = 'Xiaomin'

from scrapy.spider import Spider
from tutorial.items import ArticleItem, PageItem, WikiItem
from scrapy.utils.response import open_in_browser
import scrapy
import datetime


class DBSpider(Spider):
    #hostname = 'https://scholar.google.com/'
    name = 'db'
    #allowed_domains = ['http://cs.illinois.edu']
    start_urls = ['file://localhost/Users/Xiaomin/0.html']

    '''
    Parse all interests
    '''
    def parse(self, response):
        listOfInterest = response.xpath('').extract()
        for interest in listOfInterest:
            # item = PageItem()
            # item['name'] = interest
            item = WikiItem()
            item['name'] = interest
            return item





