from flask import Flask
from flask_session import Session
import redis

app = Flask(__name__)
app.config.from_object('config.Config')

# Configure Redis session storage
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.StrictRedis(host='localhost', port=6379)

Session(app)

from app import routes
