from flask import Flask, request, jsonify
from models import db, QuestionAnswer
from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# PostgreSQL configuration for Docker
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:example@db:5432/questions_db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
db.init_app(app)

# Initialize OpenAI client
openai_client = OpenAI()


@app.route("/ask", methods=["POST"])
def ask_question():
    """
    API endpoint to handle POST requests with a question and return an AI-generated answer.
    Stores both the question and answer in the PostgreSQL database.
    """
    data = request.get_json()

    # Validate that a JSON request was sent and contains a 'question' key
    if not data or not data.get("question"):
        return jsonify({"error": "No question provided or invalid request format"}), 400

    question = data["question"]

    try:
        # Call OpenAI API with the user's question using the gpt-4o-mini model
        completion = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ],
        )

        # Correctly access the 'content' from the message
        answer = completion.choices[0].message.content.strip()

        # Save the question and answer to the database
        new_entry = QuestionAnswer(question=question, answer=answer)
        db.session.add(new_entry)
        db.session.commit()

        # Return the question and generated answer as a JSON response
        return jsonify({"question": question, "answer": answer}), 200

    except Exception as e:
        # Handle any errors during OpenAI API call or database operations
        return jsonify({"error": f"Server error: {str(e)}"}), 500


@app.errorhandler(404)
def not_found(error):
    """Custom 404 error handler."""
    return jsonify({"error": "Endpoint not found"}), 404


if __name__ == "__main__":
    # Run the Flask app with debugging disabled for production
    app.run(host="0.0.0.0", port=5000)