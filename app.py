from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

app = Flask(__name__) 
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'a3f5c2e9d4c8b6a1f7e8d9c3a0b5f7c1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.config['SESSION_COOKIE_SECURE'] = True  

bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)

from flask import render_template, redirect, url_for, flash, session, request, jsonify, abort
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from functools import wraps
from datetime import datetime, timedelta
import requests, os, time, json, re, random

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

@app.route('/home')
def home_page():
    return render_template('page1.html')

@app.route('/register')
def register_page():
    return render_template('page2.html')

@app.route('/summary')
def summary_page():
    return render_template('page3.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
