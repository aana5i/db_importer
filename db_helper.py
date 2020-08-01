# -*- coding: utf-8 -*-
import pymysql


class DbHelper:
    def __init__(self, host, user, passwd, db, port):
        self.host = host,
        self.user = user,
        self.passwd = passwd,
        self.db = db,
        self.port = port

    def db_connect(self):
        return pymysql.connect(host=self.host[0],
                               user=self.user[0],
                               passwd=self.passwd[0],
                               db=self.db[0],
                               port=self.port)


'''
USAGE
db = DbHelper(host, user, passwd, db, port)

'''
