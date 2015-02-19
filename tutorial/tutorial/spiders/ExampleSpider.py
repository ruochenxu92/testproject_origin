# __author__ = 'Xiaomin'
#
# from scrapy.spider import BaseSpider
# from tutorial.items import ArticleItem, AuthorItem
# from scrapy.utils.response import open_in_browser
# import scrapy
# import datetime
#
#
#
# class ExampleSpider(BaseSpider):
#     #hostname = 'https://scholar.google.com/'
#     name = 'example'
#     #allowed_domains = ['http://cs.illinois.edu']
#     start_urls = ['file://localhost/Users/Xiaomin/0.html']
#
#     def parse(self, response):
#         text = response.xpath('//*[@id="gsc_prf_i"]/div[4]/a[1]/text()').extract()[0]
#         print(text)
#
#
#
#
#
#
#         #return scrapy.Request(url, callback=self.parseHomePage)
#
#          #   //*[@id="extDirectoryPerson1"]/div[3]
#
#     # def parseHomePage(self,response):
#     #     url = response.xpath('//*[@id="gsc_a_ta"]/a/text()').extract()[0]
#     #     return ArticleItem(title=url, body=url, likes =1, pub_date='2001-1-1')
#
#
#   #open_in_browser(response)
#
#         #for sel in response.xpath('//*[@id="block-block-11"]/div/div/div/div[2]'):
#          #test = response.xpath('//*[@class="chart"]/tbody/tr/td[2]/a/text()').extract()[0]
#          #test = response.xpath('//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[3]/strong/text()').extract()[0]
#         # test = response.xpath('//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/span[2]/@data-value').extract()[0]
#         #  test = response.xpath('//*[@id="gsc_table"]/div[1]/div[2]/text()').extract()[0]
#         #  t_pub_date = response.xpath('//*[@id="gsc_table"]/div[2]/div[2]/text()').extract()[0]
#         #  t_body = response.xpath('//*[@id="gsc_descr"]/text()').extract()[0]
#         #email = response.xpath("//*[contains(text(),'.edu')]").extract()[0]
#
#
#
#
#
#
#
#
#
