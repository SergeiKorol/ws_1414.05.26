import requests
def test_cannot_create_completed_task():
    """тест о котлетах"""
    body = {"title": "completed task", "completed": True}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)

    assert response.status_code == 400
