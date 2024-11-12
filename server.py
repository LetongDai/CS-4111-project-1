
"""
Columbia's COMS W4111.001 Introduction to Databases
Example Webserver
To run locally:
    python3 server.py
Go to http://localhost:8111 in your browser.
A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""
import os
from flask import Flask, render_template, g, session

from DbOperations import DB
from Login import needLogin, login_bp
from TopicList import topic_bp

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
app.register_blueprint(login_bp)
app.register_blueprint(topic_bp)
app.secret_key = "secret"
app.config["SESSION_TYPE"] = 'memcached'


@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request.

  The variable g is globally accessible.
  """
  try:
    g.conn = DB()
  except:
    print("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass


@app.route('/questions')
@needLogin
def questions():
  cursor = g.conn.getQuestionList()
  return render_template("questions.html", data=[(thing[0],thing[1]) for thing in cursor]) # extremely verbose but its self-documenting code!


'''
Included By Edward
'''
@app.route('/answer/<qid>')
@needLogin
def show_answers(qid):
    # Customize the answer based on `item`
    question = g.conn.getQuestion(qid)
    answers = g.conn.getAnswer(qid)

    return render_template('answer.html', data=[question, answers])


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:

        python3 server.py

    Show the help text using:

        python3 server.py --help

    """

    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

  run()
