# coding: utf-8
import os
import requests
from lxml import html

base_url = 'http://tieba.baidu.com/p/'
def get_one_page(page_num):
    url = base_url + page_num
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    try:
        response = requests.get(url, headers=headers).text
        return response
    except:
        print('提取链接失败: %s' % url)


def parse_one_page(response):
    e = html.fromstring(response)
    # 判断是否还有下一页
    flag = e.xpath('//ul[@class="l_posts_num"]/li[@class="l_pager pager_theme_5 pb_list_pager"]/a[last() - 1]/text()')[0]
    page = e.xpath('//ul[@class="l_posts_num"]/li[@class="l_pager pager_theme_5 pb_list_pager"]/a[last() - 1]/@href')[0].partition('?')
    # 相当与url后面的参数, 类似这样: ?pn=2
    page_num = page[1] + page[2]
    num = e.xpath('//ul[@class="l_posts_num"]/li[@class="l_pager pager_theme_5 pb_list_pager"]/a[last() - 1]/@href')[0][-1]
    for item in e.xpath('//div[@class="p_content  p_content p_content_nameplate"]'):
        try:
            # 图片的链接
            img_src = item.xpath('cc/div/img/@src')[0]
            # 图片的标题
            img_url = img_src.split('/')[-1]
        except:
            print('提取图片地址失败:<')

    if flag == '下一页':
        res = get_one_page(str(page_num))
        parse_one_page(res)


def save_to_img(url, num, img_url):
    img_path = '%s/%s/%s' % (os.path.abspath('.'), str(num), img_url)
    if not os.path.exists(str(num - 1)):
        os.mkdir(num)
    with open(img_path, 'wb+') as f:
        f.write(requests.get(url).content)
        print('正在下载图片, 链接为: %s' % url)


def main():
    print('='*20)
    print('贴吧图片下载助手')
    index = input('请输入帖子代号:')
    print('='*20)
    response = get_one_page(str(index))
    parse_one_page(response)


if __name__ == '__main__':
    main()
