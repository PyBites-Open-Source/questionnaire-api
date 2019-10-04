import unittest

from dotenv import load_dotenv

from app import create_app, db
from app.models import Answer, Category, Question

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
            db.session.commit()
        self.app.app_context().push()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def create_new_category(self, name):
        """ Helo method to create new category. """
        category = Category(name)
        db.session.add(category)
        db.session.commit()
        return category

    def create_new_question(self, question, category_id, level):
        """ Help method to create new question. """
        question = Question(question, category_id, level)
        db.session.add(question)
        db.session.commit()
        return question

    def create_new_answer(self, answer, question_id, correct_answer):
        """ Help method to create new answer. """
        answer = Answer(answer, question_id, correct_answer)
        db.session.add(answer)
        db.session.commit()
        return answer

    def test_new_category_creation(self):
        """ Test add new category. """
        new_category = self.create_new_category("Test Category")
        created_category = Category.query.filter_by(name="Test Category").first()
        self.assertEqual(new_category.name, created_category.name)

    def test_new_question_creation(self):
        """ Test add new question. """
        category = self.create_new_category("Test Category")
        new_question = self.create_new_question("Test Question", category.id, "Level 1")
        created_question = Question.query.filter_by(question="Test Question").first()
        self.assertEqual(new_question.question, created_question.question)

    def test_new_answer_creation(self):
        """ Test add new answer. """
        category = self.create_new_category("Test Category")
        question = self.create_new_question("Test Question", category.id, "Level 1")
        new_answer = self.create_new_answer("Test Answer", question.id, False)
        created_answer = Answer.query.filter_by(answer="Test Answer").first()
        self.assertEqual(created_answer.answer, new_answer.answer)

    def test_create_a_category_with_four_questions(self):
        """ Test create and query category with four questions. """
        category = self.create_new_category("Test Category")
        question1 = self.create_new_question("Test Question1", category.id, "Level 1")
        question2 = self.create_new_question("Test Question2", category.id, "Level 2")
        question3 = self.create_new_question("Test Question3", category.id, "Level 3")
        # Get all the questions
        questions = category.questions.all()
        self.assertEqual(3, len(questions))

    def test_create_multiple_answers_for_a_question(self):
        """ Test multiple answers added to a question. """
        category = self.create_new_category("Test Category")
        question = self.create_new_question("Test Question", category.id, "Level 1")
        answer1 = self.create_new_answer("Test Answer1", question.id, False)
        answer2 = self.create_new_answer("Test Answer2", question.id, False)
        answer3 = self.create_new_answer("Test Answer3", question.id, True)
        answers = question.answers.all()
        self.assertEqual(3, len(answers))
        self.assertTrue(answers[2].correct_answer)


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
            db.session.commit()
        self.app.app_context().push()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
