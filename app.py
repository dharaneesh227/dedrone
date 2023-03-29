from flask import Flask,render_template,redirect,request,session,flash,url_for,send_from_directory
import os
import webbrowser

from pymongo import MongoClient

# import customer_acqusition as ca

app=Flask(__name__) 

client = MongoClient('127.0.0.1', 27017)

db = client['dedrone']
users = db.users

# returns = users.insert_one({"sample":"test 1"}).inserted_id
# print(users.find_one())

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/overview")
def overview():
    return render_template("overview.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.get("/availability")
def availability():
    return render_template("availability.html")

@app.post("/business")
def business():
    return render_template("business.html")

@app.get("/details")
def details():
    return render_template("details.html")

@app.get("/potentialuser")
def potentialuser():
    return render_template("potentialuser.html")


@app.get("/tracking")
def tracking():
    return render_template("tracking.html")


if __name__ == "__main__":
    # webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(debug=True,) 
