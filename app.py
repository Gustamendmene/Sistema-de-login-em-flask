from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

 
username = "Aladat"
password = "1234"
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
    
        return redirect(url_for("login"))
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)