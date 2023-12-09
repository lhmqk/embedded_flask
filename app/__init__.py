from flask import Flask
from .auth.views import auth_blueprint
from .dashboard.views import dashboard_blueprint

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')
    return app
