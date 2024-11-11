from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from Login import needLogin

topic_bp = Blueprint('topics', __name__, url_prefix='/topics')


@topic_bp.route("/topics/")
@needLogin
def listTopics():
    topics = g.conn.getTopics()
    return render_template("topics.html", data=topics)
