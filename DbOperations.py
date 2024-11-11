# This python class includes all sql texts and database operations.
# The has the advantage of separating database operations from web routing codes
from sqlalchemy import *
import secrets


DB_URI = secrets.DBURI
engine = create_engine(DB_URI)
conn = engine.connect()


class DB:
    def __init__(self):
        self.conn = engine.connect()

    # this is the method for executing the queries and
    def execute(self, sql, params=None):
        cursor = conn.execute(text(sql), params)
        conn.commit()
        return cursor

    def close(self):
        self.conn.close()

    # login
    def getUser(self, username):
        return self.execute("select * from users where username = :name", {"name": username}).fetchone()[0]

    # topics
    def getTopics(self):
        return None

    # question
    def getQuestionList(self, page=1, size=10):
        return self.execute("SELECT qid,text FROM questions LIMIT :size;", {"size": size})

    def getQuestion(self, qid):
        cursor = self.execute("SELECT text FROM questions Q WHERE Q.qid = :qid;", {"qid": qid})
        return cursor.fetchone()[0]

    # answer
    def getAnswer(self, aid):
        cursor = self.execute("SELECT text FROM answers A WHERE A.qid = :qid;", {"qid: qid"})
        return [answer[0] for answer in cursor]