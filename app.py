from flask import Flask,render_template,redirect,request,session,flash
import webbrowser

from pymongo import MongoClient

import customer_acqusition as ca

app=Flask(__name__) 

client = MongoClient('127.0.0.1', 27017)

db = client.flask_db

users = db.users

returns = users.find()

print(returns)

@app.route("/")
def index():
    return render_template("login.html")

if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(debug=True,port=5000)
