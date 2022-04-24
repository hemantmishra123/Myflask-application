from flask import Flask, render_template,url_for,redirect,request
import csv
import math
#import pandas as pd 
#mport numpy as np
import sqlite3 
app = Flask(__name__)
#this is the database file.
conn=sqlite3.connect('database.db')
#it is the cursor to screen.
c = conn.cursor()
#c.execute("INSERT INTO database VALUES")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup' ,methods=['GET','POST'])
def signup():
    return render_template('register,html')

@app.route('/datafinder' ,methods=['GET','POST'])
def datafinder():
    email=request.form.get('email')
    password=request.form.get('password')
    return "the email {} and password{}  ".format(email,password)


@app.route('/submit_form', methods = ['GET','POST'] )
def submit():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_data_csv(data)
            message = 'Form Submitted, We will get in touch to you shortly!!'
            return render_template('thankyou.html',message=message)
        except:
            message = "DID NOT SAVE DATA TO DATABASE."
            return render_template('thankyou.html',message=message)
    else:
        message = "FORM NOT SUBMITTED"
        return render_template('thankyou.html',message=message)


@app.route('/submit_data', methods = ['GET','POST'] )
def function():
    if request.method=="POST":
        try:

            email=request.form.get('email')
            password=request.form.get('password')
            message="Registration successfull"
            return render_template('thankyou.html',message=message)
        except:
            message = "DID NOT SAVE DATA TO DATABASE."
            return render_template('thankyou.html',message=message)
    else:
        message = "FORM NOT SUBMITTED"
        return render_template('thankyou.html',message=message)

def data_csv(data):
    name=data['fname']
    email=data['femail']
    phone=data['fphone']
    password=data['fpass']
    cpass=data['fcpass']
    with open('db.csv', 'a', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([name,email,phone,password,cpass,])


@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')


#it is the function for writing ..
def write_data_csv(data):
    email = data['email']
    subject = data['subject']
    message = data["message"]
    with open('db.csv', 'a', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([email,subject,message])

if __name__ == "__main__":
    app.run(debug=True, port=8000)
