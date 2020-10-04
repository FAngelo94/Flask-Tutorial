from flask_worker import Manager

from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from rq import Queue
import eventlet
import os

db = SQLAlchemy()
eventlet.monkey_patch(socket=True)
socketio = SocketIO(asynch_mode='eventlet')
# initialize a Manager with the database and socketio

def create_app():
    app = Flask(__name__)
    app.redis = Redis.from_url('redis://')
    app.task_queue = Queue('my-task-queue', connection=app.redis)

    db.init_app(app)
    socketio.init_app(app, message_queue='redis://')
    # initialize the manager with the application
    return app