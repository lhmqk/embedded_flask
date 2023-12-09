from .. import socketio

# Event handler for new MQTT messages
@socketio.on('mqtt_message')
def handle_mqtt_message(data):
    socketio.emit('mqtt_message', data)
