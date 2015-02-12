__author__ = 'Xiaomin'
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider


class WikiSpider(BaseSpider):
    name = "wiki"
    allowed_domains = ["www.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Python_(programming_language)"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        test = hxs.select("//[contains(text(),'python')]").extract()
        yield (test)



#response.xpath('//*[contains(text(),"can")]')
#response.xpath('//*[contains(@class,"extDirectoryName")]')
