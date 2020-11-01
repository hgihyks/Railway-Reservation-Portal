from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:1234@localhost:5432/temp")
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

app.secret_key = '12345678' ''' this key is used to communicate with database.'''
#Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/addbook")
def addbook():
	return render_template("addbook.html")

@app.route("/bookadd", methods=["POST"])
def bookadd():
	isbn=request.form.get("isbn")
	title=request.form.get("title")
	author=request.form.get("author")
	year=request.form.get("year")
	
	db.execute("INSERT INTO first (id, name) VALUES (:id, :name)",
			{"id": isbn, "name": title}) 
	db.commit() 
	return render_template("addbook.html")

if __name__ == '__main__':
	app.run(debug=True)