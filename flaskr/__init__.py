import os

from flask import (
        Flask, render_template
)

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
        a = main.run_n_queens('html', 5)
        return render_template('base.html', board_display=a)

    return app
