import unittest

from dotenv import load_dotenv
from flask import json

from app import create_app, db
from app.api.models.answer import Answer
from app.api.models.category import Category
from app.api.models.question import Question


class TestAnswers(unittest.TestCase):
    """
    Test Questions Routes.
    """

    def setUp(self):
        self.app = create_app("testing")
        self.app.testing = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            db.session.commit()
        self.app.app_context().push()
        self.answer_data()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def answer_data(self):
        """ Setup answer data. """
        category = Category("Test Category").create()
        question = Question("Test Question", category.id, "Easy", False).create()
        answer1 = Answer("Test Answer 1", question.id, False).create()
        answer2 = Answer("Test Answer 2", question.id, True).create()

    def answer(self):
        """ Help method with answer data. """
        data = {"answer": "Test Answer", "question_id": 1, "correct_answer": False}
        return data

    def test_add_new_answer(self):
        """ Tedd add new answer. """
        response = self.client.post(
            "/api/v1/answers",
            data=json.dumps(self.answer()),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual("Test Answer", data["answer"]["answer"])

    def test_get_a_specific_answer(self):
        """ Test get a specific answer. """
        response = self.client.get("/api/v1/answers/1", content_type="application/json")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual("Test Answer 1", data["answer"]["answer"])

    def test_update_an_answer(self):
        """ Test update an answer. """
        answer = self.answer()
        answer["answer"] = "Updated Answer"
        response = self.client.put(
            "/api/v1/answers/1",
            data=json.dumps(answer),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual("Updated Answer", data["answer"]["answer"])

    def test_delete_an_answer(self):
        """ Test delete an answer. """
        response = self.client.delete(
            "/api/v1/answers/1", content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual("Object deleted", data["message"])
        # Try again to access the same object
        response = self.client.get("/api/v1/answers/1", content_type="application/json")
        self.assertEqual(response.status_code, 404)
