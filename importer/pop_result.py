import json


class Populate:
    def __init__(self, mydb):
        self.mydb = mydb

    def get_file(self):
        with open("data/results.json", "r", encoding='utf-8', newline="") as f:
            reader3 = json.load(f)

        for r in reader3['tekikensa']['info']:
            result_phrase = {
                'resultName': r['resultName'].strip(),
                'resultId': r['resultId'].strip(),
                'analysisId': r['analysisId'].strip(),
                'commentStudent': r['commentStudent'].strip(),
                'commentGuardian': r['commentGuardian'].strip()
            }

            for job in r['job']:
                jobs = {
                    'jobName': job['jobName'].strip(),
                    'jobDescription': job['jobDescription'].strip(),
                    'analysisId': r['analysisId'].strip()
                }
                self.insert_into_db(json.dumps(jobs), 'jobs')

            for study in r['study']:
                studies = {
                    'studyName': study['studyName'].strip(),
                    'studyDescription': study['studyDescription'].strip(),
                    'analysisId': r['analysisId'].strip()
                }
                self.insert_into_db(json.dumps(studies), 'studies')
            self.insert_into_db(json.dumps(result_phrase), 'result_table')

    def insert_into_db(self, r, flg):
        cursor = self.mydb.cursor()
        json_obj = json.loads(r)

        if flg == 'result_table':
            print("resultName:", json_obj["resultName"])
            print("resultId:", json_obj["resultId"])
            print("analysisId:", json_obj["analysisId"])
            print("commentStudent:", json_obj["commentStudent"])
            print("commentGuardian:", json_obj["commentGuardian"])
            print('---')
            cursor.execute("INSERT INTO result_phases (id, type, reasons_student, reasons_teacher, result_name) VALUES (%s,%s,%s,%s,%s)",
                           (json_obj["resultId"], json_obj["analysisId"], json_obj["commentStudent"], json_obj["commentGuardian"], json_obj["resultName"]))

        elif flg == 'jobs':
            print("jobName:", json_obj["jobName"])
            print("jobDescription:", json_obj["jobDescription"])
            print("analysisId:", json_obj["analysisId"])
            print('---')
            cursor.execute("INSERT INTO jobs (type, job_name, job_description) VALUES (%s,%s,%s)",
                           (json_obj["analysisId"], json_obj["jobName"], json_obj["jobDescription"]))
        elif flg == 'studies':
            print("studyName:", json_obj["studyName"])
            print("studyDescription:", json_obj["studyDescription"])
            print("analysisId:", json_obj["analysisId"])
            print('---')
            cursor.execute("INSERT INTO studies (type, study_name, study_description) VALUES (%s,%s,%s)",
                           (json_obj["analysisId"], json_obj["studyName"], json_obj["studyDescription"]))

        #close the connection to the database.
        self.mydb.commit()
        cursor.close()
        print("Done")
