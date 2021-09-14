from flask import Blueprint, render_template, request, session
from flask_session import Session
import sqlite3



excerciseTracker = Blueprint('excerciseTracker', __name__)

@excerciseTracker.route('/', methods= ['GET', 'POST'] )
def home():

    db = sqlite3.connect('excercise.db')
    cur = db.cursor()
    cur.execute("SELECT * FROM lifts WHERE id='1'")
    
    lift = cur.fetchall()
    length = len(lift)
    return render_template("home.html", lift = lift, message = length, length = length)

@excerciseTracker.route('/add', methods= ['GET', 'POST'])
def add():
    if request.method == "POST":
        excercise = request.form.get('Excercise')
        if not excercise:
             return render_template("add.html", messageGate = True, message = "Please enter an excercise")
    else:

        return render_template("add.html", messageGate = False)