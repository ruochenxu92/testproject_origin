__author__ = 'Xiaomin'

from scrapy.spider import Spider
from scrapy.utils.response import open_in_browser
import scrapy
import os
from tutorial.items import ReviewItem, cs499Item
import lxml.html
import datetime
import json
from pytz import timezone


def getUrls():
    path = os.path.abspath('/Users/Xiaomin/testproject/tutorial/cs499.json')
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

# //*[@id="dlpage"]/dl[1]/   dd[1]/div/div[1]
# //*[@id="dlpage"]/dl[1]/   dd[2]/div/div[1]
# //*[@id="dlpage"]/dl[1]/   dd[3]/div/div[1]

#//*[@id="dlpage"]/dl[1]/dd[1]/div[1]/div[1]

    #//*[@id="dlpage"]/dl[1]/dd[1]/div[1]/div[1]/text()
    def parse(self, response):
        i = 1

        print response.xpath('//*[@id="dlpage"]/dl/dd[1]/div/div[1]/text()').extract()[0]
        prefix = 'http://arxiv.org'

        for sel in response.xpath('//*[@id="dlpage"]/dl[1]/dt'):
            item = cs499Item()
            item['urllink'] = prefix + sel.xpath('span/a[1]/@href').extract()[0]
            item['pdflink'] = prefix + sel.xpath('span/a[2]/@href').extract()[0]

            date_str = str(datetime.datetime.now())
            datetime_obj_naive = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            datetime_obj_central = timezone('US/Central').localize(datetime_obj_naive)
            item['date'] =datetime_obj_central

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




