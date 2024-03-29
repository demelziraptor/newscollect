# -*- coding: utf-8 -*-

# Scrapy settings for newscollect project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'newscollect'

SPIDER_MODULES = ['newscollect.spiders']
NEWSPIDER_MODULE = 'newscollect.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newscollect (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'newscollect.pipelines.DatelessPipeline': 300,
    'newscollect.pipelines.ParseDatePipeline': 400,
    'newscollect.pipelines.NewscollectPipeline': 1000
}