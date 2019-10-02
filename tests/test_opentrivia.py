import unittest

from app import create_app, db

from dotenv import load_dotenv

load_dotenv()


class TestModels(unittest.TestCase):
    def setUp(self):
        # create a test client
        self.app = create_app("development")
        # propagate the exceptions to the test client
        self.app.testing = True
        # testing client
        self.client = self.app.test_client

        with self.app.app_context():
            # create all tables
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_a_question(self):
        pass

    def test_create_an_answer(self):
        pass

    def test_delete_question(self):
        pass

class TestWebapp(unittest.TestCase):

    def test_home_page(self):
        pass

    def test_developer_page(self):
        pass

class TestApiEndpoints(unittest.TestCase):

    API_URL = "http://localhost/api/v1/"

    def setUp(self):
        # create a test client
        self.app = create_app("development")
        # propagate the exceptions to the test client
        self.app.testing = True
        # testing client
        self.client = self.app.test_client

        with self.app.app_context():
            # create all tables
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_api_create_question(self):
        pass

    def test_api_get_question(self):
        pass

    def test_api_get_all_questions(self):
        pass

    def test_api_add_answer_to_question(self):
        pass

    def test_api_get_all_answers_of_question(self):
        pass

    def test_api_get_delete_question(self):
        pass
