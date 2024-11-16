# This python class includes all sql texts and database operations.
# The has the advantage of separating database operations from web routing codes
from sqlalchemy import *
from Dbsecrets import DBURI


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
            SELECT T.tid, T.topic, COUNT(Q.qid) 
	        FROM Topics T 
            LEFT OUTER JOIN BelongToRelations R
            ON T.tid = R.tid
            LEFT OUTER JOIN Questions Q
            ON R.qid = Q.qid
            GROUP BY T.tid, T.topic;
        """
        result = self.execute(topicQuery).fetchall()

        # sort topics based on alphabetic order
        # The only exception is "Other", which is fixed to be the last one
        def cmpTopics(t1, t2):
            t1_l = t1[1].lower()
            t2_l = t2[1].lower()
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
        print(result)
        return sorted(result, key=cmp_to_key(cmpTopics))

    # question
    # SELECT qid, text FROM questions Q WHERE Q.qid in (SELECT qid FROM belongtorelations BTR, topics T WHERE BTR.tid=T.tid and T.topic = 'Physics');
    def getQuestionByTopicID(self, tid, page=1, size=10):
        print(f'TOPIC: {tid}'.format(topic=tid))
        return self.execute("SELECT Q.text, Q.qid, T.topic, T.tid  FROM questions Q, topics T, belongtorelations BRT WHERE Q.qid = BRT.qid AND T.tid=BRT.tid AND T.tid=:tid;", {"size": size, "tid": tid})

    '''
    def getQuestion(self, qid):
        cursor = self.execute("SELECT text FROM questions Q WHERE Q.qid = :qid;", {"qid": qid})
        return cursor.fetchone()[0]
    '''
    '''
    def getAnswer(self, qid):
        cursor = self.execute("SELECT text FROM answers A WHERE A.qid = :qid;", {"qid": qid})
        return [answer[0] for answer in cursor]
    '''
    def addAnswer(self, name):
        self.execute('INSERT INTO test(name) VALUES (:name)', {"name": name})

    def getTopicFromTID(self, tid):
        return self.execute('SELECT topic FROM topics T where T.tid=:tid LIMIT 1;', {"tid": tid}).fetchone()

    def getAnswersInQuestionData(self, tid, qid):
        query = "SELECT Q.qid, Q.text, A.aid, A.text, U.username, A.date " \
                "FROM questions Q NATURAL JOIN belongtorelations BRT NATURAL JOIN topics T " \
                "NATURAL JOIN users U INNER JOIN answers A ON Q.qid = A.qid " \
                "WHERE Q.qid=:qid AND T.tid=:tid " \
                "ORDER BY A.date DESC;"
        return self.execute(query, {"tid": tid, "qid": qid})