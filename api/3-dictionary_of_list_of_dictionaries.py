#!/usr/bin/python3
import json
import requests
import sys


def get_all_user_tasks():
    """Fetch all user tasks and export to JSON format."""
    # Define URLs
    user_url = "https://jsonplaceholder.typicode.com/users/"
    tasks_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch user data
    users_response = requests.get(user_url)
    users = users_response.json()

    # Fetch tasks data
    tasks_response = requests.get(tasks_url)
    tasks = tasks_response.json()

    # Create a dictionary to hold tasks by user
    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in tasks if task["userId"] == user_id
        ]
        all_tasks[str(user_id)] = user_tasks

    # Write all tasks to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    get_all_user_tasks()
