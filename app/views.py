"""
api.py

This module will contain the routes to our app interface.
"""
from flask import Blueprint


webapp = Blueprint("api", __name__)


@webapp.route("/")
def index():
    """ Home page """
    return "Hello World! This is our app front page"
