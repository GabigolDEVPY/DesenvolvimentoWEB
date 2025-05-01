from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from routes.login import main_bp
    app.register_blueprint(main_bp)