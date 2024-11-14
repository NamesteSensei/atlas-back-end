#!/usr/bin/python3
"""
This script fetches an employee's TODO list progress from the JSONPlaceholder
API and displays the number of completed tasks along with their titles.
"""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetches the TODO list progress for an employee based on their ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        str: Formatted string showing the employee's name, task completion
             progress, and completed task titles.
    """
    # Define URLs for employee info and TODO list
    user_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    # Fetch employee data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        return "Error: Could not fetch employee data."

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch employee's TODO list
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        return "Error: Could not fetch employee TODO data."

    todos_data = todos_response.json()

    # Calculate task progress
    completed_tasks = [
        task["title"] for task in todos_data if task["completed"]
    ]
    total_tasks = len(todos_data)

    # Format the output
    result = (
        f"Employee {employee_name} is done with tasks"
        f"({len(completed_tasks)}/{total_tasks}):"
    )
    for task_title in completed_tasks:
        result += f"\n\t {task_title}"

    return result


# Only execute if script is run directly
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Print the employee's TODO progress
    print(fetch_employee_todo_progress(employee_id))
