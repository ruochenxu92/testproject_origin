__author__ = 'Xiaomin'
__author__ = 'Xiaomin'

from scrapy.spider import Spider
from scrapy.utils.response import open_in_browser
import scrapy
import datetime
import os
from tutorial.items import WikiItem



class IMDBReviewSpider(Spider):
    hostname = 'http://www.imdb.com/'
    name = 'cs499urls'
    #allowed_domains = ['http://cs.illinois.edu']
    start_urls = ['http://arxiv.org/archive/cs']


    def parse(self, response):
        for url in response.xpath('//*[@id="content"]/ul[2]/li/a[1]'):
            item = WikiItem()
            item['name'] = url.xpath('@href').extract()[0]
            yield item



