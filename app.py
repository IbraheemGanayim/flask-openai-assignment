from flask import Flask, request, jsonify
from models import db, QuestionAnswer
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# PostgreSQL configuration for Docker
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:example@db:5432/questions_db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
db.init_app(app)


@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        # Mock OpenAI response (replace with actual API call later)
        answer = f"This is a mocked response for: {question}"

        # Save question and answer to the database
        new_entry = QuestionAnswer(question=question, answer=answer)
        db.session.add(new_entry)
        db.session.commit()

        return jsonify({"question": question, "answer": answer}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)