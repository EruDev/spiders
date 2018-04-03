# coding:utf-8
import requests
import re
import os

# 百度图片
"""
xpath 试了一把, 并不能解析到, 然后发现图片链接在源代码中
"""
index = 1 # 文件夹名

def get_one_page(url):
    """获取单页的网页源码"""
    try:
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            }
        response = requests.get(url, headers=headers)
        response.encoding='utf-8'
    except:
        print('error')
    return response.text


def parse_one_page(response):
    """解析单页"""
    pattern = re.compile(r'objURL":"(.*?)"')
    urls = pattern.findall(response, re.S)
    return urls


def save_to_file(urls):
    """储存到本地"""
    global index
    # 判断是否存在该文件夹
    if not os.path.exists(str(index)):
        os.mkdir(str(index))

    for url in urls:
        # 获取图片名称
        img_title = url.split('/')[-1]
        # 存储路径
        img_path = '%s//%s//%s' % (os.path.abspath('.'), index, img_title)
        # print(img_path)
        try:
            with open(img_path, 'wb+') as f:
                f.write(requests.get(url).content)
            print('正在下载图片, 链接为: %s' % url)
        except:
            print('Invalid img title.')
            continue

    index += 1


def main(page):
    # 遍历爬取
    print('='*30)
    print('百度图片下载器')
    word = input('请输入关键字, 只支持单关键字:>')
    print('='*30)
    for i in range(page):
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={word}pn={page}'.format(word=word, page=page*20)
        response = get_one_page(url)
        urls = parse_one_page(response)
        save_to_file(urls)


if __name__ == '__main__':
    main(10)