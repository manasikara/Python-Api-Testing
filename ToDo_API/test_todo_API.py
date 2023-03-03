# PyTest • REST API Integration Testing with Python
# Learnig material --> https://youtu.be/7dgQRVqF1N0
# API tested --> https://todo.pixegami.io/

import requests

endpoint = "https://todo.pixegami.io/"

"""
#WRITING A TEST WITH PYTHON
response = requests.get(endpoint)
print(response)
#printing website data
data = response.json()
print(data)
#printing the status code
status_code = response.status_code
print(status_code)
"""


# WRITING A TEST WITH PYTEST

# 1st test case - get
def test_can_call_endpoint():
    response = requests.get(endpoint)
    assert response.status_code == 200
    pass


# 2nd test case - put
def test_can_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()

    task_id = data['task']['task_id']
    get_task_response = get_task(task_id)

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]


# 3rd test case - update
def test_can_update_task():
    # create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    # update the task
    new_payload = {
        "user_id": payload["user_id"],
        "task_id": task_id,
        "content": "my updated content",
        "is_done": True,
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    # get and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]

def test_can_list_tasks():
    # Create N tasks.
    N = 3
    for _ in range(3):
        payload = new_task_payload()
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    # List tasks, and check that there are N items
    pass



def create_task(payload):
    return requests.put(endpoint + "/create-task", json=payload)


def update_task(payload):
    return requests.put(endpoint + "/update-task", json=payload)


def get_task(task_id):
    return requests.get(endpoint + f"/get-task/{task_id}")


def new_task_payload():
    return {
        "content": "my test content",
        "user_id": "test_user",
        "is_done": False,
    }


# 25:13 - to be continued