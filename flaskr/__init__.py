import os

from flask import Flask

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

    return app
