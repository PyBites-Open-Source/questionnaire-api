from app import db


class Question(db.Model):
    """
    Question Model

    Represents the question table.
    """

    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(120), nullable=False)
    categoryid = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    level = db.Column(db.String(30), nullable=False)
    true_false_question = db.Column(db.Boolean)

    # Relationship one-to-many
    category = db.relationship(
        "Category", backref=db.backref("questions", lazy="dynamic")
    )

    def __init__(self, question, categoryid, level):
        self.question = question
        self.categoryid = categoryid
        self.level = level

    def __repr__(self):
        return f"<Question> {self.question}"

    def create(self):
        """ Save object to database. """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """ Delete the object from database. """
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """ Return question details as dict. """
        data = {
            "id": self.id,
            "question": self.question,
            "category": self.category,
            "level": self.level,
            "_links": {},
        }
        return dat
