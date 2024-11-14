#!/usr/bin/python3
"""
Script to test 0-gather_data_from_an_API.py for correct employee name output.
"""

import subprocess
import sys

def user_info(employee_id):
    # Run the script and capture the output
    result = subprocess.run(
        ['./0-gather_data_from_an_API.py', str(employee_id)],
        text=True, capture_output=True
    )
    output = result.stdout.strip()
    
    # Expected employee name for employee_id 6
    expected_name = "Mrs. Dennis Schulist"
    
    # Check if the output contains the correct employee name
    if expected_name in output:
        print("Employee Name: OK")
    else:
        print("Employee Name: Incorrect")

# Only execute if script is run directly
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main_0.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    user_info
