# coding: utf-8
import requests
from lxml import html

# 简单爬取猫眼电影top100, 并存入到本地

page = 1
index = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

def get_info(offset):
    global index
    global page

    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    response = requests.get(url, headers=headers).text
    e = html.fromstring(response)

    for item in e.xpath('//dl[@class="board-wrapper"]/dd'):
        # 电影名
        movie_name = item.xpath('div/div/div[1]/p[1]/a/text()')[0]
        # 演员
        actor = item.xpath('div/div/div[1]/p[2]/text()')[0].strip()
        # 上映时间
        time = item.xpath('div/div/div[1]/p[3]/text()')[0]
        # 评分
        data = item.xpath('div/div/div[2]/p')
        score = data[0].xpath('string(.)').strip()


        with open('maoyan.txt', 'a+', encoding='utf-8') as f:
            f.write('Top{index}\n电影名: {name}\n{time}\n{actor} 评分: {score}\n'
              .format(index=index, name=movie_name, time=time, actor=actor, score=score))
            f.write('\n')

        index += 1
    print('正在爬取第%s页' % page)
    page += 1


if __name__ == '__main__':
    for i in range(10):
        get_info(i*10)


