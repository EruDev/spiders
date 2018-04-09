from BiQuGe import settings
import pymysql

MYSQL_HOST = settings.MYSQL_HOST
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB


conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, db=MYSQL_DB, charset='utf8')
cur = conn.cursor()


class Sql:

    @classmethod
    def insert_bqg_name(cls, xs_name, xs_author, last_update, name_id):
        """插入小说名"""
        sql = 'INSERT INTO biquge_name (xs_name, xs_author, last_update, name_id) VALUES (%(xs_name)s, %(xs_author)s, %(last_update)s, %(name_id)s)'
        # 字段名
        value = {
            'xs_name': xs_name,
            'xs_author': xs_author,
            'last_update': last_update,
            'name_id': name_id,
        }
        cur.execute(sql, value)
        conn.commit()
        print('成功存储一条数据~')

    @classmethod
    def insert_bqg_content(cls, xs_chaptername, xs_content, url):
        """插入小说内容"""
        sql = 'INSERT INTO biquge_novel_content (xs_chaptername, xs_content, url) VALUES (%(xs_chaptername)s, %(xs_content)s, %(url)s)'
        # 字段名
        value = {
            'xs_chaptername': xs_chaptername,
            'xs_content': xs_content,
            'url': url,
        }
        cur.execute(sql, value)
        conn.commit()

    @classmethod
    def select_chapter(cls, url):
        # 去重
        sql = 'SELECT EXISTS(SELECT 1 FROM biquge_novel_content WHERE url=%(url)s)'
        value = {'url': url}
        cur.execute(sql, value)
        # 返回查询结果的第一条数据
        return cur.fetchall()[0]

    @classmethod
    def select_name(cls, name_id):
        # 去重
        sql = 'SELECT EXISTS(SELECT 1 FROM biquge_name WHERE name_id=%(name_id)s)'
        value = {'name_id': name_id}
        cur.execute(sql, value)
        # 返回查询结果的第一条数据
        return cur.fetchall()[0]