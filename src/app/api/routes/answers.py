from flask import Blueprint, make_response, request, jsonify, abort
from app.api.models.answer import Answer
from app.api.models.question import Question
from app.api.decorators import answers_validation

# Define answer Blueprint
answer_bp = Blueprint("answer_api", __name__)


@answer_bp.route("/answers/<int:id>", methods=["GET"])
def get_answer(id):
    """ Get answer. """
    answer = Answer.query.get(id)
    if answer is not None:
        response = {"answer": answer.to_dict()}
        return make_response(jsonify(response), 200)
    abort(404)


@answer_bp.route("/answers", methods=["POST"])
@answers_validation
def create_answer():
    """ Create new answer. """
    if request.is_json:
        data = request.get_json()
        question = Question.query.get(data["question_id"])
        if question:
            new_answer = Answer(data["answer"], question.id, data["correct_answer"])
            answer = new_answer.create()
            response = {"answer": answer.to_dict()}
            return make_response(jsonify(response), 201)
    abort(404)


@answer_bp.route("/answers/<int:id>", methods=["PUT"])
@answers_validation
def update_answer(id):
    """ Update answer. """
    answer = Answer.query.get(id)
    if request.is_json and answer is not None:
        data = request.get_json()
        answer.answer = data["answer"]
        answer.question_id = data["question_id"]
        answer.correct_answer = data["correct_answer"]
        answer.save()
        response = {"answer": answer.to_dict()}
        return make_response(jsonify(response), 201)
    print("No Update Answer")
    abort(404)


@answer_bp.route("/answers/<int:id>", methods=["DELETE"])
def delete_answer(id):
    """ Delete answer. """
    answer = Answer.query.get(id)
    if answer is not None:
        answer.delete()
        response = {"message": "Object deleted"}
        return make_response(jsonify(response), 200)
    abort(404)


@answer_bp.errorhandler(404)
def not_found(error):
    """ Return message for not found. """
    return make_response(jsonify({"error": "Not found"}), 404)
