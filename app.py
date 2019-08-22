from flask import Flask

import sys
from os import listdir
sys.path.insert(0,"/imagens")

from flask import render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template('chat2.html', imgs=[f.split('.')[0] for f in listdir('./static/img')])

@socketio.on('message')
def messagerecived(data):
    print (data) 
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app,'127.0.0.1', 3000)
