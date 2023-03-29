from flask import Flask,render_template,redirect,request,session,flash,url_for,send_from_directory
import os
import webbrowser
from pymongo import MongoClient

import analytic as an

app=Flask(__name__)

client = MongoClient('127.0.0.1', 27017)

db = client.get_database('dedrone')
users = db.users

# returns = users.insert_one({"sample":"test 1"}).inserted_id
# print(users.find_one())

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/overview")
def overview():
    return render_template("overview.html")

@app.route("/cost")
def cost():
    return render_template("cost.html")

@app.route("/login")
def loging():
    return render_template("login.html")

@app.route("/statistics")
def stat():
    return render_template("statistics.html")

@app.post("/plan")
def plan():
    return render_template("plan.html")

@app.post("/order")
def order():
    return render_template("order.html")

@app.post("/live")
def live():
    return render_template("live.html")

@app.get("/availability")
def availability():
    return render_template("availability.html")

@app.route("/business",methods = ['POST','GET'] )
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

@app.post("/register")
def regp():
    if request.method == "POST":
        name = request.form.get("Name")
        org = request.form.get("Org")
        gst = request.form.get("GSTno")
        email = request.form.get("email")
        password = request.form.get("password")
        print("\n\n"+name+org+gst+email+password+"\n\n")
        # user_found = users.find_one({"name": name}

        # if user_found:
        #         return redirect("/")
        #         # message = 'There already is a user by that name'
        #         # return render_template('index.html')
        #         #, message=message)
        # if email_found:
        #         return redirect("/")
        #         # message = 'This email already exists in database'
        #         # return render_template('index.html')
        #         #, message=message)
        # else:
        user_input = {'name': name, 'email': email, 'password': password,'org':org,
                           'gst':gst}
        users.insert_one(user_input)
        return redirect("/")

# @app.post("/login")
# def loginp():
#     message = 'Please login to your account'
#     if "email" in session:
#         return redirect(url_for("logged_in"))

#     if request.method == "POST":
#         email = request.form.get("email")
#         password = request.form.get("password")

       
#         email_found = records.find_one({"email": email})
#         if email_found:
#             email_val = email_found['email']
#             passwordcheck = email_found['password']
            
#             if bcrypt.checkpw(password.encode('utf-8'), passwordcheck):
#                 session["email"] = email_val
#                 return redirect(url_for('logged_in'))
#             else:
#                 if "email" in session:
#                     return redirect(url_for("logged_in"))
#                 message = 'Wrong password'
#                 return render_template('login.html', message=message)
#         else:
#             message = 'Email not found'
#             return render_template('login.html', message=message)
#     return render_template('login.html', message=message)



if __name__ == "__main__":
    # webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(debug=True,host='0.0.0.0') 
