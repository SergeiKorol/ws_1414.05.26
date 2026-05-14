import requests


def test_delete_and_check():
    create_data = {
        "title": "Test Task",
        "completed": False
    }


create_response = requests.post(
    "https://todo-app-sky.herokuapp.com/",
    json=create_data
)
"""Поменяли что-то"""

assert create_response.status_code == 200, "Ошибка создания задачи"
task_id = create_response.json().get('id')

delete_response = requests.delete(
    f"https://todo-app-sky.herokuapp.com/{task_id}"
)

assert delete_response.status_code == 200, "Ошибка удаления задачи"

get_deleted_response = requests.get(
    f"https://todo-app-sky.herokuapp.com/{task_id}"
)

assert get_deleted_response.status_code == 404

