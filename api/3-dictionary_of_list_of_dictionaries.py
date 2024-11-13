#!/usr/bin/python3
"""
This script fetches all employees' TODO list progress from a REST API and
exports it to a JSON file in the format:
{
    "USER_ID": [
        {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
        ...
    ],
    ...
}
"""

import json
import requests


def fetch_all_employee_data():
    """
    Fetches TODO lists for all employees.
    
    Returns:
        dict: Dictionary with each employee's ID as keys, and lists of task
              dictionaries containing 'username', 'task', and 'completed' as values.
    """
    # Fetch all users and their TODOs
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)
    users_data = users_response.json()
    todos_data = todos_response.json()

    # Initialize dictionary for all employee tasks
    all_tasks = {}

    # Populate all_tasks with each user's tasks
    for user in users_data:
        user_id = user["id"]
        username = user["username"]

        # Filter todos for the current user
        user_tasks = [
            {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            for todo in todos_data if todo["userId"] == user_id
        ]

        # Add user's tasks to all_tasks dictionary
        all_tasks[str(user_id)] = user_tasks

    return all_tasks


# Only execute if script is run directly
if __name__ == "__main__":
    # Fetch all employees' data
    all_employee_data = fetch_all_employee_data()

    # Write data to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_employee_data, jsonfile)
