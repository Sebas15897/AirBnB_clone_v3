#!/usr/bin/python3
""" Create API  with Flask """
from flask import Flask, jsonify
from models import storage
from models.engine import *
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

""" Instance of Flask """
app = Flask(__name__)

""" Register the blueprint app_views """
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_storage(error):
    """ Close the db """
    storage.close()


if __name__ == "__main__":
    """ Main Function """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True, debug=True)
