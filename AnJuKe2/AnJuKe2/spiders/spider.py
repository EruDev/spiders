
if __name__ == '__main__':

    import requests
    import re
    from pprint import pprint

    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
    }

    url = 'https://m.anjuke.com/ajax/zufang/homerecommend/?page=80000&city_id=14'
    r = requests.get(url, headers=headers).text
    # print(r)
    infos = re.findall(r'"tw_home_recommend_prop":(.*?),"request_time"', r)
    # a = dict()
    # for each in infos:
    #     print(each['title'])
    # print(infos[0], type(infos))
    # for i in infos[0]:
    #     print(i['id'])
    for i in infos[0]:
        print(i)