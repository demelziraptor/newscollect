from scrapy.contrib.spiders import XMLFeedSpider
from newscollect.items import NewscollectItem

class GuardianSpider(XMLFeedSpider):
    name = 'guardian'
    allowed_domains = ['www.theguardian.com']
    start_urls = ['http://www.theguardian.com/world/rss']
    itertag = 'item'
    
    def parse_node(self, response, node):
        node.remove_namespaces()
        item = NewscollectItem()
        item['title'] = node.xpath('//item/title/text()').extract()[0]
        item['date'] = node.xpath('//item/date/text()').extract()[0]
        yield item