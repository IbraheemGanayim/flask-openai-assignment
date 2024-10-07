import json
from app import app

def test_ask_question():
    tester = app.test_client()
    response = tester.post(
        '/ask',
        data=json.dumps({"question": "What is AI?"}),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "answer" in data