#!/usr/bin/python3
"""
This script fetches and displays an employee's TODO list progress using
a REST API. Given an employee ID, it retrieves the employee's name and
tasks, then displays the number of completed tasks along with a list of
task titles.
"""

import requests  # For making HTTP requests to the API
import sys       # For handling command-line arguments


def fetch_employee_data(employee_id):
    """
    Fetch and display TODO list progress for a given employee ID.
    Args:

        employee_id (int): The ID of the employee.
    """

    # Define URLs for employee info and TODO list
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    # Fetch employee data (name) from the API
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")  # Extract employee's name

    # Fetch employee's TODO list from the API
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate total and completed tasks
    total_tasks = len(todos_data)  # Total number of tasks
    completed_tasks = [
        task for task in todos_data if task.get("completed")
    ]  # List of completed tasks
    number_of_done_tasks = len(completed_tasks)  # Number of completed tasks

    # Display summary of tasks completed
    print(
        f"Employee {employee_name} is done with tasks("
        f"{number_of_done_tasks}/{total_tasks}):"
    )
    # Display titles of each completed task, indented with tab
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


# Only execute if script is run directly, not imported
if __name__ == "__main__":
    # Check if exactly one argument (employee ID) is provided
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Convert argument to integer and validate
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Fetch and display data for the given employee ID
    fetch_employee_data(employee_id)
