__author__ = 'Xiaomin'

from scrapy.spider import Spider
from tutorial.items import ArticleItem, AuthorItem, PaperItem, FieldItem, InterestItem
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
        listOfInterest = response.xpath('//*[@id="gsc_prf_i"]/div[4]/a/text()').extract()
        for interest in listOfInterest:
            item = InterestItem()
            item['name'] = interest
            return item





