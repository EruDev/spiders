# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
from AnJuKe2.items import AnjukeZuFangItem, AnjukeErShouFangItem


class AnJuKeMongoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient("localhost", 27017)
        db = client["AnJuKe"]
        self.zufang = db["AnJuKe"]
        self.ershoufang = db['AnJuKe']
        print('开启数据库')

    def process_item(self, item, spider):
        print('MongoDBItem', item)
        """ 判断类型 存入MongoDB """
        if isinstance(item, AnjukeZuFangItem):
            print('AnjukeZuFangItem True')
            try:
                self.zufang.update_one({'zf_url': item['zf_url']}, {'$set': dict(item)}, upsert=True)
            except Exception:
                pass

        if isinstance(item, AnjukeErShouFangItem):
            print('AnjukeErShouFangItem True')
            try:
                self.ershoufang.update_one({'esf_link': item['esf_link']}, {'$set': dict(item)}, upsert=True)
            except Exception:
                pass
        return item