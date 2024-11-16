from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from Login import needLogin

questions_bp = Blueprint('QuestionList', __name__, template_folder="templates")


@questions_bp.route("/topics/<topic_id>")
@needLogin
def listQuestionsInTopic(topic_id):
    questions = g.conn.getQuestionByTopicID(topic_id)
    parsed = [thing for thing in questions]
    topic_name = g.conn.getTopicFromTID(topic_id)
    return render_template("questions.html", data=parsed, topic_name=topic_name, tid=topic_id)
