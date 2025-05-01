from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__, static_folder='/static',template_folder='../templates')

@main_bp.route("/", methods=["GET"])
def return_login():
    return render_template("login.html")

@main_bp.route("/", methods=["GET"])
def enviar_dados():
    return render_template("login.html")