from flask import Flask
from flask_mongoengine import MongoEngine
from flask_user import login_required, UserManager, UserMixin
from pprint import pprint



app = Flask(__name__)
app.config.from_pyfile('ip/default_settings.py')
#this line is to be commented:
app.config.from_pyfile('local_settings.py')
db = MongoEngine(app)



if __name__ == '__main__':
  pprint(app.config)
  app.run(
    host = app.config['SERVER_IP'],
    port = app.config['SERVER_PORT'],
    debug = app.config['DEBUG'])
