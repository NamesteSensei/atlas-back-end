#!/usr/bin/python3
"""
Exports all tasks for each employee to a JSON file.
Each user's tasks are stored as a list of dictionaries, with the task title,
completion status, and username, under their respective user ID.
"""
import json
import requests


def export_all_to_json():
    """Export all employees' tasks to a JSON file."""
    # Base URL for API
    url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users = requests.get(f"{url}/users").json()

    # Dictionary to store the tasks for all employees
    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        # Fetch tasks for each user
        todos = requests.get(
            f"{url}/todos", params={"userId": user_id}
        ).json()

        # List to store the formatted tasks for each user
        user_tasks = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in todos
        ]

        # Add to main dictionary under the user's ID
        all_tasks[user_id] = user_tasks

    # Export to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


# Main block to execute function
if __name__ == "__main__":
    export_all_to_json()
