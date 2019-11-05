# code: utf-8

from flask import Blueprint

from app import db
from app.api.models.answer import Answer
from app.api.models.category import Category
from app.api.models.question import Question

bp_manage = Blueprint("manage", __name__)


@bp_manage.cli.command("db_create")
def db_create():
    """ Create database and tables. """
    db.create_all()
    print("Database created.")


@bp_manage.cli.command("db_delete")
def db_delete():
    """ Delete database and all tables. """
    db.drop_all()
    print("Database deleted.")


@bp_manage.cli.command("seed")
def seed():
    """ Populate tables with data. """
    category = Category("Category 1").create()
    print(f"Create: {category}")

    question1 = Question("Question 1", 1, "Hard", False).create()
    print(f"Create: {question1}")
    question2 = Question("Question 2", 1, "Easy", True).create()
    print(f"Create: {question2}")
    question3 = Question("Question 3", 1, "Medium", True).create()
    print(f"Create: {question3}")

    answer1 = Answer("Answer 1", 1, False).create()
    print(f"Create: {answer1}")
    answer2 = Answer("Answer 2", 1, True).create()
    print(f"Create: {answer2}")
    answer3 = Answer("Answer 3", 1, False).create()
    print(f"Create: {answer3}")
    answer4 = Answer("Answer 4", 2, True).create()
    print(f"Create: {answer4}")
    answer5 = Answer("Answer 5", 2, False).create()
    print(f"Create: {answer5}")
    answer6 = Answer("Answer 6", 2, False).create()
    print(f"Create: {answer6}")
    answer7 = Answer("Answer 7", 3, False).create()
    print(f"Create: {answer7}")
    answer8 = Answer("Answer 8", 3, True).create()
    print(f"Create: {answer8}")
    answer9 = Answer("Answer 9", 3, False).create()
    print(f"Create: {answer9}")
