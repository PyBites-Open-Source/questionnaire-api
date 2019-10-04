from app import db


class Category(db.Model):
    """
    Category Model

    Represents the category table.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Category> {self.name}"


class Question(db.Model):
    """
    Question Model

    Represents the question table.
    """

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

    def to_dict(self):
        """ Return question details as dict. """
        data = {
            "id": self.id,
            "question": self.question,
            "category": self.category,
            "level": self.level,
            "_links": {},
        }
        return data


class Answer(db.Model):
    """
    Answer Model

    Represents answer table.
    """

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(80), nullable=False)
    questionid = db.Column(db.Integer, db.ForeignKey("question.id"), nullable=False)
    correct_answer = db.Column(db.Boolean, nullable=False)

    # Relationship one-to-many
    question = db.relationship(
        "Question", backref=db.backref("answers", lazy="dynamic")
    )

    def __init__(self, answer, questionid, correct_answer):
        self.answer = answer
        self.questionid = questionid
        self.correct_answer = correct_answer

    def __repr__(self):
        return f"<Answer> {self.answer}"


class UserAnswer(db.Model):
    """
    User Answer Model

    Represents the user_answer table.
    """

    id = db.Column(db.Integer, primary_key=True)
    questionid = db.Column(db.Integer, db.ForeignKey("question.id"))
    answerid = db.Column(db.Integer, db.ForeignKey("answer.id"))

    def __init__(self, questionid, answerid):
        self.questionid = questionid
        self.answerid = answerid
