#!/usr/bin/python3
"""
Script to retrieve employee's TODO list progress for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    # Ensure script is called with an employee ID argument
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Base URL for JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    # Fetch tasks data
    tasks = requests.get(f"{base_url}/todos?userId={employee_id}").json()

    # Get the employee's name and calculate task progress
    employee_name = user.get("name")
    total_tasks = len(tasks)
    completed_tasks = [task["title"] for task in tasks if task["completed"]]

    # Print the formatted output
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for title in completed_tasks:
        print(f"\t {title}")
