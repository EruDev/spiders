# coding: utf-8

import time
import requests
from random import choice, randint
from multiprocessing import Pool
from lxml import html
from requests.exceptions import RequestException

import agents
import proxies
from pipeline import *


BASE_URL = 'http://search.dangdang.com/?key=' # 起始URL
KW = 'Python'  # 关键字

def get_html(url):
    """获取网页源代码"""
    agent = choice(agents.agents) # 随机取一个user_agent
    headers = {
        'User-Agent': agent,
    }
    try:
        response = requests.get(url, headers=headers, proxies=choice(proxies.proxy_list)) # 随机取一个ip..其实很简陋..网上拿的免费的ip
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引出错!')
        return None


def parse_one_page(response):
    """解析单页"""
    el = html.fromstring(response)
    next = el.xpath('//div[@class="paging"]/ul/li[last() - 1]/a/text()')[0] # 下一页
    href = el.xpath('//div[@class="paging"]/ul/li[last() - 1]/a/@href')[0].replace('/', '').partition('&')
    next_page = href[1] + href[2] # 下一页URL
    # print(next_page)

    for item in el.xpath('//ul[@class="bigimg"]/li'):
        try:
            title = item.xpath('a/@title')[0].strip() # 书名
            price = item.xpath('p[3]/span/text()')[0] # 价格
            data = item.xpath('p[5]/span[1]')
            author = list(map(lambda x: x.xpath('string(.)'), data))[0] # 作者
            timer = item.xpath('p[5]/span[2]/text()')[0].replace('/', '') # 出版日期
            press = item.xpath('p[5]/span[3]/a/text()')[0] # 出版社
            # print(title, price, author, time, press, timer)
            MyDB().save_to_mysql(title, price, author, timer, press)
        except:
            title = '暂无图书信息！'
            price = '暂无价格!'
            press = '暂无出版社信息!'
            author = '暂无作者信息!'
            timer = '暂无出版时间!'
            # print(title, price, author, timer, press)
            MyDB().save_to_mysql(title, price, author, timer, press)
    # 翻页
    if next == '下一页':
        url = BASE_URL + KW + next_page
        print(url)
        time.sleep(randint(1, 5))
        response = get_html(url)
        parse_one_page(response)


def main():
    # 创建表
    MyDB().create_table()
    url = BASE_URL + KW
    # print(url)
    response = get_html(url)
    parse_one_page(response)


if __name__ == '__main__':
    # 开启多进程模式
    pool = Pool(4)
    for i in range(1, 5):
        p = pool.apply_async(main)
    pool.close()
    pool.join()