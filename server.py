from flask import Flask, render_template,url_for,redirect,request
import csv
import math
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
            data=request.form.to_dict()
            data_csv(data)
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



def write_data_csv(data):
    email = data['email']
    subject = data['subject']
    message = data["message"]
    with open('db.csv', 'a', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([email,subject,message])

app.run()
