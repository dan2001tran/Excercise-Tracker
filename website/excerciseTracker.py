from flask import Blueprint, render_template, request, session
from flask_session import Session
import sqlite3



excerciseTracker = Blueprint('excerciseTracker', __name__)

@excerciseTracker.route('/')
def home():
    db = sqlite3.connect('excercise.db')
    cur = db.cursor()
    cur.execute("SELECT * FROM lifts WHERE id='1'")
    
    lift = cur.fetchall()
    length = len(lift)
    return render_template("home.html", lift = lift, message = length, length = length)

@excerciseTracker.route('/add')
def add():
    
    return render_template("add.html")