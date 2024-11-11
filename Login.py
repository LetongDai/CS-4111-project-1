from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
login_bp = Blueprint('login', __name__, url_prefix='/login')


@login_bp.route('/login/', methods=('GET', 'POST'))
def login():
    if request.method == "POST":
        username = request.form["name"]
        user = g.conn.getUser(username)
        if user is None:
            flash("user does not exist")
            return render_template("login.html")
        else:
            session["uid"] = user['id']
            session["username"] = user["username"]
            return redirect(url_for("TopicList.topics"))


@login_bp.before_app_request
def loadUser():
    g.uid = session.get("uid")
    if g.uid is not None:
        g.username = session.get("username")


@login_bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for("Login.login"))


def needLogin(req):
    def checkLogin(**kwargs):
        if g.uid is None:
            return redirect(url_for("Login.login"))
        else:
            return req(**kwargs)
    return checkLogin
