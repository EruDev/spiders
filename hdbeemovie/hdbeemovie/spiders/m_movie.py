# # -*- coding: utf-8 -*-
# import re
# from scrapy import Spider, Request
# from ..items import HdbeemovieItem
# from hdbeemovie.MySqlpipelines.Sql import MySql
# import requests
# from hdbeemovie import settings
#
# class HdbeeSpider(Spider):
#     name = 'hdbee'
#     allowed_domains = ['www.hdbee.net']
#     FIRST = True
#     NEXT_URL = MySql.find_next_page_url()
#     CURRENT_URL = MySql.find_current_movie_url()
#     CURRENT_PAGE_URLS = set(MySql.find_last_movie_url())
#
#     r = requests.get(CURRENT_URL, headers=settings.DEFAULT_REQUEST_HEADERS).text
#     all_urls = set(re.findall(r'class="user_list_kz" href="(.*?)" title', r, re.S))
#     surplus_urls = all_urls - CURRENT_PAGE_URLS
#
#
#     BASE_URL = 'http://www.hdbee.net/movie/'
#     KW = ['oumei', 'guochan', 'gangtai', 'rihan', 'yatai']
#
#     try:
#         if NEXT_URL is None and CURRENT_URL is None:
#             print('首次启动爬虫, 等待抓取')
#         else:
#             print('上一次爬取电影的 URL:', CURRENT_URL)
#             print('待抓取下一个电影的URL:', list(surplus_urls)[0])
#     except KeyError:
#         print('\n')
#         print('出了点小问题')
#
#     def start_requests(self):
#         if self.FIRST:
#             self.FIRST = False
#             for word in self.KW:
#                 yield Request(url=self.BASE_URL + word, callback=self.parse)
#         else:
#             if self.surplus_urls:
#                 for url in self.surplus_urls:
#                     yield Request(url=url, callback=self.parse_detail)
#             else:
#                 yield Request(url=self.NEXT_URL, callback=self.parse)
#
#     def parse(self, response):
#         next_page_url = response.xpath('//div[@class="nav-links"]/a[last()]/@href').extract_first(default='null')
#         current_page_url = next_page_url[:-1] + str(int(next_page_url[-1]) - 1)
#
#         for item in response.xpath('//ul[@id="index_ajax_list"]/li'):
#             current_movie_url = item.xpath('a/@href').extract_first()
#             m_id = current_movie_url.split('/')[-1].replace('.html', '')
#             yield Request(url=current_movie_url, callback=self.parse_detail,
#                           meta={'m_id': m_id,
#                                 'current_movie_url': current_movie_url,
#                                 'next_page_url': next_page_url,
#                                 'current_page_url': current_page_url})
#
#         if next_page_url:
#             yield Request(url=next_page_url, callback=self.parse)
#
#     def parse_detail(self, response):
#         m_item = HdbeemovieItem()
#         m_item['m_id'] = response.meta.get('m_id')
#         m_item['current_movie_url'] = response.meta.get('current_movie_url')
#         m_item['next_page_url'] = response.meta.get('next_page_url')
#         m_item['img_src'] = response.xpath('//div[@class="col-xs-4 padding-right-0"]/a/img/@src').extract_first(
#             default="null")
#         m_item['introduce'] = response.xpath('//div[@class="movie-introduce"]/p/text()').extract_first(
#             default="null").strip().replace('\u3000', '')
#         for item in response.xpath('//div[@class="movie-meta"]'):
#             data = item.xpath('h1')
#             m_item['title'] = data.xpath('string(.)').extract_first(default="null")
#             data1 = item.xpath('p[1]')
#             m_item['director'] = data1.xpath('string(.)').extract_first(default="null")
#             data2 = item.xpath('p[2]')
#             m_item['scriptwriter'] = data2.xpath('string(.)').extract_first(default="null")
#             data3 = item.xpath('p[3]')
#             m_item['actor'] = data3.xpath('string(.)').extract_first(default="null")
#             data4 = item.xpath('p[4]')
#             m_item['m_type'] = data4.xpath('string(.)').extract_first(default="null")
#             data5 = item.xpath('p[5]')
#             m_item['localtion'] = data5.xpath('string(.)').extract_first(default="null")
#             data6 = item.xpath('p[6]')
#             m_item['languages'] = data6.xpath('string(.)').extract_first(default="null")
#             data7 = item.xpath('p[7]')
#             m_item['times'] = data7.xpath('string(.)').extract_first(default="null")
#             data8 = item.xpath('p[8]')
#             m_item['m_time'] = data8.xpath('string(.)').extract_first(default="null")
#             data9 = item.xpath('p[9]')
#             m_item['others'] = data9.xpath('string(.)').extract_first(default="null")
#             data10 = item.xpath('p[10]')
#             m_item['score'] = data10.xpath('string(.)').extract_first(default="null")
#
#         yield m_item
#
#
