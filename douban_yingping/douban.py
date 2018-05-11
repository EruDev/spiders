# coding: utf-8
from multiprocessing import Pool
import requests
from lxml import html
from random import choice
import json
from pymongo import MongoClient
from user_agents import agents
from proxies import IPPOOL

"""
多进程简单抓取豆瓣
后来的我们
影评数据
"""

client = MongoClient('localhost')
db = client.douban
yingping = db.yingping

User_Agent = choice(agents)
proxy = choice(IPPOOL)
# print(proxy)
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Host': 'movie.douban.com',
    'User-Agent': User_Agent,
    'Referer': 'https://movie.douban.com/subject/26683723',
    'Cookie': 'll="108288"; bid=diEfXIIUyAA; ap=1; __utmz=30149280.1525965783.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=D891A46DFC44DA007AD601A091A2C3601|ded22183bd02e923cecb3464a7f94b7e; ps=y; push_noty_num=0; push_doumail_num=0; __utmc=30149280; __utmc=223695111; __utmz=223695111.1525992889.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1525998136%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E8%25B1%2586%25E7%2593%25A3%26rsv_spt%3D1%26rsv_iqid%3D0xc44f251500023ec6%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D7%26rsv_sug1%3D5%26rsv_sug7%3D100%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.520925212.1525961877.1525992889.1525998136.4; __utma=223695111.1679184162.1525961877.1525992889.1525998136.4; __utmb=223695111.0.10.1525998136; __utmt=1; __utmb=30149280.1.10.1525998136; dbcl2="158213626:p63T5m/PjP4"; ck=z8jm; _pk_id.100001.4cf6=8ada7580c409b768.1525961878.4.1525998202.1525994617.',
}


def get_html(url):
    response = requests.get(url, headers=headers, proxies=proxy)
    try:
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.content
        return False
    except requests.RequestException as e:
        print(e)
        return False


def parse_comment(response):
    comments_list = list()
    el = html.fromstring(response)
    for comment in el.xpath('//div[@class="main review-item"]'):
        user = comment.xpath('header/a[2]/text()')[0]
        score = comment.xpath('header/span[1]/@title')[0]
        time = comment.xpath('header/span[2]/text()')[0].strip()
        title = comment.xpath('div/h2/a/text()')[0]
        short_content = comment.xpath('div/div/div/text()')[0].strip().replace('(', '').replace('&nbsp;', '')
        up = comment.xpath('div/div[3]/a/span/text()')[0].strip() + '赞'
        down = comment.xpath('div/div[3]/a[2]/span/text()')[0].strip() + '踩'
        reply = comment.xpath('div/div[3]/a[3]/text()')[0].strip()
        # print(user, score, time, title, short_content, up, down, reply)
        comments_dict = {
            'user': user,
            'score': score,
            'time': time,
            'title': title,
            'short_content': short_content,
            'up': up,
            'down': down,
            'reply': reply,
        }
        comments_list.append(comments_dict)

    return comments_list


def write_to_file(data):
    try:
        with open('comments.txt', 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')
        print('write txt successfully!')
    except:
        print('some errors!')


def save_to_mongo(data):
    try:
        if yingping.insert(data):
            print('save to mongo successfully!')
    except:
        print('save error!')
    finally:
        print(data)


def main(i):
    url = 'https://movie.douban.com/subject/26683723/reviews?start={}'.format(str(i))
    response = get_html(url)
    data = parse_comment(response)
    f = write_to_file(data)
    database = save_to_mongo(data)
    print(f, database)


if __name__ == '__main__':
    p = Pool(4)
    p.map(main, [i*20 for i in range(1, 214)])
    p.close()
    p.join()
    print('all done!')