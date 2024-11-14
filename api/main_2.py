#!/usr/bin/python3
import sys
import csv
import os

def user_info(user_id):
    # Construct the file name from the user_id
    filename = f"{user_id}.csv"
    
    # Check if the file exists
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return
    
    # Open and read the CSV file
    with open(filename, mode='r') as f:
        reader = csv.reader(f)
        # Print each line in the desired format
        for row in reader:
            print(f"User ID: {row[0]}, Username: {row[1]}, "
                  f"Task Completed: {row[2]}, Task Title: {row[3]}")

# Main execution block
if __name__ == "__main__":
    # Ensure a user ID is provided
    if len(sys.argv) < 2:
        print("Usage: main_2.py <user_id>")
    else:
        try:
            # Convert user ID to integer and get user info
            user_id = int(sys.argv[1])
            user_info(user_id)
        except ValueError:
            print("User ID must be an integer.")
