import os

from flask import Flask, redirect, render_template
from sampleapp.form import MainForm
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.metadata.clear()
    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

        return app