import unittest

from dotenv import load_dotenv

from app import create_app

load_dotenv()


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
