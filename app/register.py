#from app import app
# from flask import render_template,request, url_for, request, redirect, flash, jsonify
# from main import db,engine
from main import *


@app.route("/")
def addbook():
	return render_template("booking_agent_register.html")

@app.route("/register", methods=["GET","POST"])
def register():
	if request.method == "POST":

		req = request.json
		uname = req["uname"]
		password = req["password"]
		fname = req["fname"]
		lname = req["lname"]
		email = req["email"]
		phone = req["phone"]
		address = req["address"]
		gender = req["gender"]
		creditcard = req["credit"]
		dob = req["dob"]

		resultproxy = db.execute("SELECT * FROM booking_agent WHERE uname = (:uname) or email=(:email) or phone=(:phone) or creditcard=(:creditcard)",{"uname": uname,"email": email,"phone": phone, "creditcard": creditcard})

		ct = 0
		for _ in resultproxy:
			ct = 1
			break
		
		if (ct > 0) :
			return "0"
		else:
			db.execute("INSERT INTO booking_agent (uname, password,fname,lname,email,phone,address,gender,creditcard,dob) VALUES (:uname, :password,:fname,:lname,:email,:phone,:address,:gender,:creditcard,:dob)",
			{"uname": uname, "password": password, "fname":fname,"lname":lname, "email":email,"phone":phone,"address":address, "gender":gender, "creditcard":creditcard, "dob":dob})
			db.commit()
			return "1"

	return "NULL"