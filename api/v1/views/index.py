#!/usr/bin/python3
import os
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Returns the number of each object by type"""
    classes = {"Amenity": Amenity, "City": City,
               "Place": Place, "Review": Review, "State": State, "User": User}
    stats = {}
    for cls in classes:
        stats[cls] = storage.count(classes[cls])
    return jsonify(stats)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request."""
    storage.close()
