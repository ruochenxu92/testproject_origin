__author__ = 'Xiaomin'

from scrapy.spider import Spider
from scrapy.utils.response import open_in_browser
import scrapy
import datetime
import os
from tutorial.items import ReviewItem
import lxml.html



def getUrls():
    path = os.path.abspath('/Users/Xiaomin/testproject/tutorial/url.txt')
    f = open(path, 'r')
    listOfUrls = f.read().split('\n')
    return listOfUrls

class IMDBReviewSpider(Spider):
    hostname = 'http://www.imdb.com/'
    name = 'review'
    #allowed_domains = ['http://cs.illinois.edu']
    start_urls = getUrls()

    def __init__(self):
        self.count = 0

    def parse(self, response):
        try:
            reviews = ''
            reviews = response.xpath('//*[@id="titleUserReviewsTeaser"]/div/span/div[2]/p/text()').extract()[0]
            title = response.xpath('//title/text()').extract()[0]
            print(title)
            item = ReviewItem()
            item['url'] = response.url
            # t = lxml.html.parse(item['url'])
            # print(type(t))
            print(type(title))
            title = title.encode("utf8")
            item['title'] = title
            item['review'] = reviews
            item['filename'] = 'xxu46_'+ str(self.count) + '.txt'
            seeMore = response.xpath('//*[@id="quotes"]/a[last()]/@href').extract()[0]
            prefix = item['url'].split('trivia')[0]
            seeMore =prefix + seeMore
            request = scrapy.Request(seeMore, callback=self.parseMovieDetails)
            request.meta['item'] = item
            yield request
        except:
            pass
        self.count += 1


    def parseMovieDetails(self,response):
        item = response.meta['item']
        buffer = ''
        for content in response.xpath('//*[@id="quotes_content"]/div[2]/div/div[1]/p/text()'):
            buffer += content.xpath('text()').extract()[0] + '\n'
        item['quotes'] = buffer
        return item



