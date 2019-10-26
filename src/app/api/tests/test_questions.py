import unittest

from dotenv import load_dotenv
from flask import json

from app import create_app, db
from app.api.models.answer import Answer
from app.api.models.category import Category
from app.api.models.question import Question


class TestQuestions(unittest.TestCase):
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
        self.questions_data()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def questions_data(self):
        """ Setup question data. """
        category = Category("Test Category").create()
        question1 = Question("Test Question 1", category.id, "Hard", False).create()
        question2 = Question("Test Question 2", category.id, "Hard", False).create()

    def question(self):
        """ Help method with question data. """
        data = {
            "question": "Test question",
            "category_id": 1,
            "level": "Easy",
            "true_false_question": False,
        }
        return data

    def test_add_new_question(self):
        """ Test add new question route. """
        response = self.client.post(
            "/api/v1/questions",
            data=json.dumps(self.question()),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual("Test question", data["question"]["question"])

    def test_get_a_question(self):
        """ Test get a question. """
        response = self.client.get(
            "/api/v1/questions/1", content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual("Test Question 1", data["question"]["question"])

    def test_get_all_questions(self):
        """ Test get all questions. """
        response = self.client.get("/api/v1/questions", content_type="application/json")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(2, len(data["questions"]))

    def test_update_a_question(self):
        """ Test update a question. """
        question = self.question()
        question["question"] = "Updated question"
        response = self.client.put(
            "/api/v1/questions/1",
            data=json.dumps(question),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual("Updated question", data["question"]["question"])

    def delete_a_question(self):
        """ Test delete a question. """
        response = self.client.delete(
            "/api/v1/questions/1", content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual("Object deleted", data["message"])
        # Trying again to access the same question
        response = self.client.get("/api/questions/1", content_type="application/json")
        self.assertEqual(response.status_code, 404)
