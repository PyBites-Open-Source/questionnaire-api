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
        self.client = self.app.test_client()

        with self.app.app_context():
            # create all tables
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


class TestWebapp(unittest.TestCase):
    def setUp(self):
        # create a test client
        self.app = create_app("development")
        # propagate the exceptions to the test client
        self.app.testing = True
        # testing client
        self.client = self.app.test_client()

    def test_home_page(self):
        """ Test home page """
        response = self.client.get("/")
        self.assertEqual(response.status, "200 OK")
        html = response.get_data(as_text=True)
        self.assertIn("<title>Home Page</title>", html)

    def test_developer_page(self):
        """ Test developer page """
        response = self.client.get("/developer")
        self.assertEqual(response.status, "200 OK")
        html = response.get_data(as_text=True)
        self.assertIn("<title>Developer Page</title>", html)


class TestApiEndpoints(unittest.TestCase):

    API_URL = "http://localhost/api/v1/"

    def setUp(self):
        # create a test client
        self.app = create_app("development")
        # propagate the exceptions to the test client
        self.app.testing = True
        # testing client
        self.client = self.app.test_client()

        with self.app.app_context():
            # create all tables
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
