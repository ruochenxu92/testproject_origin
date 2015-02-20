__author__ = 'Xiaomin'

from scrapy.spider import Spider
from scrapy.utils.response import open_in_browser
import scrapy
import datetime
import os
from tutorial.items import WikiItem
import lxml.html

def getUrls():
    path = os.path.abspath('/Users/Xiaomin/testproject/tutorial/xxu46_0.txt')
    f = open(path, 'r')
    listOfUrls = f.read().split('\n')
    return listOfUrls

class IMDBReviewSpider(Spider):
    name = 'family'
    #allowed_domains = ['http://cs.illinois.edu']
    start_urls = getUrls()

    def __init__(self):
        self.count = 0
        self.hostname = getUrls()

    def parse(self, response):
        oneWiki = WikiItem()
        for sel in response.xpath('//*[@id="threadslist"]/tbody/tr/td[3]/div[1]/a'):
            item = WikiItem()
            item['name'] = sel.xpath('@href').extract()[0]

            print item['name']
            yield item
            #oneWiki['name'].append(item)

        #return oneWiki


    #         sel.
    #
    #
    #     #
    #     # request = scrapy.Request(seeMore, callback=self.parseMovieDetails)
    #     # request.meta['item'] = item
    #     # yield request
    #
    #
    # def parse(self, response):
		# # for sel in response.xpath('//*[@id="threadslist"]/tbody/tr/td[3]/div[1]/a'):
		# 	item = WikiItem()
    #         item['name'] = sel.xpath('@href').extract()[0]
		# 	yield item



    #
    #
	# def parseMovieDetails(self, response):
	# 	item = response.meta['item']
	# 	item = self.getBasicFilmInfo(item, response)
	# 	item = self.getTechnicalDetials(item, response)
	# 	item = self.getCastMemberInfo(item, response)
	# 	return item

    #
    # def parseMovieDetails(self,response):
    #     item = response.meta['item']
    #     buffer = ''
    #     for url in response.xpath('//*[@id="threadslist"]/tbody/tr/td[3]/div[1]/a'):
    #
    #
    #
    #
    #
    #
    #     item['quotes'] = buffer
    #     return item



