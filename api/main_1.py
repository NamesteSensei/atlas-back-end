#!/usr/bin/python3
import sys
import csv

def user_info(user_id):
    """Retrieve and display user info from CSV file based on user_id."""
    try:
        with open(f"{user_id}.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"No CSV file found for user ID {user_id}.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            user_id = int(sys.argv[1])
            user_info(user_id)
        except ValueError:
            print("Please provide a valid integer as user ID.")
    else:
        print("Usage: python3 main_1.py <user_id>")
