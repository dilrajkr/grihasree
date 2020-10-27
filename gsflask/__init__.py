from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='gspassword'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://gsadmin:gspostgres@localhost:5432/gsdatabase'
db=SQLAlchemy(app)

from gsflask import routes




