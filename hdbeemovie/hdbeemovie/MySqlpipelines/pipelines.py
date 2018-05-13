# coding: utf-8
from hdbeemovie.items import HdbeemovieItem
from .Sql import MySql


class HdbbeePipeline(object):
    def process_item(self, item, spider):
        """
        判断类型,然后入库
        :param item:
        :param spider:
        :return:
        """
        if isinstance(item, HdbeemovieItem):
            try:
                MySql.insert_db(item)
                print('pipelines文件---成功插入数据库~')
                print(item)
            except Exception as e:
                print(e)
                print('失败！')