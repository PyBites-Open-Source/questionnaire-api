"""
api.py

This module will contain the api endpoints.
"""
from flask import Blueprint


api_endpoints = Blueprint("api", __name__)


@api_endpoints.route("/api")
def index():
    """ Home API page """
    return "Hello World!"
