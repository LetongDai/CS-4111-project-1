from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from Login import needLogin

questions_bp = Blueprint('QuestionList', __name__, template_folder="templates")


@questions_bp.route("/topics/<topic_id>", methods=['POST', 'GET'])
@needLogin
def listQuestionsInTopic(topic_id):
    questions = g.conn.getQuestionByTopicID(topic_id)
    parsed = [thing for thing in questions]
    topic_name = g.conn.getTopicFromTID(topic_id)
    announcement_data = g.conn.getLatestAnnouncement(topic_id).fetchone()
    if request.method == 'POST':
        if 'qid' in request.form:
            g.conn.deleteQuestion(request.form['qid'], g.uid)
        elif 'userQuestionText' in request.form:
            g.conn.addQuestionToTopic(topic_id, request.form['userQuestionText'], g.uid)
        return redirect(url_for('QuestionList.listQuestionsInTopic', topic_id=topic_id))

    return render_template("questions.html", data=parsed, topic_name=topic_name, tid=topic_id, loggedInUID=g.uid, announcementData=announcement_data)
