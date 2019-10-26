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


def questions_validation(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.is_json:
            data = request.get_json()
            message = {"error": "Invalid data"}
            if type(data["question"]) != str:
                message["error"] = "question must be a string"
                return make_response(jsonify(message), 400)
            if type(data["category_id"]) != int:
                message["error"] = "category_id must be int"
                return make_response(jsonify(message), 400)
            if data["level"] not in ["Easy", "Medium", "Hard"]:
                message["error"] = "level must be Easy, Medium, Hard"
                return make_response(jsonify(message), 400)
            if type(data["true_false_question"]) != bool:
                message["error"] = "true_false_question must be bool"
                return make_response(jsonify(message), 400)
        return f(*args, **kwargs)

    return decorated_function


def answers_validation(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.is_json:
            data = request.get_json()
            message = {"error": "Invalid data"}
            if type(data["answer"]) != str:
                message["error"] = "answer must be a string"
                return make_response(jsonify(message), 400)
            if type(data["question_id"]) != int:
                message["error"] = "question_id must be int"
                return make_response(jsonify(message), 400)
            if type(data["correct_answer"]) != bool:
                message["error"] = "correct_answer must be int"
                return make_response(jsonify(message), 400)
        return f(*args, **kwargs)

    return decorated_function
