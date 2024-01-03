from flask import Blueprint, render_template, request, redirect, url_for, session
from .. import socketio
import paho.mqtt.client as mqtt
import random
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, MQTT_USERNAME, MQTT_PASSWORD, MQTT_CA_PATH

# Flask Blueprint for the dashboard
dashboard_blueprint = Blueprint('dashboard', __name__)

# Global variable to store messages
messages = []

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    messages.append(message)
    socketio.emit('mqtt_message', {'message': message})

# MQTT Setup
client_id = f'publish-{random.randint(0, 1000)}'
client = mqtt.Client(client_id)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.tls_set(ca_certs=MQTT_CA_PATH)
client.connect(MQTT_BROKER, MQTT_PORT)
client.loop_start()

# Dashboard route
@dashboard_blueprint.route('/', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        message = request.form['message']
        client.publish(MQTT_TOPIC, message)
        # Redirect to the same page but with a GET request
        return redirect(url_for('dashboard.dashboard'))
    # Retrieve the last message from the session if available
    last_message = session.pop('last_message', None)
    return render_template('dashboard.html', messages=messages, last_message=last_message)
