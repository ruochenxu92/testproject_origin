# __author__ = 'Xiaomin'
#
# from tutorial.items import WikiItem, ArticleItem, MovieItem
#
# __author__ = 'Xiaomin'
# from scrapy.selector import HtmlXPathSelector
# from scrapy.spider import BaseSpider
# import scrapy
#
# class MovieSpider(BaseSpider):
#     name = "movie"
#     start_urls = ["http://www.imdb.com/chart/top?ref_=nv_ch_250_4"]
#
#     def parse(self, response):
#         hostname = 'http://www.imdb.com'
#         self.log("Fetch group home page: %s" % response.url)
#
#         for sel in response.xpath('//*[@id="main"]/div/div[2]/table/tbody/tr/td[2]'):
#             item = MovieItem()
#             item['Title'] = sel.xpath('a/text()').extract()[0]
#             item['Rating'] = sel.xpath('span[1]/@data-value').extract()[0]
#             item['Ranking'] = sel.xpath('span[1]/text()').re('\d+')[0]
#             item['ReleaseDate'] = sel.xpath('span[2]/@data-value').extract()[0]
#             item['MainPageUrl'] = hostname + sel.xpath('a/@href').extract()[0]
#             url = item['MainPageUrl']
#
#
#             request = scrapy.Request(url, callback=self.getBasicInfo)
#             request.meta['item'] = item
#             yield  request
#
#     def getBasicInfo(self, response):
#         item = response.meta['item']
#         item['Director'] = response.xpath('//*[@id="overview-top"]/div[4]/a/span/text()').extract()
#         item['Writers']  = response.xpath('//*[@id="overview-top"]/div[5]/a/span/text()').extract()
#         item['Sinopsis'] = response.xpath('//*[@id="titleStoryLine"]/div[1]/p/text()').extract()[0]
#         item['Genres'] = response.xpath('//*[@id="titleStoryLine"]/div[4]/a/text()').extract()
#         item['MapRating'] = response.xpath('//*[@id="titleStoryLine"]/div[5]/span[1]/text()').extract()[0]
#         return item
#
#
#     def ifNotEmptyGetIndex(self, item, index = 0):
# 		if item: #check to see it's not empty
# 			return item[index]
# 		else:
# 			return item