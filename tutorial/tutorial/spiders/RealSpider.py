__author__ = 'Xiaomin'

from scrapy.spider import BaseSpider
from tutorial.items import ArticleItem, AuthorItem,InterestItem, PaperItem
from scrapy.utils.response import open_in_browser
import scrapy
import datetime
import os
from scrapy import log

'''
get list of professors
'''
def getListOfProfessors():
    listOfProfessors = []
    path = os.path.abspath("/Users/Xiaomin/testproject/tutorial/professor.txt")
    f = open(path)
    listOfProfessors = f.read().split('\n')
    return listOfProfessors

'''
get list of urls
'''
def getStartUrls():
    prefix = 'https://scholar.google.com/scholar?q='
    suffix = '&btnG=&hl=en&as_sdt=0%2C14'
    start_urls = []
    listOfProfessors = getListOfProfessors()
    for prof in listOfProfessors:
        start_urls.append(prefix + prof + suffix)
    return start_urls

start_urls = getStartUrls()




'''
spider for crawling authors information
'''
class RealSpider(BaseSpider):
    hostname = 'https://scholar.google.com/'
    name = 'real'
    allowed_domains = [hostname]
    start_urls = getStartUrls()

    def parse(self, response):
        url = response.xpath("//a[contains(@href, 'user')]/@href").extract()[0]

        try:
            url = self.hostname + url
            # print url
            item = {}
            # request = scrapy.Request(url, callback=self.parse_page2)
            # request.meta['item'] = item
            # return request
            item['url'] = url
            print("success",url)
            yield item
        except:
            print("url exception",url)





    # def parse_page2(self,response):
    #     #url = response.xpath('//*[@id="gsc_a_ta"]/a/text()').extract()[0]
    #     #author['institution'] = response.xpath('//*[@id="gsc_prf_i"]/div[3]/text()').extract()[0]
    #     items = response.meta['item']
    #     for sel in response.xpath('//*[@id="gsc_prf_i"]/div[4]/a'):
    #         interest_area = sel.xpath('/text()').extract()[0]
    #         items.append(interest_area)
    #         print "interest:",interest_area
    #     return items
    #return ArticleItem(title=url, body=url, likes =1, pub_date='2001-1-1')

    def parse_details(self, response):
        item = response.meta.get('item', None)
        if item:
            # populate more `item` fields
            return item
        else:
            self.log('No item received for %s' % response.url,
                level=log.WARNING)


