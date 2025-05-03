from flask import Blueprint, render_template

main_bp = Blueprint('login', __name__, template_folder='../templates')




@main_bp.route("/", methods=["GET"])
def return_login():
    return render_template("login.html")


