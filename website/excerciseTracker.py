from flask import Blueprint, render_template, request, session
from flask_session import Session
import sqlite3

from werkzeug.utils import redirect



excerciseTracker = Blueprint('excerciseTracker', __name__)

@excerciseTracker.route('/', methods= ['GET', 'POST'] )
def home():

    db = sqlite3.connect('excercise.db')
    cur = db.cursor()
    cur.execute("SELECT * FROM lifts")
    
    lift = cur.fetchall()
    length = len(lift)

    cur.close()
    db.close()
    return render_template("home.html", lift = lift, message = length, length = length)

@excerciseTracker.route('/add', methods= ['GET', 'POST'])
def add():
    if request.method == "POST":

        messageGateExcercise = False
        messageGateRPE = False
        messageGateWeight = False
        messageGateReps = False

        userInput = False

        excercise = request.form.get('Excercise')
        if not excercise:
             messageGateExcercise = True
             userInput = True
        weight = request.form.get('Weight')
        if not weight:
             messageGateWeight = True
             userInput = True
        reps = request.form.get('Rep-Range')
        if not reps:
             messageGateReps = True
             userInput = True
        rpe3 = request.form.get('RPE3')
        rpe2 = request.form.get('RPE2')
        rpe1 = request.form.get('RPE1')

        if not rpe1 and not rpe2 and not rpe3:
            messageGateRPE = True
            userInput = True
        if userInput:
            return render_template("add.html", messageGateWeight = messageGateWeight, messageGateExcercise = messageGateExcercise, messageGateReps = messageGateReps, messageGateRPE = messageGateRPE)
        
        db = sqlite3.connect('excercise.db')
        cur = db.cursor()  
        cur.execute("INSERT INTO lifts (excercise, weight, reps, RPE3, RPE2, RPE1) VALUES (?, ?, ?, ?, ?, ?)", (excercise.lower(), weight, reps, rpe3, rpe2, rpe1))
        
        db.commit()
        cur.close()
        db.close()
        return redirect("/")
    else:

        return render_template("add.html", messageGate = False)

@excerciseTracker.route('/delete', methods= ['GET', 'POST'])
def delete():
    if request.method == "POST":
        messageGateExcercise = False
        userInput = False
        excercise = request.form.get('Excercise')
        excercise.lower();
        if not excercise:
             messageGateExcercise = True
             userInput = True

        if userInput:
            return render_template("add.html", messageGateExcercise = messageGateExcercise)
        
        db = sqlite3.connect('excercise.db')
        cur = db.cursor()  
        cur.execute("DELETE FROM lifts WHERE excercise =?", (excercise,))
        
        db.commit()
        cur.close()
        db.close()
        return redirect("/")
    
    else:

        return render_template("delete.html")

@excerciseTracker.route('/update', methods= ['GET', 'POST'])
def update():
    if request.method == "POST":

        messageGateExcercise = False
        messageGateUpdate = False

        userInput = False

        excercise = request.form.get('Excercise')
        if not excercise:
             messageGateExcercise = True
             userInput = True
        
        weight = request.form.get('Weight')
        reps = request.form.get('Rep-Range')
        rpe3 = request.form.get('RPE3')
        rpe2 = request.form.get('RPE2')
        rpe1 = request.form.get('RPE1')

        if not weight and not reps and not rpe1 and not rpe2 and not rpe3:
            messageGateUpdate = True
            userInput = True
        if userInput:
            return render_template("update.html", messageGateExcercise = messageGateExcercise, messageGateUpdate = messageGateUpdate)
        
        db = sqlite3.connect('excercise.db')
        cur = db.cursor()
        if weight:
            cur.execute("UPDATE lifts SET weight=? WHERE excercise=?",(weight, excercise.lower(),))
        if reps:
            cur.execute("UPDATE lifts SET reps=? WHERE excercise=?",(reps, excercise.lower(),))
        if rpe1:
            cur.execute("UPDATE lifts SET RPE1=? WHERE excercise=?",(rpe1, excercise.lower(),))
        if rpe2:
            cur.execute("UPDATE lifts SET RPE2=? WHERE excercise=?",(rpe2, excercise.lower(),))
        if rpe3:
            cur.execute("UPDATE lifts SET RPE3=? WHERE excercise=?", (rpe3, excercise.lower(),))
        
        db.commit()
        cur.close()
        db.close()
        return redirect("/")
    else:

        return render_template("update.html", messageGate = False)