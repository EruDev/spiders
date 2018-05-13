# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HdbeemovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    m_id = scrapy.Field()                   # 电影 id
    current_movie_url = scrapy.Field()      # 电影URL
    # next_url = scrapy.Field()
    next_page_url = scrapy.Field()          # 下一页URL
    current_page_url = scrapy.Field()       # 当前页面URL
    title = scrapy.Field()                  # 电影标题
    director = scrapy.Field()               # 导演
    scriptwriter = scrapy.Field()           # 编辑
    actor = scrapy.Field()                  # 演员
    m_type = scrapy.Field()                 # 电影类型
    localtion = scrapy.Field()              # 上映地区
    languages = scrapy.Field()              # 语言
    times = scrapy.Field()                  # 时长
    m_time = scrapy.Field()                 # 上映时间
    others = scrapy.Field()                 # 其他信息
    score = scrapy.Field()                  # 评分
    img_src = scrapy.Field()                # 电影封面图链接
    introduce = scrapy.Field()              # 简介