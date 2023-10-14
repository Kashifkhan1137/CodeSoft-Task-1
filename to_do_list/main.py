import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

def load():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def add(task):
    tasks = load()
    tasks.append(task)
    save(tasks)
    print("Task added successfully!")

def list():
    tasks = load()
    if tasks:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("No tasks found.")

def remove(index):
    tasks = load()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save(tasks)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add(task)
        elif choice == "2":
            list()
        elif choice == "3":
            list()
            index = int(input("Enter the task index to remove: ")) - 1
            remove(index)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Lets Run the Program
#
