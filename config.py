import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    SESSION_TYPE = 'redis'
    SESSION_REDIS = 'redis://localhost:6379'
    SESSION_PERMANENT = False
