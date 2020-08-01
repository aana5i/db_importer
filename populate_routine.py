import argparse
from db_helper import DbHelper


class PopulateDb:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="argparse")
        self.parser.add_argument("--host", '-host', type=str, default='localhost', help="DBホスト名を入力してください")
        self.parser.add_argument("--user", '-user', type=str, default='root', help="ユーザー名を入力してください")
        self.parser.add_argument("--passwd", '-passwd', type=str, default='', help="パスワードを入力してください")
        self.parser.add_argument("--db", '-db', type=str, required=True, help="DB名を入力してください")
        self.parser.add_argument("--port", '-port', type=int, default=3306, help="DBポートを入力してください")
        self.parser.add_argument("--importer", '-importer', type=str, required=True, help="インポーターを入力してください")
        self.args = self.parser.parse_args()
        self.open_importer()

    def db_connect(self):
        _mydb = DbHelper(host=self.args.host,
                         user=self.args.user,
                         passwd=self.args.passwd,
                         db=self.args.db,
                         port=self.args.port)
        self.mydb = _mydb.db_connect()

    def open_importer(self):
        self.db_connect()
        mod = __import__(f'importer.{self.args.importer}', fromlist=['Populate'])
        Populate = getattr(mod, 'Populate')
        p = Populate(self.mydb)
        p.get_file()


_p = PopulateDb()


'''
USAGE
populate_rountine.py -db caseStudy -passwd root -port 3306 -importer pop_interview
'''