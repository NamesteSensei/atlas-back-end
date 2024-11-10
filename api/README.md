# Atlas Back-End API Project

## Project Overview

This project is designed to interact with a REST API to gather data about an employee's TODO list progress. For a given employee ID, the script retrieves the employee's name and the completion status of their tasks, then displays a summary of completed tasks.

### Learning Objectives

This project helps to deepen understanding of the following concepts:

- What an API and a REST API are
- Usage and best practices for Pythonic naming conventions
- Appropriate applications and limitations of Bash scripting
- Basics of the CSV and JSON formats
- Python package and module organization following PEP8 style guidelines

## Requirements

- **Editor:** vi, vim, or emacs
- **Environment:** Ubuntu 20.04 LTS with Python 3.8.X
- **Python Libraries:** Only standard libraries (`requests` or `urllib` for API requests)
- **Execution Permissions:** Ensure the script is executable (`chmod +x`)
- **File Structure:** 
  - All Python files should end with a newline
  - Use `get()` for dictionary access to avoid KeyErrors
  - Use `if __name__ == "__main__":` to prevent unintended execution

## Files

- **0-gather_data_from_an_API.py**: The main Python script to gather and display data about an employee's TODO list.

## Usage

To use the script, provide an employee ID as a command-line argument.

```bash
./0-gather_data_from_an_API.py <employee_id>
