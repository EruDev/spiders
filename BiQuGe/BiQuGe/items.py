# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 小说名
    name = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 编号
    name_id = scrapy.Field()
    # 链接
    link = scrapy.Field()
    # 最后更新
    last_update = scrapy.Field()
    # 章节地址
    chapter_url = scrapy.Field()


class ChapterItem(scrapy.Item):
    # 小说编号
    id_name = scrapy.Field()
    # 用来绑定章节顺序
    num = scrapy.Field()
    # 章节内容
    chaptercontent = scrapy.Field()
    # 章节地址
    chapterurl = scrapy.Field()
    # 章节名字
    chaptername = scrapy.Field()
