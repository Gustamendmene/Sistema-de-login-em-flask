from flask import session
from flask import Flask
from flask import render_template,redirect
from flask import request
from flask import flash
import os;
from database import get_data
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
if not app.secret_key:
    raise RuntimeError("SECRET_KEY environment variable is missing")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        data = get_data()
        usuario = request.form.get("username")
        senha = request.form.get("password")
 
        if usuario in data and data[usuario]["senha"]==senha:
            session["user"]=usuario
            flash("Login realizado com sucesso","success")
            return redirect("/")
        else:
            flash("Usuário ou senha inválidos","error")
            return render_template("login.html")

@app.route("/")
def main():
    if(session.get("user") is None):
        return redirect("login")
    else:
        return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
