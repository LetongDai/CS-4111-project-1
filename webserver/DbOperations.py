# This python class includes all sql texts and database operations.
# The has the advantage of separating database operations from web routing codes
from sqlalchemy import *
from db_secrets import DBURI


DB_URI = DBURI
engine = create_engine(DB_URI)
conn = engine.connect()


class DB:
    def __init__(self):
        self.conn = engine.connect()

    # this is the method for executing the queries and
    def execute(self, sql_text, params=None):
        cursor = self.conn.execute(text(sql_text), params)
        self.conn.commit()
        return cursor

    def close(self):
        self.conn.close()

    # login
    def getUser(self, username):
        user = self.execute("select * from users where username = :name;", {"name": username}).fetchone()
        if user is not None:
            return {"id": user[0], "username": user[1]}
        else:
            return None

    # topics
    def getTopics(self):
        topicQuery = """
            SELECT T.topic, COUNT(Q.qid) 
	        FROM Topics T 
            LEFT OUTER JOIN BelongToRelations R
            ON T.tid = R.tid
            LEFT OUTER JOIN Questions Q
            ON R.qid = Q.qid
            GROUP BY T.topic;
        """
        result = self.execute(topicQuery).fetchall()

        # sort topics based on alphabetic order
        # The only exception is "Other", which is fixed to be the last one
        def cmpTopics(t1, t2):
            t1_l = t1[0].lower()
            t2_l = t2[0].lower()
            if t1_l == "other":
                return 1
            if t2_l == "other":
                return -1
            if t1_l < t2_l:
                return -1
            elif t1_l == t2_l:
                return 0
            else:
                return 1

        from functools import cmp_to_key
        return sorted(result, key=cmp_to_key(cmpTopics))

    # question
    def getQuestionList(self, page=1, size=10):
        return self.execute("SELECT qid,text FROM questions LIMIT :size;", {"size": size})

    def getQuestion(self, qid):
        cursor = self.execute("SELECT text FROM questions Q WHERE Q.qid = :qid;", {"qid": qid})
        return cursor.fetchone()[0]

    # answer
    def getAnswer(self, qid):
        cursor = self.execute("SELECT text FROM answers A WHERE A.qid = :qid;", {"qid": qid})
        return [answer[0] for answer in cursor]

    def addAnswer(self, name):
        self.execute('INSERT INTO test(name) VALUES (:name)', {"name": name})