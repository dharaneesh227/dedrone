from flask import Flask,render_template,redirect,request,session,flash

from pymongo import MongoClient

app=Flask(__name__) 

client = MongoClient('127.0.0.1', 27017)

db = client.flask_db

users = db.users

returns = users.find()

print(returns)
