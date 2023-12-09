from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

from app.dashboard.views import dashboard_blueprint
app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

def create_app():
    return app
