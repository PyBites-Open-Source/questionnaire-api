# code: utf-8

from functools import wraps

from flask import jsonify, make_response, request


def categories_validation(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.is_json:
            data = request.get_json()
            if type(data["name"]) != str:
                message = {"error": "Name is not a string"}
                return make_response(jsonify(message), 400)
        return f(*args, **kwargs)

    return decorated_function
