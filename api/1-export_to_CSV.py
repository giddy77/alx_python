import requests
import sys
import csv

def get_employee_todo_list_progress(employee_id):
    # Fetch employee details
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(employee_url)
    employee_data = response.json()

    if 'name' not in employee_data:
        print(f"Employee with ID {employee_id} not found.")
        return

    employee_name = employee_data['name']

    # Fetch employee's TODO list
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(todo_url)
    todo_data = response.json()

    # Create a CSV file for the employee
    csv_file_name = f'{employee_id}.csv'

    # Calculate the progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    # Print employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

    # Write the CSV header
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write the CSV data
        for task in todo_data:
            task_status = "Completed" if task['completed'] else "Not Completed"
            csv_writer.writerow([employee_id, employee_name, task_status, task['title']])

    print(f"Data exported to {csv_file_name}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py [employee_id]")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_list_progress(employee_id)
