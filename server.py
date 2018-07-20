""" server for personal website """
from flask import Flask
from flask import request, render_template, redirect, flash, session, jsonify

app = __Flask__(name)

@app.route("/", methods=[GET])
def home_page():


    return render_template("home.html")

@app.route("/experience", methods=[GET])
def home_page():

    return render_template("experience.html")


@app.route("/photography", methods=[GET])
def photography():

    return render_template("photography.html")


@app.route("/contact", methods=[GET])
def contact_me():

    return render_template("contact.html")


@app.route("/myjourney", methods=[GET])
def my_journey():

    return render_template("my_journey.html")
