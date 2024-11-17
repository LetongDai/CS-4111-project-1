from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from Login import needLogin

answers_bp = Blueprint('AnswerList', __name__, template_folder="templates")


@answers_bp.route("/topics/<topic_id>/<question_id>", methods=['POST', 'GET'])
@needLogin
def listAnswersInQuestion(topic_id, question_id):
    data = g.conn.getAnswersInQuestionData(topic_id, question_id)
    topic_name = g.conn.getTopicFromTID(topic_id)
    data = [topic_name, data.fetchall()]
    userHaveAnswerHere = g.conn.doesUserHaveAnswerInQuestion(g.uid, question_id)

    if request.method == 'POST':
        if 'qid' in request.form and 'aid' in request.form:
            g.conn.deleteAnswer(request.form['aid'], request.form['qid'], g.uid)

        elif 'answerEditTEXT' in request.form and 'answerEditQID' in request.form and 'answerEditAID' in request.form:
            g.conn.updateAnswer(request.form['answerEditTEXT'], request.form['answerEditQID'], request.form['answerEditAID'], g.uid)

        elif 'userAnswerInput' in request.form:
            #print(request.form['userAnswerInput'])
            g.conn.insertAnswer(request.form['userAnswerInput'], question_id, g.uid)

        return redirect(url_for('AnswerList.listAnswersInQuestion', topic_id=topic_id, question_id=question_id))
    return render_template('answers.html', data=data, loggedInUID=g.uid, canUserAnswer=userHaveAnswerHere)
