# -*- coding: utf-8 -*-
import scrapy
from BiQuGe.items import BiqugeItem, ChapterItem
from scrapy.http import Request # 一个单独的request模块, 需要跟进URL的时候, 会用到
import re
from BiQuGe.mysqlpipelines.sql import Sql


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['www.biquge5200.com']
    start_urls = ['https://www.biquge5200.com/xiaoshuodaquan/']

    def parse(self, response):
        # print(response.text)
        urls = response.xpath('//div[@class="novellist"]/ul/li')
        # 遍历小说主页所有的URL
        for el in urls:
            url = 'https:' + el.xpath('a/@href').extract()[0]
            yield Request(url, callback=self.parse_novel, meta={'link': url}) # meta可以用来传参

    def parse_novel(self, response):
        """解析单个小说"""
        item = BiqugeItem()
        item['name'] = response.xpath('//div[@id="info"]/h1/text()').extract()[0] # 小说名
        author = response.xpath('//div[@id="info"]/p[1]/text()').extract()[0]
        item['author'] = str(author).replace('作\xa0\xa0\xa0\xa0者：', '') # 小说作者
        name_id = response.meta['link'].split('/')[-2]
        item['name_id'] = str(name_id) # 小说编号
        last_update = response.xpath('//div[@id="info"]/p[3]/text()').extract()[0]
        item['last_update'] = str(last_update).replace('最后更新：', '') # 小说最后更新日期

        # 这里匹配出来的是 章节和章节名
        urls = re.findall(r'<dd><a href="(.*?)">(.*?)</a></dd>', response.text)
        num = 0
        for url in urls:
            num = num + 1
            chapter_url = url[0]
            chapter_name = url[1]
            rets = Sql.select_name(chapter_url)
            if rets[0] == 1:
                print('章节已经存在了')
            else:
                yield Request(chapter_url, callback=self.parse_chapter_content, meta={'num': num,
                                                                                      'id_name': item['name_id'],
                                                                                      'chaptername': chapter_name,
                                                                                      'chapterurl': chapter_url,
                                                                                  }) # meta参数可以用来传参, 具体的用法可以参考官方文档
        yield item

    def parse_chapter_content(self, response):
        item = ChapterItem()
        # item['id_name'] = response.meta['id_name'] # 小说编号
        item['num'] = response.meta['num'] # 用来指定章节顺序
        chaptercontent = response.xpath('//div[@id="content"]/text()').extract()[0]
        item['chaptercontent'] = str(chaptercontent).replace('\xa0', '').replace('\u3000＊', '')  # 小说内容
        item['chapterurl'] = response.meta['chapterurl'] # 小说URL
        item['chaptername'] = response.meta['chaptername'] # 小说章节名
        yield item














