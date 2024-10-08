import json  # Import the json module to handle JSON data
from app import app  # Import the Flask app instance from the app module


def test_ask_question():
    """
    Unit test for the /ask endpoint.
    This test sends a POST request with a sample question and verifies the response.
    """
    # Create a test client for the Flask app, allowing us to make requests to the app as if we're a client.
    tester = app.test_client()

    # Send a POST request to the /ask endpoint with a JSON payload.
    # The question "What is AI?" is sent as part of the request.
    response = tester.post(
        "/ask",  # The URL to send the request to
        data=json.dumps({"question": "What is AI?"}),  # The request body (JSON payload)
        content_type="application/json",  # Specify that the request content is JSON
    )

    # Assert that the response status code is 200 (OK), indicating the request was successful.
    assert response.status_code == 200

    # Parse the response data from JSON format into a Python dictionary.
    data = json.loads(response.data)

    # Assert that the key "answer" is present in the response, meaning the API returned an answer.
    assert "answer" in data