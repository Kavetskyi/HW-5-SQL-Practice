from app import app
from flask import render_template


@app.route("/")
def hello_world():
    a = "Good evening, we are from Ukraine!"
    return render_template("index.html", variable=a)


@app.route("/add/<var1>/<var2>")
def adding(var1, var2):
    return var1 + ' + ' + var2 + " = " + str(int(var1) + int(var2))
