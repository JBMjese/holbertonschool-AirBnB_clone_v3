#!/usr/bin/python3
"""
define a route in the API that can be accessed via the /status URL
and that returns a JSON indicating that the API status is "OK".
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status', methods=['GET'])
def status():
    data = {"status": "OK"}
    return (jsonify(data))

@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Retrieve the number of each object type"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
    }
    return jsonify(stats)
