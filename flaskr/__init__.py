import os

from flask import Flask

from .mvc import main

def create_app(test_config=None):
    # creates and configures the app
    app = Flask(__name__, instance_relative_config=True)
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return('Hello world')

    @app.route('/n_queens')
    def n_queens():
        return main.run_n_queens('plaintext', 5)

    return app
