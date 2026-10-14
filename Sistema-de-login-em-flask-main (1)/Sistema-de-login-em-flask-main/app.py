from functools import wraps
from flask import session
from flask import Flask
from flask import render_template,redirect,url_for
from flask import request
from flask import flash
import os;
from database import get_data

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

if not app.secret_key:
    raise RuntimeError("SECRET_KEY environment variable is missing")

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        usuario = session.get("user")
        if not usuario:
            flash("Você precisa fazer o login pra acessar esta pagina","error")
            return redirect(url_for("login"))
        return func(*args,**kwargs)
    return wrapper

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        data = get_data()
        usuario = request.form.get("username")
        senha = request.form.get("password")
 
        if usuario in data and data[usuario]["senha"]==senha:
            session.clear()
            session["user"]=usuario
            flash("Login realizado com sucesso","success")
            return redirect("/")
        else:
            flash("Usuário ou senha inválidos","error")
            return render_template("login.html")

@app.get("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/login")

@app.route("/", methods=["GET"])
@login_required
def main():
    usuario = session.get("user")
    
    data = get_data()
    aluno = data.get(usuario)

    nome = aluno.get("nome", usuario)
    turma = aluno.get("turma", aluno["nome"])
    notas = aluno.get("notas", aluno["notas"]) 
    return render_template(
        "Paginadashboard.html",
        nome=nome,
        turma=turma,
        notas=notas,
    )

if __name__ == '__main__':
    app.run(debug=True)
