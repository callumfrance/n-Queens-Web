import os

from flask import (
        Flask, render_template, request, url_for, redirect, flash
)

from .mvc import main

def create_app(test_config=None):
    # creates and configures the app
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = "test"
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def base():
        return redirect(url_for('board_select'))

    @app.route('/n_queens/<int:n_size>')
    def n_queens(n_size=5):
        if n_size > 50:
            n_size = 50
            flash('For performance reasons, n has been capped to 50')
        elif n_size < 1:
            n_size = 1
            flash('n must be at least 1 (obviously)')

        b = main.run_n_queens('html', n_size)
        return render_template('board.html', board_display=b, n_size=n_size)

    @app.route('/board_select', methods=('GET', 'POST'))
    def board_select():
        if request.method == 'POST':
            n_size_bs = request.form['n_size']
            error = None

            if n_size_bs is None:
                error = 'n was not set'

            if error is None:
                return redirect(url_for('n_queens', n_size=n_size_bs))
            else:
                flash(error)

        return render_template('board_select.html')


    return app
