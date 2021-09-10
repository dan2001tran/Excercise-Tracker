from flask import Flask, config

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123abc'

    from .excerciseTracker import excerciseTracker
    from .auth import auth

    app.register_blueprint(excerciseTracker, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app