from flask import Blueprint, render_template, request, redirect, url_for, session, app
from datetime import timedelta

auth_blueprint = Blueprint('auth', __name__)

# Hardcoded user credentials
users = {'user1': 'password1', 'user2': 'password2'}

@auth_blueprint.route('/')
def login():
    # Check if user is logged in
    if 'logged_in' in session:
        # Redirect to dashboard if already logged in
        return redirect(url_for('dashboard.dashboard'))
    # Show login page if not logged in
    return render_template('login.html')

@auth_blueprint.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    keep_login = request.form.get('keep_login')
    # Validate credentials
    if users.get(username) == password:
        # Set the session as "logged_in"
        session['logged_in'] = True
        # Set the session to not be permanent if the checkbox is not checked
        session.permanent = 'remember' in request.form
        if session.permanent:
            # Set the duration of the session to be permanent (e.g., 30 days)
            app.permanent_session_lifetime = timedelta(days=30)
        # Redirect to dashboard after successful login
        return redirect(url_for('dashboard.dashboard'))
    # Handle invalid credentials
    return 'Invalid credentials', 401
