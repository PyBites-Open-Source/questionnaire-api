from app import db

class OpenTrivia(db.Model):
    """
    class representes trivia table

    todo: add fields to the table.
    - fields which could be added   
        * id   
        * question 
        * question type : (T/F ,  MCQ)   
        * category : (Tech, Science etc.)  
        * difficulty  
        * date created
        * date modified
    """

    __tablename__ = "opentrivia"