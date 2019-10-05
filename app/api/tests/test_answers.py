import unittest

from dotenv import load_dotenv

from app import create_app, db


class TestAnswers(unittest.TestCase):
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

    def answer(self):
        """ Help method with answer data. """
        data = {"answer": "Test Answer", "question_id": "1", "correct_answer": "false",}
        return data

    def test_add_new_answer(self):
        """ Tedd add new answer. """
        response = self.client.post("/api/answers", data=self.answer())
        self.assertEqual(response.status_code, 201)
        self.assertEqual("Test Answer", str(response.data))

    def test_get_a_specific_answer(self):
        """ Test get a specific answer. """
        pass

    def test_get_all_answers(self):
        """ Test get all answers. """
        pass

    def test_update_an_answer(self):
        """ Test update an answer. """
        pass

    def test_delete_an_answer(self):
        """ Test delete an answer. """
        pass
