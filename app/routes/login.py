from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def return_login():
    return render_template('login.html')