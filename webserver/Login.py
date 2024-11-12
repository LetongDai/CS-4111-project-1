from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from functools import wraps

login_bp = Blueprint('Login', __name__,  template_folder="templates")


@login_bp.route('/login/', methods=('GET', 'POST'))
def login():
    session.clear()
    if request.method == "POST":
        username = request.form["name"]
        user = g.conn.getUser(username)
        if user is None:
            flash("user does not exist")
            return render_template("login.html")
        else:
            session["uid"] = user['id']
            session["username"] = user["username"]
            return redirect(url_for("TopicList.listTopics"))
    else:
        return render_template("login.html")


@login_bp.before_app_request
def loadUser():
    g.uid = session.get("uid")
    if g.uid:
        g.username = session.get("username")


@login_bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for("Login.login"))


def needLogin(req):
    @wraps(req)
    def checkLogin(*args, **kwargs):
        if not g.uid:
            return redirect(url_for("Login.login"))
        else:
            return req(*args, **kwargs)
    return checkLogin
