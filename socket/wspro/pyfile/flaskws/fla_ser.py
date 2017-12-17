import time
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return 'index!!'


@socketio.on('connect', namespace='/test')
def test_connect():
    print 1
    emit('my response', {'data': 'Connected99', 'count': 0})


@socketio.on('my event', namespace='/test')
def test_message(message):
    print 2
    print message
    emit('my response', {'data': message['data'], 'count': 2})

if __name__ == '__main__':
    socketio.run(app,debug=True,host='0.0.0.0')