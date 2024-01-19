# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy.settings import Settings
from scrapy.exceptions import DropItem
from itemadapter import ItemAdapter
import logging
logging.basicConfig(
    filename='log.log',level=logging.DEBUG
)

class MongoDBPipeline(object):
    @classmethod
    def from_crawler(cls,crawler):
        cls.connection_string=crawler.settings.get('MONGODB_SERVER')
        cls.database=crawler.settings.get('MONGODB_DB')
        cls.collection=crawler.settings.get('MONGODB_COLLECTION')
        return cls()
    
    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.connection_string)
        self.db=self.client[self.database]
        

    def process_item(self,item,spider):
        valid=True
        for data in item:
            if not data:
                valid=False
                raise DropItem("Missing{0}".format(data))
        if valid:
            self.db[self.collection].update_one(ItemAdapter(item).asdict(),{'$set':dict(item)},True)
            # logging.info("question add to MongoDB database!",spider)
        return item
    
    def close_spider(self,spider):
        self.client.close()

