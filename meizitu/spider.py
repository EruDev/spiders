# coding: utf-8
import os
import time
import requests
from random import choice
from lxml import html
from requests.exceptions import RequestException

from proxy import ip_list
from agents import agents


class MeiZiTu(object):

    def __init__(self):
        self.headers = {
            'User - Agent': choice(agents),
            'Referer': 'http://www.mzitu.com/', }

    def get_html(self, url):
        """获取网页源代码"""
        try:
            response = requests.get(url, headers=self.headers, proxies=choice(ip_list))
            if response.status_code == 200:
                return response.text
            return None
        except RequestException as e:
            print(e)
            return None

    def all_url(self, response):

        el = html.fromstring(response)
        for item in el.xpath('//ul[@class="archives"]'):
            urls = item.xpath('li/p[contains(@class, "url")]/a/@href')

            for url in urls:
                self.img(url)
                time.sleep(0.01)

    def img(self, url):

        response = self.get_html(url)
        el = html.fromstring(response)
        title = el.xpath('//div[@class="main-image"]/p/a/img/@alt')[0]
        img_src = el.xpath('//div[@class="main-image"]/p/a/img/@src')[0]  # 图片链接
        next_url = el.xpath('//div[@class="pagenavi"]/a[last()]/@href')[0]  # 下一页图片URL
        img_name = el.xpath('//div[@class="main-image"]/p/a/img/@src')[0][-9:]   # 图片名
        flag = el.xpath('//div[@class="pagenavi"]/a[last()]/span/text()')[0].replace('»', '')  # 下一页

        self.makedir(title)

        img_path = '%s/%s%s' % ('C:\MeiZiTu\\' + title, img_name, '.jpg')

        self.down_img(img_path, img_src)

        # print(title)
        # print(img_src)
        # print(next_url)
        # print(flag)
        # print(img_path)

        if flag == '下一页':
            self.img(next_url)

    def makedir(self, title):

        isExists = os.path.exists(os.path.join('C:\MeiZiTu', title))
        if not isExists:
            print('新建一个名为:', title, '的文件夹！')
            os.mkdir(os.path.join('C:\MeiZiTu', title))
            os.chdir(os.path.join('C:\MeiZiTu', title))
            return True
        else:
            return False

    def down_img(self, path, img_src):
        with open(path, 'wb+') as f:
            f.write(requests.get(img_src, headers=self.headers).content)
            print('正在下载图片, 链接为: ', img_src)
        print('该图下载完成')

    def main(self):
        url = 'http://www.mzitu.com/all/'
        response = self.get_html(url)
        self.all_url(response)


if __name__ == '__main__':
    MeiZiTu().main()