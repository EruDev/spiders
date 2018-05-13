# # coding: utf-8
#
# if __name__ == '__main__':
#     import re
#     import requests
#
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
#         'Upgrade-Insecure-Requests': '1',
#         'Referer': 'http://www.hdbee.net/movie/',
#         'Host': 'www.hdbee.net',
#     }
#     response = requests.get(url="http://www.hdbee.net/movie/oumei/page/1", headers=headers).text
#     urls = re.findall(r'class="user_list_kz" href="(.*?)"', response, re.S)
#     print(set(urls))

#     import requests
#     from lxml import html
#

#     url = 'http://www.hdbee.net/movie/oumei/page/2'
#     current_url = 'http://www.hdbee.net/53248.html'
#     response = requests.get(url, headers=headers).text
#     # print(response)
#     import re
#     urls = re.findall(r'class="user_list_kz" href="(.*?)" title', response, re.S)
#     print(urls)
#     # for href in urls:
#     #     print(href)
#
#     el = html.fromstring(response)
#     # m_all = el.xpath('//div[@class="nav-links"]/a[last()-1]/text()')[0]
#     # print(m_all, type(m_all))
#     # for i in range(1, int(m_all) + 1):
#     #     url = url + '/page/' + str(i)
#     #     print(url)
#     # for item in el.xpath('//ul[@id="index_ajax_list"]/li'):
#     #     href = item.xpath('a/@href')[0]
#     #     title = item.xpath('div/h2/text()')[0]
#     #     print(href, title)
#     # #     m_id = href.split('/')[-1].replace('.html', '')
#     # #     print(href, m_id)
#     # next = el.xpath('//div[@class="nav-links"]/a[last()]/@href')[0]
#     # print(next)
#     # url = 'http://www.hdbee.net/59.html'
#     # response = requests.get(url, headers=headers).text
#     # el = html.fromstring(response)
#     # m_introduce = el.xpath('//div[@class="movie-introduce"]/p/text()')[0]
#     # print(m_introduce)
#     # for item in el.xpath('//div[@class="movie-meta"]'):
#     #     data = item.xpath('h1')[0]
#     #     title = data.xpath('string(.)')
#     #     data1 = item.xpath('p[1]')[0]
#     #     director = data1.xpath('string(.)')
#     #     data2 = item.xpath('p[2]')[0]
#     #     scriptwriter = data2.xpath('string(.)')
#     #     data3 = item.xpath('p[3]')[0]
#     #     actor = data3.xpath('string(.)')
#     #     data4 = item.xpath('p[4]')[0]
#     #     m_type = data4.xpath('string(.)')
#     #     data5 = item.xpath('p[5]')[0]
#     #     localtion = data5.xpath('string(.)')
#     #     data6 = item.xpath('p[6]')[0]
#     #     language = data6.xpath('string(.)')
#     #     data7 = item.xpath('p[7]')[0]
#     #     time = data7.xpath('string(.)')
#     #     data8 = item.xpath('p[8]')[0]
#     #     m_time = data8.xpath('string(.)')
#     #     data9 = item.xpath('p[9]')[0]
#     #     others = data9.xpath('string(.)')
#     #     data10 = item.xpath('p[10]')[0]
#     #     score = data10.xpath('string(.)')
#     #     print(title, director, scriptwriter, actor, m_type, localtion, language, time, m_time, others, score)

