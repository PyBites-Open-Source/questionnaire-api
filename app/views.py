"""
api.py

This module will contain the routes to our app interface.
"""
from flask import Blueprint
from flask import render_template

from app.models import Question

webapp = Blueprint("api", __name__)


@webapp.route("/")
def index():
    """ Home page """
    return render_template("home.html")


@webapp.route("/developer")
def developer():
    """ Developer page """
    return render_template("developer.html")
