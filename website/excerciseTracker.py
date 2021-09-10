from flask import Blueprint

excerciseTracker = Blueprint('excerciseTracker', __name__)

@excerciseTracker.route('/')
def home():
    return "<h1>Test</h1>"