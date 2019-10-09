# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import  app

from app.models import  Service
from app import db
from flask import request
from werkzeug.urls import url_parse
from datetime import datetime



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    services = Service.query.order_by(Service.id).all()
    return render_template('index.html', title='Home', services = services)



@app.route('/import', methods=['GET', 'POST'])
def importbase():
    f = open('app/costur.py', 'r')
    code_str = f.read()
    f.close()
    code = compile(code_str, 'app/costur.py', 'exec')
    exec(code)
    services = Service.query.order_by(Service.id).all()
    return render_template('index.html', title='Home', services = services)



@app.route('/test', methods=['GET', 'POST'])
def test():
    return "Hello, World!"
