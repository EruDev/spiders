# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class HuxiuwangItem(scrapy.Item):
    title = Field()
    author = Field()
    time = Field()
    desc = Field()
    link = Field()



class ArticleItem(scrapy.Item):
    article_title = Field()
    article_author = Field()
    article_content = Field()


