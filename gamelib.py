import os
from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy


port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run()