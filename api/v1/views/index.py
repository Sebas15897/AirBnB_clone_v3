#!/usr/bin/python3
""" Status of our Api and some stats """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def app_status():
    """ Returns the api status """
    return(jsonify(status="OK"))


@app_views.route("/stats")
def stats():
    """ Returns the number of each objects by type """
    result = {"amenities": storage.count("Amenity"),
              "cities": storage.count("City"),
              "places": storage.count("Place"),
              "reviews": storage.count("Review"),
              "states": storage.count("State"),
              "users": storage.count("User")}
    return jsonify(result)
