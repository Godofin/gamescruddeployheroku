import os
from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import re
from importlib import reload
def get_port():
  return int(os.environ.get("PORT", 5000))
    return (delta.days)

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=get_port())