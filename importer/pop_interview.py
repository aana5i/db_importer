import json
import re


class Populate:
    def __init__(self, mydb):
        self.mydb = mydb

    def get_file(self):
        with open("data/db.json", "r", encoding='utf-8', newline="") as f:
            reader3 = json.load(f)

        for k, v in reader3.items():
            self.insert_into_db(k, v)

    def insert_into_db(self, k, r):
        cursor = self.mydb.cursor()
        print('id', k)
        for _, v in r.items():
            interviews = [v2 for v2 in v.keys() if re.search(r'interview', v2)]

            interview = ['\n'.join(v[i]) for i in interviews if interviews]

            interview = '\n\n'.join([i for i in interview])
            if "high_school" not in v:
                v["high_school"] = ''
            if "university" not in v:
                v["university"] = ''

            cursor.execute("INSERT INTO interviews (id, work, dream, club, work_info, presentation, high_school, university, interviews) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (k, v["work"], v["dream"], v["club"], v["work_info"], v["presentation"], v["high_school"], v["university"], interview))

        # close the connection to the database.
        self.mydb.commit()
        cursor.close()
        print("Done")
