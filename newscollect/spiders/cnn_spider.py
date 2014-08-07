from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from newscollect.items import NewscollectItem

class CNNSpider(CrawlSpider):
    name = "cnn"
    allowed_domains = ["edition.cnn.com"]
    start_urls = ["http://edition.cnn.com/WORLD/all.html"]
    user_agent = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 5 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.99 Mobile Safari/537.36'
    
    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//div[@class="module_bgroup"]')), callback='parse_item'),
    )
    
    def parse_item(self, response):
        item = NewscollectItem()
        item['title'] = response.xpath('//li[@class="article"]/span[@class="tline"]/text()').extract()[0]
        item['date'] = response.xpath('//li[@class="article"]/span[@class="artday"]/text()').extract()[0]
        yield item