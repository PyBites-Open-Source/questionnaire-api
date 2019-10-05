import unittest

from dotenv import load_dotenv

from app import create_app, db
from app.models.category import Category


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
        category = Category("Test Category")
        category.create()
        response = self.client.get("/api/categories/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Category", str(response.data))

    def test_get_all_categories(self):
        """ Test get all categories. """
        category1 = Category("Category 1")
        category2 = Category("Category 2")
        category1.create()
        category2.create()
        response = self.client.get("/api/categories")
        self.assertEqual(response.status_code, 200)

    def test_update_a_category(self):
        """ Test update a category. """
        category = Category("Category Test")
        category.create()
        updated_category = {"name": "Update Category"}
        response = self.client.put("/api/categories/1", data=updated_category)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Update Category", str(response.data))

    def test_delete_a_specific_category(self):
        """ Delete a specific category """
        category = Category("Test Category")
        category.create()
        response = self.client.delete("/api/categories/1")
        self.assertEqual(response.status_code, 200)
        # Try to get again the same category
        response = self.client.get("/api/categories/1")
        self.assertEqual(response.status_code, 404)
