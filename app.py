import bcrypt
import datetime
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from pytz import timezone
import sqlite3
from tempfile import mkdtemp


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = "metrics.db"


# Routes
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        password = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        con = sqlite3.connect(db)
        cur = con.cursor()

        cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?, ?)", 
                   (username, hashed_password, 0, 0))

        user_id = cur.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchall()[0][0]

        con.commit()
        con.close()

        if user_id:
            session["user_id"] = user_id
            current_datetime = datetime.datetime.now(timezone('US/Eastern'))
            current_time = current_datetime.strftime("%H:%M:%S")
            session["start_time"] = current_time
            print(user_id)

        return redirect("/timer")

    else:
      return redirect("/")


@app.route("/timer", methods=["GET", "POST"])
def timer():
    if request.method == "POST":
        con = sqlite3.connect(db)
        cur = con.cursor()

        cur.execute("INSERT INTO usage SELECT NULL, ?, ?, TIME('now', 'localtime')", (session["user_id"], session["start_time"]))

        con.commit()
        con.close()

        return redirect("/timer")

    else:
        return render_template("timer.html")


