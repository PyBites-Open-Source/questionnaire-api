from app import db
from app.models.answer import Answer
from app.models.category import Category


class Question(db.Model):
    """
    Question Model

    Represents the question table.
    """

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(120), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    level = db.Column(db.String(30), nullable=False)
    true_false_question = db.Column(db.Boolean)

    # Relationship one-to-many
    category = db.relationship(
        "Category", backref=db.backref("questions", lazy="dynamic")
    )

    def __init__(self, question, category_id, level, true_false_question):
        self.question = question
        self.category_id = category_id
        self.level = level
        self.true_false_question = true_false_question

    def __repr__(self):
        return f"<Question> {self.question}"

    def create(self):
        """ Save object to database. """
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        """ Delete the object from database. """
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """ Return question details as dict. """
        data = {
            "id": self.id,
            "question": self.question,
            "category_id": self.category_id,
            "level": self.level,
            "_links": {},
        }
        return dat
