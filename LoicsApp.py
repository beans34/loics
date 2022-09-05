from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "Reece"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods = ["POST","GET"])
def login():
   if request.method == "POST":
       user = request.form["Username"]
       session["user"] = user
       return redirect(url_for("user",usr = user))
   else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template('login.html')


@app.route("/user")
def user():
    if "user" in session:
        currentUser = session["user"]
        return render_template("user.html" ,  log_user= currentUser )
    else:
        return redirect(url_for("login"))



@app.route("/logout")
def logout():
    session.pop("user", None)
    return render_template("logout.html")

 
if __name__ == "__main__":
    app.run(debug = True)



