from flask import Blueprint
from flask import render_template

acceso = Blueprint("acceso",__name__)

@acceso.route("/")
def index():
    return render_template("acceso/index.html")

