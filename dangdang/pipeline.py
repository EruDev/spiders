# coding: utf-8
import pymysql
from config import *


class MyDB(object):

    def __init__(self):
        """
        数据库基本配置
        """
        self.host = MySQL_HOST
        self.user = MySQL_USER
        self.password = MySQL_PASSWORD
        self.db = MySQL_DB
        self.charset = 'utf8'

        self.conn = pymysql.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    db=self.db,
                                    charset=self.charset)
        self.cur = self.conn.cursor()

    def create_table(self):
        """
        创建表
        :return:
        """
        try:

            self.cur.execute('DROP TABLE IF EXISTS dangdang')
            table = 'CREATE TABLE dangdang (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, title VARCHAR(255) NULL, price VARCHAR(255) NULL, author VARCHAR(255) NULL,timer VARCHAR(255), press VARCHAR(255))'
            self.cur.execute(table)
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.cur.close()
            self.conn.close()

    def save_to_mysql(self, title, price, author, timer, press):
        """
        插入数据
        :param title:
        :param price:
        :param author:
        :param timer:
        :param press:
        :return:
        """
        try:

            self.cur.execute('INSERT INTO dangdang (title, price, author, timer, press) VALUES (%s, %s, %s, %s, %s)', (title, price, author, timer, press))
            print('插入数据成功, %s, %s, %s, %s, %s' % (title, price, author, timer, press))
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.cur.close()
            self.conn.close()