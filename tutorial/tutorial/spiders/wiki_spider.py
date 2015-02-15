from tutorial.items import WikiItem

__author__ = 'Xiaomin'
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider


class WikiSpider(BaseSpider):
    name = "wiki"

    start_urls = ["file:///Users/Xiaomin/test.html",
                  "file:///Users/Xiaomin/test1.html",
                  "file:///Users/Xiaomin/test2.html"]

    def parse(self, response):
        self.log("Fetch group home page: %s" % response.url)
        wiki = WikiItem()
        wiki['name'] = response.xpath("/html/body/p[1]/text()").extract()[0]
        wiki['value'] = response.xpath("/html/body/p[3]/a/@href").extract()[0]
        print("wiki", wiki['name'] )
        return wiki



#response.xpath('//*[contains(text(),"can")]')
#response.xpath('//*[contains(@class,"extDirectoryName")]')
