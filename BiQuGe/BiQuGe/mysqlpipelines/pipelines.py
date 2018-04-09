from .sql import Sql
from BiQuGe.items import BiqugeItem, ChapterItem



class BiQuGePipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, BiqugeItem):
            name_id = item['name_id']
            last_update = item['last_update']
            ret = Sql.select_name(name_id)
            if ret[0] == 1:
                print('已经存在了')
            else:
                xs_name = item['name']
                xs_author = item['author']
                Sql.insert_bqg_name(xs_name, xs_author, last_update, name_id)
                print('开始存小说标题')

        if isinstance(item,ChapterItem):
            url = item['chapterurl']
            # name_id = item['id_name']
            xs_chaptername = item['chaptername']
            xs_content = item['chaptercontent']
            Sql.insert_bqg_content(xs_chaptername, xs_content, url)
            print('小说存储完毕~')
            return item