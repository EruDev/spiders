# coding: utf-8
import json
from multiprocessing import Pool
import requests
from pymongo import MongoClient

client = MongoClient('localhost')
db = client['xmla']
collection = db.xmla

"""
fiddler 抓取
喜马拉雅精品榜数据
"""

headers = {
    'Cookie': '1&_device=android&00000000-7d51-9bab-ffff-ffffceffdffe&6.3.93;channel=and-d8;impl=com.ximalaya.ting.android;osversion=25;XUM=TBia6F7p;XIM=31364e7b98add;c-oper=%E4%B8%AD%E5%9B%BD%E8%81%94%E9%80%9A;net-mode=WIFI;res=1080%2C1920;NSUP=42e8bc82%2C422068c8%2C1526003876290;AID=EyYxlPf2eng=;manufacturer=OPPO;xm_grade=0;domain=.ximalaya.com;path=/;x-abtest-bucketIds=100261,100230;x_xmly_resource=xm_source%3Asquare%26xm_medium%3ApaidCategory%26xm_item%3Arank_all_category_paid;x_xmly_tid=8604149828287320115;x_xmly_ts=1526004188528;',
    'Cookie2': '$version=1',
    'user-agent': 'ting_6.3.93(OPPO+R11,Android25)',
    'Host': 'mobwsa.ximalaya.com',
    'Accept-Encoding': 'gzip',
    'Content-Type': 'application/json;charset=utf-8',
    'Connection': 'keep-alive',
}

def main(i):
    url = 'http://mobwsa.ximalaya.com/mobile/discovery/v1/rank/album?device=android&pageId={}&pageSize=20&rankingListId=62'.format(str(i))
    response = requests.get(url, headers=headers).json()['list']
    # print(response)
    for item in response:
        title = item['title']
        nickname = item['nickname']
        tracks = str(item['tracks']) + '集'
        playsCounts = item['playsCounts']
        score = item['score']

        info = {
            'title': title,
            'nickname': nickname,
            'tracks': tracks,
            'playCounts': playsCounts,
            'score': score,
        }
        collection.insert(info)
        print(title, nickname, tracks, playsCounts, score)

if __name__ == '__main__':
    p = Pool(4)
    p.map(main, [i for i in range(1, 6)]) # 只有五页。。
    p.close()
    p.join()
    print('all done!')