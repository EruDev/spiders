# coding: utf-8
import requests
from lxml import html

url = 'http://image.baidu.com/search/index?tn=baiduimage&word=%E6%96%B0%E5%9E%A3%E7%BB%93%E8%A1%A3'
response = requests.get(url)
response.encoding = 'utf-8'
baidu_html = response.text
# print(response.text)

e = html.fromstring(baidu_html)

for item in e.xpath('//li[@class="imgitem"]'):
    # img_url = item.xpath('div/a/img/@data-imgurl')
    # print(img_url)
    img_url = item.xpath('//*[@id="imgid"]/div/ul/li[1]/div[1]/a/img')
    print(img_url)