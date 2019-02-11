from flask import Flask, render_template, request
from random import randint
from functions import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/business", methods=["GET", "POST"])
def business():
    if request.method == "GET":
        return render_template("business.html")
    elif request.method == "POST":
        form_data = request.form
        businesschoice = form_data["businesschoice"]
        if businesschoice == "type":
            results = sort_business_type()
            length = len(results)
        elif businesschoice == "name":
            results = sort_business_name()
            length = len(results)
        return render_template("business.html", **locals())

        
@app.route("/residential")
def residential():
    surname_results = display_residential()
    return render_template("residential.html", surname_results=surname_results)


@app.route("/confirmation", methods=["POST"])
def confirmation():
    form_data = request.form
    email = form_data["email"]
    result="All OK"
    return render_template("confirmation.html", title="Form confirmation", **locals())


if __name__ == "__main__":
    app.run(debug=True)
