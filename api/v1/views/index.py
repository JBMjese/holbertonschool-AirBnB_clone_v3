#!/usr/bin/python3
"""
define a route in the API that can be accessed via the /status URL
and that returns a JSON indicating that the API status is "OK".
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

@app_views.route('/status', methods=['GET'])
def status():
    data = {"status": "OK"}
    return (jsonify(data))

@app_views.route('/stats')
def clases_count():
    '''endpoint that retrieves the number of each objects by type'''
    new_dict = {}
    new_dict["amenities"] = storage.count("Amenity")
    new_dict["cities"] = storage.count("City")
    new_dict["places"] = storage.count("Place")
    new_dict["reviews"] = storage.count("Review")
    new_dict["states"] = storage.count("State")
    new_dict["users"] = storage.count("User")
    return jsonify(new_dict)
