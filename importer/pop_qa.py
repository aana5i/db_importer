import re


class Populate:
    def __init__(self, mydb):
        self.mydb = mydb

    def get_file(self):
        filepath = 'data/qa.txt'
        qa = {}
        with open(filepath, encoding="shift-jis") as fp:
            line = fp.readline()
            cnt = 0

            question = []
            answer_list = ['A', 'B', 'C', 'D', 'E']
            tmp = []
            i = 0
            while line:
                if re.search(r'^Q', line.strip()):
                    question.append(line.strip())
                    i += 1

                if line.strip()[0] in answer_list:
                    tmp.append(line.strip())
                    if cnt == 5:
                        qa[question[i-1]] = tmp
                        tmp = []
                        cnt = -1

                line = fp.readline()
                cnt += 1

        self.insert_into_db(qa)

    def insert_into_db(self, k):
        cursor = self.mydb.cursor()
        ids = 0
        for question, answers in k.items():
            ids += 1
            print(ids, question)
            cursor.execute("INSERT INTO questions (id, text) VALUES (%s,%s)",
                           (ids, question))
            for answer in answers:
                print(answer)
                cursor.execute("INSERT INTO answers (text, question_id) VALUES (%s,%s)",
                               (answer, ids))

        # close the connection to the database.
        self.mydb.commit()
        cursor.close()
        print("Done")
