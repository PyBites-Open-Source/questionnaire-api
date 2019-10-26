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

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def save(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """ Returns category details as dict. """
        data = {"name": self.name}
        return data
