#!/usr/bin/python3
"""
This script fetches an employee's TODO list from a REST API and exports
the data to a JSON file in the format:
{
  "USER_ID": [
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"},
    ...
  ]
}
"""

import json  # For writing data to a JSON file
import requests  # For making HTTP requests to the API
import sys  # For handling command-line arguments


def fetch_employee_data(employee_id):
    """
    Fetches employee info and TODO list based on employee ID.
    Args:

        employee_id (int): The ID of the employee.
    Returns:

        tuple: A tuple containing the employee's name and list of tasks.
    """
    # Define URLs for employee info and TODO list
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    # Fetch employee data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("username")  # Get the employee's username

    # Fetch employee's TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    return employee_name, todos_data


def export_to_json(employee_id, employee_name, todos_data):
    """
    Exports the TODO list data to a JSON file.
    Args:

        employee_id (int): The ID of the employee.
        employee_name (str): The username of the employee.
        todos_data (list): List of tasks associated with the employee.
    """
    # Structure the data for JSON export
    json_data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name
            } for task in todos_data
        ]
    }

    # Define JSON filename
    filename = f"{employee_id}.json"
    # Write data to JSON file

    with open(filename, mode="w") as jsonfile:
        json.dump(json_data, jsonfile)


# Only execute if script is run directly
if __name__ == "__main__":
    # Validate input
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Fetch employee data and TODO list
    employee_name, todos_data = fetch_employee_data(employee_id)

    # Export data to JSON
    export_to_json(employee_id, employee_name, todos_data)
