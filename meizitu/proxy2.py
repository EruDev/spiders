# coding: utf-8
import requests
from lxml import html

ip_list = list()
ip_dict = dict()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
url = 'http://www.xicidaili.com/nn/'
response = requests.get(url, headers=headers).text
# print(response.text)

el = html.fromstring(response)
ips = el.xpath('//td[@class="country"]/following-sibling::*[1]/text()')
for item in ips:
    ip = item.replace('\n', '').strip()
    if '.' in ip:
        ip_dict['HTTP'] = ip
        # ip_list.append(ip_dict)
        print(ip_dict)
