import unittest

from dotenv import load_dotenv

from app import create_app, db
from app.models import Category


class TestCategories(unittest.TestCase):
    """
    Test Categories Routes.
    """

    def setUp(self):
        self.app = create_app("development")
        self.app.testing = True
        self.client = self.app.test_client()
        self.category = {"name": "Test Category"}

        with self.app.app_context():
            db.create_all()
            db.session.commit()
        self.app.app_context().push()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_new_category(self):
        """ Test add new category route. """
        response = self.client.post("/api/categories", data=self.category)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Test Category", str(response.data))

    def test_get_a_specific_category(self):
        """ Test get a specific category. """

    def test_get_all_categories(self):
        """ Test get all categories. """
        pass

    def test_update_a_category(self):
        """ Test update a category. """
        pass

    def test_delete_a_specific_category(self):
        """ Delete a specific category """
        pass
