__author__ = 'Xiaomin'

from scrapy.spider import BaseSpider
from tutorial.items import ArticleItem, WikiItem
from scrapy.utils.response import open_in_browser
import scrapy
import datetime
import os
from scrapy import log
import json

def getStartUrls():
    start_urls = []
    json_data=open('actor4.json')
    data = json.load(json_data)
    json_data.close()
    for entry in data:
        start_urls.append(entry['name'])
    return start_urls



#
# start_urls = getStartUrls()

# def getStartUrls():
#     path = os.path.abspath("/Users/Xiaomin/testproject/tutorial/.txt")
#     f = open(path)
#     listOfProfessors = f.read().split('\n')
#     return listOfProfessors

'''
spider for crawling authors information
'''
class IMDBSpider(BaseSpider):
    hostname = 'http://www.imdb.com'
    name = 'imdbreal'
    allowed_domains = [hostname]
    start_urls = getStartUrls()

    def parse(self, response):
        for url in response.xpath('//*[@id="filmography"]/div[2]/div/b/a'):
            wiki = WikiItem()
            str = self.hostname + url.xpath('@href').extract()[0]
            print str
            self.log("Fetch group home page: %s" % response.url)
            wiki['name'] = str
            wiki['value'] = str
            yield wiki

    # def parse_page2(self,response):
    #     #url = response.xpath('//*[@id="gsc_a_ta"]/a/text()').extract()[0]
    #     #author['institution'] = response.xpath('//*[@id="gsc_prf_i"]/div[3]/text()').extract()[0]
    #     items = response.meta['item']
    #     for sel in response.xpath('//*[@id="gsc_prf_i"]/div[4]/a'):
    #         interest_area = sel.xpath('/text()').extract()[0]
    #         items.append(interest_area)
    #         print "interest:",interest_area
    #     return items
    #     return ArticleItem(title=url, body=url, likes =1, pub_date='2001-1-1')
    #
    #
    #
    #
    #
    # def parse_details(self, response):
    #     item = response.meta.get('item', None)
    #     if item:
    #         # populate more `item` fields
    #         return item
    #     else:
    #         self.log('No item received for %s' % response.url,
    #             level=log.WARNING)
    #
    #
