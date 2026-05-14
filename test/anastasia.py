import requests


def test_add_edit():
    body = {"title": "generated", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]
    body = {"title": "generated-1"}
    response = requests.patch(f"https://todo-app-sky.herokuapp.com/{id}", json=body)
    assert response['id'] == id
