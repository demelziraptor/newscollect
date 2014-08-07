from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from newscollect.spiders.cnn_spider import CNNSpider
from newscollect.spiders.guardian_spider import GuardianSpider
from scrapy.utils.project import get_project_settings

spiders = [GuardianSpider(), CNNSpider()]
spiders_running = len(spiders)

def spider_stopped():
    global spiders_running
    spiders_running -= 1
    if spiders_running == 0:
        reactor.stop()

def setup_crawler(spider):
    print "Starting crawl for", spider.name
    settings = get_project_settings()
    crawler = Crawler(settings)
    crawler.signals.connect(spider_stopped, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()

for spider in spiders:
    setup_crawler(spider)
log.start(loglevel=log.DEBUG)
reactor.run()