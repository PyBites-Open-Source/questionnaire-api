from app import db


class Answer(db.Model):
    """
    Answer Model

    Represents answer table.
    """

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(80), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"), nullable=False)
    correct_answer = db.Column(db.Boolean, nullable=False)

    # Relationship one-to-many
    question = db.relationship(
        "Question", backref=db.backref("answers", lazy="dynamic")
    )

    def __init__(self, answer, question_id, correct_answer):
        self.answer = answer
        self.question_id = question_id
        self.correct_answer = correct_answer

    def __repr__(self):
        return f"<Answer> {self.answer}"

    def create(self):
        """ Save object to database. """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """ Delete object from database. """
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """ Return answer details as dict. """
        data = {
            "answer": self.answer,
            "question_id": self.question_id,
            "correct_answer": self.correct_answer,
        }
