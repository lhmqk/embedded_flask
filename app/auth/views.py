from flask import Blueprint, render_template, request, redirect, url_for

auth_blueprint = Blueprint('auth', __name__)

# Hardcoded user credentials
users = {'user1': 'password1', 'user2': 'password2'}

@auth_blueprint.route('/')
def login():
    return render_template('login.html')

@auth_blueprint.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    if users.get(username) == password:
        return redirect(url_for('dashboard.dashboard'))
    return 'Invalid credentials', 401
