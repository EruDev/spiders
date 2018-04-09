# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymongo
# from scrapy.conf import settings
# from scrapy import log
# from scrapy.exceptions import DropItem
#
# """
# 本来是打算存入到mongodb中的
# """
#
# class BiqugePipeline(object):
#
#     def open(self, spider):
#         self.conn = pymongo.MongoClient(
#             settings['MONGODB_SERVER'],
#             settings['MONGODB_PORT']
#         )
#         self.db = self.conn[settings['MONGODB_DB']]
#         self.collection = self.db[settings['MONGODB_COLLECTION']]
#
#         log.msg('Load name_id from MongoDB database!',
#                 level=log.DEBUG, spider=spider)
#
#         self.itemlist = set()
#         for i in self.collection.find():
#             self.itemlist.add(i['name_id'])
#
#     def close(self, spider):
#         self.conn.close()
#
#     def process_item(self, item, spider):
#         if item['name_id'] in self.itemlist:
#             raise DropItem('Duplication data!')
#         self.collection.insert(dict(item))
#         log.msg('novel record added to MongoDB database.',
#                 level=log.DEBUG, spider=spider)
#         return item
