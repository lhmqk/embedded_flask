from flask import Blueprint, render_template, request, redirect, url_for, session
import paho.mqtt.client as mqtt
import random

# MQTT Configuration
broker = 'v4e74e78.ala.us-east-1.emqxsl.com'
port = 8883
topic = "/testtopic/1"
username = 'lhmqk'
password = 'Khai16082002'
ca_path = '/home/lhmqk/Documents/Obisidian/BK-213/Thesis/flask_test/emqxsl-ca.crt'
client_id = f'publish-{random.randint(0, 1000)}'

# Flask Blueprint for the dashboard
dashboard_blueprint = Blueprint('dashboard', __name__)

# MQTT Client Setup
client = mqtt.Client(client_id)
client.username_pw_set(username, password)
client.tls_set(ca_certs=ca_path)

# Global variable to store messages
messages = []

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(topic)

def on_message(client, userdata, msg):
    messages.append(msg.payload.decode())

# Set the callbacks and start the MQTT loop
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)
client.loop_start()

# Dashboard route
@dashboard_blueprint.route('/', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        message = request.form['message']
        client.publish(topic, message)
        # Store the message in the session to display after redirect
        session['last_message'] = message
        # Redirect to the same page but with a GET request
        return redirect(url_for('dashboard.dashboard'))
    # Retrieve the last message from the session if available
    last_message = session.pop('last_message', None)
    return render_template('dashboard.html', messages=messages, last_message=last_message)
