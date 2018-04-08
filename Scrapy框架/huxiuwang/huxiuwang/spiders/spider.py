from lxml import html
import requests
from pprint import pprint

def main():

    url = 'https://www.huxiu.com/v2_action/article_list'
    payload = {
        'huxiu_hash_code': '6f3d16563e201e5c61f124425d473db9',
        'page': '2',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }

    response = requests.post(url, headers=headers, data=payload).json()['data']
    pprint(response)


if __name__ == '__main__':
    main()