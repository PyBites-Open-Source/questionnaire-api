import unittest

from dotenv import load_dotenv
from flask import json

from app import create_app, db
from app.models.category import Category


@unittest.skip("Waiting to be implemented.")
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
        self.category_data()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def category_data(self):
        """ Setup category data. """
        category1 = Category("Test Category 1").create()
        category2 = Category("Test Category 2").create()

    def test_add_new_category(self):
        """ Test add new category route. """
        response = self.client.post(
            "/api/categories", data=self.category, content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual("New object created.", data["message"])

    def test_get_a_specific_category(self):
        """ Test get a specific category. """
        response = self.client.get("/api/categories/1", content_type="application/json")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual("Test Category 1", data["name"])

    def test_get_all_categories(self):
        """ Test get all categories. """
        response = self.client.get("/api/categories", content_type="application/json")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(2, len(data))

    def test_update_a_category(self):
        """ Test update a category. """
        updated_category = {"name": "Update Category"}
        response = self.client.put(
            "/api/categories/1", data=updated_category, content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual("Update Category", data["name"])

    def test_delete_a_specific_category(self):
        """ Delete a specific category """
        response = self.client.delete(
            "/api/categories/1", content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual("Object deleted.", data["message"])
        # Try to get again the same category
        response = self.client.get("/api/categories/1", content_type="application/json")
        self.assertEqual(response.status_code, 404)