# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import time
import json
from AnJuKe2.items import AnjukeZuFangItem, AnjukeErShouFangItem
import re
from random import random


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'

    def start_requests(self):
        # 北京租房
        for i in range(1000):
            zf_url = 'https://m.anjuke.com/ajax/zufang/homerecommend/?page={}&city_id=14'.format(str(i))
            yield Request(zf_url, callback=self.parse_zufang)
            time.sleep(random())

        # 北京二手房
        for i in range(234):
            esf_url = 'https://beijing.anjuke.com/v3/ajax/rec/profile/?cityid=14' \
                      '&proids=1143668672%2C1172245917%2C1176510782&resulttype=3&page={}'.format(str(i))

            yield Request(esf_url, callback=self.parse_ershoufang)
            time.sleep(random())

    def parse_ershoufang(self, response):
        item = AnjukeErShouFangItem()
        response = response.text
        infos = re.findall(r'"results":(.*?),"request_time"', response)[0]
        infos = json.loads(infos)
        for info in infos:
            item['esf_proid'] = info['PROID']
            item['esf_cityid'] = info['CITYID']
            item['esf_title'] = info['TITLE']
            item['esf_link'] = info['LINK']
            item['esf_price'] = info['PROPRICE']
            item['esf_roomnum'] = info['ROOMNUM']
            item['esf_hallnum'] = info['HALLNUM']
            item['esf_toiletnum'] = info['TOILETNUM']
            item['esf_area'] = info['AREANUM'] + '平'
            item['esf_commname'] = info['COMMNAME']
            item['esf_areacode'] = info['AREACODE']
            item['esf_imagesrc'] = info['IMAGESRC']
            # print(info)

            yield item

    def parse_zufang(self, response):
        item = AnjukeZuFangItem()
        response = response.text
        infos = re.findall(r'"tw_home_recommend_prop":(.*?),"request_time"', response)[0]
        infos = json.loads(infos)
        # print(infos)
        for info in infos:
            item['zf_id'] = info['id']
            item['zf_title'] = info['title']
            item['zf_url'] = info['url']
            item['zf_room_num']= info['room_num']
            item['zf_hall_num'] = info['hall_num']
            item['zf_fitment_name'] = info['fitment_name']
            item['zf_price'] = info['price']
            item['zf_comm_name'] = info['comm_name']
            item['zf_block_name'] = info['block_name']
            item['zf_area_name'] = info['area_name']
            item['zf_area_num'] = info['area_num']
            item['zf_rent_type'] = info['rent_type']
            item['zf_tags'] = info['tags']

            yield item
