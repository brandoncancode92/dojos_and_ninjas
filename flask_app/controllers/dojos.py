from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


# Redirect route to Home Page
@app.route('/')
def index():
    return redirect("/dojos")

# Home Page
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", dojo=dojos)

# Creating a new Dojo on the Home Page
@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

