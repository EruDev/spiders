# coding: utf-8
import pymysql
from hdbeemovie import settings
MYSQL_HOST = settings.MYSQL_HOST
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWD = settings.MYSQL_PASSWD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

conn = pymysql.connect(host=MYSQL_HOST,
                     db=MYSQL_DB,
                     port=MYSQL_PORT,
                     user=MYSQL_USER,
                     passwd=MYSQL_PASSWD,
                     charset='utf8')
cursor = conn.cursor()
print('连接数据库成功!')


class MySql(object):

    @classmethod
    def insert_db(cls, item):
        """
        插入数据
        :param item:
        :return:
        """
        try:
            sql = "INSERT INTO beemovie (current_movie_url, next_page_url, current_page_url, m_id, title, director, scriptwriter, actor, m_type, localtion, languages, times, m_time, others, score, img_src, introduce) VALUES (%(current_movie_url)s, %(next_page_url)s, %(current_page_url)s, %(m_id)s, %(title)s, %(director)s, %(scriptwriter)s, %(actor)s, %(m_type)s, %(localtion)s, %(languages)s, %(times)s, %(m_time)s, %(others)s, %(score)s, %(img_src)s, %(introduce)s)"
            values = {
                'current_movie_url': item['current_movie_url'],
                'next_page_url': item['next_page_url'],
                'current_page_url': item['current_page_url'],
                'm_id': item['m_id'],
                'title': item['title'],
                'director': item['director'],
                'scriptwriter': item['scriptwriter'],
                'actor': item['actor'],
                'm_type': item['m_type'],
                'localtion': item['localtion'],
                'languages': item['languages'],
                'times': item['times'],
                'm_time': item['m_time'],
                'others': item['others'],
                'score': item['score'],
                'img_src': item['img_src'],
                'introduce': item['introduce'],
            }
            cursor.execute(sql, values)
            conn.commit()
            print('Sql文件----成功插入一条数据~')
        except Exception as e:
            print(e)
            conn.rollback()

    @classmethod
    def find_next_page_url(cls):
        """
        电影下一页对应的URL
        :return:
        """
        sql = 'SELECT id, current_movie_url, next_page_url FROM beemovie ORDER BY id DESC LIMIT 1'
        cursor.execute(sql)
        result = cursor.fetchall()[0][2]

        return result

    @classmethod
    def find_current_movie_url(cls):
        """
        当前电影对应的URL
        :return:
        """
        sql = 'SELECT id, current_movie_url, next_page_url FROM beemovie ORDER BY id DESC LIMIT 1'
        cursor.execute(sql)
        result = cursor.fetchall()[0][1]

        return result

    @classmethod
    def find_last_movie_page_url(cls):
        """
        数据库存储的最后一条电影页面的URL
        :return:
        """
        sql = 'SELECT id, current_page_url FROM beemovie ORDER BY id DESC LIMIT 1'
        cursor.execute(sql)
        result = cursor.fetchall()[0][1]

        return result

    @classmethod
    def find_last_movie_url(cls):
        """
        数据库存储的最后一条电影的URL
        :return:
        """
        li = list()
        current_page_url = cls.find_last_movie_page_url()
        sql = 'SELECT id, current_movie_url FROM beemovie WHERE current_page_url="%s"' % current_page_url
        cursor.execute(sql)
        result = cursor.fetchall()
        for m_url in result:
            li.append(m_url[1])

        return li

    @classmethod
    def find_next_current_page_url(cls):
        """
        数据库存储的最后一条电影的下一页的URL
        :return:
        """
        sql = 'SELECT next_page_url,current_page_url FROM beemovie ORDER BY id DESC LIMIT 1'
        cursor.execute(sql)
        result = cursor.fetchall()[0]

        return result[0], result[1]

# if __name__ == '__main__':
#     result = MySql.find_last_movie_url()
#     print(result)

