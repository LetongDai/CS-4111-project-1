from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from Login import needLogin

answers_bp = Blueprint('AnswerList', __name__, template_folder="templates")


@answers_bp.route("/topics/<topic_id>/<question_id>")
@needLogin
def listAnswersInQuestion(topic_id, question_id):


    data = g.conn.getAnswersInQuestionData(topic_id, question_id)
    topic_name = g.conn.getTopicFromTID(topic_id)
    data = [topic_name, data.fetchall()]
    print(g.username)

    return render_template('answers.html', data=data)
    #return render_template("answers.html", data=[('hi'), ('bye')])
