from app import db


class OpenTrivia(db.Model):
    """
    class representes trivia table

    todo: add fields to the table.
    - fields which could be added   
        * id   
        * question 
        * answers
        * question type : (T/F ,  MCQ)   
        * category : (Tech, Science etc.)  
        * difficulty  
        * date created
        * date modified
    """

    __tablename__ = "opentrivia"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String())
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )
