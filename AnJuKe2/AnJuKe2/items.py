# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class AnjukeZuFangItem(scrapy.Item):
    zf_id = Field()                 # 编号
    zf_title = Field()              # 标题
    zf_url = Field()                # 链接
    zf_room_num = Field()           # 户型(室)
    zf_hall_num = Field()           # 户型(厅)
    zf_fitment_name = Field()       # 装修
    zf_price = Field()              # 价格
    zf_comm_name = Field()          # 所属小区
    zf_block_name = Field()         # 村
    zf_area_name = Field()          # 区
    zf_area_num = Field()           # 面积(平)
    zf_rent_type = Field()          # 出租类型
    zf_tags = Field()               # 标签


class AnjukeErShouFangItem(scrapy.Item):
    esf_proid = Field()             # 编号
    esf_cityid = Field()            # 城市编号 14为北京
    esf_title = Field()             # 标题
    esf_link = Field()              # 链接
    esf_price = Field()             # 价格
    esf_roomnum = Field()           # 户型(室)
    esf_hallnum = Field()           # 户型(厅)
    esf_toiletnum = Field()         # 卫生间
    esf_area = Field()              # 面积
    esf_commname = Field()          # 所属小区
    esf_areacode = Field()          # 小区编号
    esf_imagesrc = Field()          # 图片链接
