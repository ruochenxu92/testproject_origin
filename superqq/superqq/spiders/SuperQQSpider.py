__author__ = 'Xiaomin'

from scrapy.spider import Spider
from scrapy.utils.response import open_in_browser
import scrapy
import os
from superqq.items import PaperItem
import datetime
import json


def getUrls():
    path = os.path.abspath('/Users/Xiaomin/testproject/superqq/cs499.json')
    jf = open(path)
    data = json.load(jf)
    urls = []
    for url in data:
        urls.append('http://arxiv.org' + url['name'])
    return urls

class CS499Spider(Spider):
    hostname = 'http://arxiv.org'
    name = 'cs499'
    #allowed_domains = ['http://cs.illinois.edu']
    start_urls = getUrls()

    def __init__(self):
        self.count = 0

    def parse(self, response):
        i = 1

        # print response.xpath('//*[@id="dlpage"]/dl/dd[1]/div/div[1]/text()').extract()[0]
        prefix = 'http://arxiv.org'

        for sel in response.xpath('//*[@id="dlpage"]/dl[1]/dt'):
            item = PaperItem()
            item['urllink'] = prefix + sel.xpath('span/a[1]/@href').extract()[0]
            item['pdflink'] = prefix + sel.xpath('span/a[2]/@href').extract()[0]
            item['date'] = str(datetime.datetime.now())
            item['category'] = response.xpath('//*[@id="dlpage"]/h1/text()').extract()[0]
            seeMore = item['urllink']
            request = scrapy.Request(seeMore, callback=self.parseMovieDetails)
            request.meta['item'] = item
            i += 1
            yield request


    def parseMovieDetails(self,response):
        item = response.meta['item']
        buffer = ''
        for content in response.xpath('//*[@id="abs"]/div[2]/div[2]/a'):
            buffer += content.xpath('text()').extract()[0] + ', '
        item['authors'] = buffer[:-1]
        item['title']   = response.xpath('//*[@id="abs"]/div[2]/h1/text()').extract()[0]
        item['subjects'] = response.xpath('//*[@class="primary-subject"]/text()').extract()[0]
        abstract = response.xpath('//*[@id="abs"]/div[2]/blockquote').extract()[0]
        item['abstract'] = abstract[78:-13] #delete the tag part
        return item



