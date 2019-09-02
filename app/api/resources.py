"""
endpoints.py

This module will hold the Resources.
"""
from flask_restful import Resource


# TODO - Implement methods
class Question(Resource):
    def get(self, question_id):
        return "Hello World!"

    def put(self, question_id):
        pass

    def delete(self, question_id):
        pass
