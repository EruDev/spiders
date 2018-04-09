# -*- coding: utf-8 -*-
import scrapy
import json
from lxml import html
from huxiuwang.items import HuxiuwangItem, ArticleItem


class HuxiuSpider(scrapy.Spider):
    name = 'huxiu'

    def start_requests(self):
        url = 'https://www.huxiu.com/v2_action/article_list'
        for i in range(1, 10):
            # FromRequest 是Scrapy发送POST请求的方法
            yield scrapy.FormRequest(
                url=url,
                formdata={'huxiu_hash_code': '6f3d16563e201e5c61f124425d473db9',
                          'page': str(i)},
                callback=self.parse,
            )

    def parse(self, response):
        # print(response.text)
        data = json.loads(response.text)['data']
        # print(data)
        r = html.fromstring(data)
        item = HuxiuwangItem()

        item['title'] = r.xpath('//a[@class="transition msubstr-row2"]/text()')[0]
        item['time'] = r.xpath('//span[@class="time"]/text()')[0]
        item['author'] = r.xpath('//span[@class="author-name"]/text()')[0]
        item['desc'] = r.xpath('//div[@class="mob-sub"]/text()')[0]
        item['link'] = r.xpath('//h2/a/@href')[0]
        link = item['link']

        yield item
        yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        item = ArticleItem()
        item['article_title'] = response.xpath('//h1/text()').extract()[0].strip()
        item['article_author'] = response.xpath('//span[@class="author-name"]/a/text()').extract()[0].strip()
        content = response.xpath('//div[@class="article-content-wrap"]')
        item['article_content'] = content.xpath('string(.)').extract()[0].strip().replace('\n', '').replace('/', '')

        yield item
