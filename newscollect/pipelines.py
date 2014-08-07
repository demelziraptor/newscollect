# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from datetime import datetime
from scrapy.exceptions import DropItem


class DatelessPipeline(object):
    def process_item(self, item, spider):
        if 'date' not in item:
            raise DropItem("Item has no date; dropping!")
        else:
            return item
        
class ParseDatePipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'guardian':
            item['date'] = datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%SZ')
        if spider.name == 'cnn':
            item['date'] = datetime.strptime(item['date'], 'updated %H:%M %Z %d.%m.%y')
        return item

class NewscollectPipeline(object):
    def process_item(self, item, spider):
        return """The {name} website wrote this headline: "{title}" at this time: {date}""".format(
                    name=spider.name, title= item['title'], date=item['date'].strftime('%H:%M on %d/%m/%Y'))
