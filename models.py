from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class QuestionAnswer(db.Model):
    __tablename__ = "questions_answers"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())