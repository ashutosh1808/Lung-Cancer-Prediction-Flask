from flask import Flask,render_template,session,request,redirect,url_for
from sqlite3 import *
import pickle
import hashlib
from flask_mail import Mail,Message
from random import randrange

app=Flask(__name__)
app.secret_key="ashutoshrocks"
app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"]=587
app.config["MAIL_USERNAME"]="testerbrucewayne@gmail.com"
app.config["MAIL_PASSWORD"]="tradzfiylzdnmqgc"
app.config["MAIL_USE_TLS"]=True
app.config["MAIL_USE_SSL"]=False

mail=Mail(app)

@app.route("/",methods=["GET","POST"])
def home():
	if "username" in session:
		con=None
		try:
			con=connect("lung_cancer.db")
			cursor=con.cursor()
			sql="select * from patients"
			cursor.execute(sql)
			data=cursor.fetchall()
			return render_template("home.html",name=session["username"],msg=data)
		except Exception as e:
			return render_template("home.html",msg=e)
		finally:
			if con is not None:	con.close()
	else:
		return redirect(url_for("login"))

@app.route("/logout",methods=["GET","POST"])
def logout():
	session.clear()
	return redirect(url_for("login"))

@app.route("/gp",methods=["GET","POST"])
def gp():
	return render_template("predict.html")

@app.route("/login",methods=["GET","POST"])
def login():
	if request.method=="POST":
		un=request.form["un"]
		pw=request.form["pw"]
		con=None
		try:
			con=connect("auth.db")
			cursor=con.cursor()
			sql="select * from users where username='%s' and password='%s'"
			cursor.execute(sql%(un,pw))
			data=cursor.fetchall()
			if len(data)==0:
				return render_template("login.html",msg="invalid login")
			else:
				session["username"]=un
				return redirect(url_for("home"))
		except Exception as e:
			return render_template("login.html",msg=e)
		finally:
			if con is not None:	
				con.close()
	else:
		return render_template("login.html")

@app.route("/about",methods=["GET","POST"])
def about():
	return render_template("about.html")

@app.route("/pred",methods=["GET","POST"])
def pred():
	if request.method=="POST":
		age=int(request.form["age"])
		alc=int(request.form["ac"])
		pp=int(request.form["pp"])
		cd=int(request.form["cd"])
		with open("lc.model","rb") as f:
			model=pickle.load(f)
		d=[[age,alc,pp,cd]]
		res=model.predict(d)
		con=None
		try:
			con=connect("lung_cancer.db")
			cursor=con.cursor()
			sql="insert into patients values('%d','%d','%d','%d','%s')"
			cursor.execute(sql%(age,alc,pp,cd,res[0]))
			con.commit()
			return render_template("predict.html",msg=res)
		except Exception as e:
			con.rollback()
			return render_template("predict.html",msg=e)
		finally:
			if con is not None:	con.close()
	else:
		return render_template("predict.html")
@app.route("/signup",methods=["GET","POST"])
def signup():
	if request.method=="POST":
		un=request.form["un"]
		length=int(request.form["length"])
		pw=""
		text="abcdefghijklmnopqrstuvwxyz"
		if request.form.get("uc"):
			text+=text.upper()
		if request.form.get("di"):
			text+="0123456789"
		for i in range(length):
			pw+=text[randrange(len(text))]
		msg=Message("Greetings from LCD App",sender="testerbrucewayne@gmail.com",recipients=[un])
		msg.body=" Greetings user! "+"\n"+" Your password for LCD is: "+str(pw)+"\n"+"Regards, "+"\n"+"Team LCD"
		mail.send(msg)
		con=None
		try:
			con=connect("auth.db")	
			cursor=con.cursor()
			sql="insert into users values('%s','%s')"
			cursor.execute(sql%(un,pw))
			con.commit()
			return redirect(url_for('login'))
		except:
			con.rollback()
			return render_template("signup.html",msg="User already present!")
		finally:
			if con is not None:
				con.close()
	else:
		return render_template("signup.html")

if __name__=="__main__":
	app.run(debug=True,use_reloader=True)