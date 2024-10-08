from flask_sqlalchemy import (
    SQLAlchemy,
)  # Import SQLAlchemy, which provides ORM functionality

# Initialize the SQLAlchemy object
db = SQLAlchemy()


# Define the QuestionAnswer model that maps to the "questions_answers" table in the database
class QuestionAnswer(db.Model):
    __tablename__ = (
        "questions_answers"  # Explicitly set the table name to "questions_answers"
    )

    # Define columns for the table
    id = db.Column(
        db.Integer, primary_key=True
    )  # 'id' is the primary key and auto-incremented
    question = db.Column(
        db.String(500), nullable=False
    )  # 'question' is a string with a max length of 500 characters, cannot be null
    answer = db.Column(
        db.Text, nullable=False
    )  # 'answer' is a Text field (no size limit), cannot be null
    created_at = db.Column(
        db.DateTime, server_default=db.func.now()
    )  # 'created_at' automatically stores the timestamp when the record is created
