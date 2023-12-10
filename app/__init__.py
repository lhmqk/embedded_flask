from flask import Flask, redirect, url_for
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Define the route for '/'
@app.route('/')
def index():
    return redirect(url_for('auth.login'))

from app.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/login')

from app.dashboard.views import dashboard_blueprint
app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

def create_app():
    return app
