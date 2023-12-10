var socket = io.connect('http://' + document.domain + ':' + location.port);

// Listen for MQTT messages from the server
socket.on('mqtt_message', function(data) {
    var li = document.createElement('li');
    li.appendChild(document.createTextNode(data.message));
    document.getElementById('messages').appendChild(li);
});