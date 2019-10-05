import unittest

from dotenv import load_dotenv

from app import create_app, db


class TestQuestions(unittest.TestCase):
    """
    Test Questions Routes.
    """

    def setUp(self):
        self.app = create_app("development")
        self.app.testing = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            db.session.commit()
        self.app.app_context().push()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    
    def question(self):
        """ Help method with question data. """
        data = {
            "question": "Test question",
            "category_id": "1",
            "level": "Difficult",
            "true_false_question": "false"
        }
        return data

    def test_add_new_question(self):
        """ Test add new question route. """
        response = self.client.post("api/questions" data=self.question())
        self.assertEqual(response.status_code, 201)
        self.assertIn("Test question", str(response.data))


    def test_get_a_question(self):
        """ Test get a question. """
        pass

    def test_get_all_questions(self):
        """ Test get all questions. """
        pass

    def test_update_a_question(self):
        """ Test update a question. """
        pass

    def delete_a_question(self):
        """ Test delete a question. """
        pass
