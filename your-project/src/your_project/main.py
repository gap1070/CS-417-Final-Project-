# This file is the main entry for this program 

# Import the Task class from task.py
from .task import Task 
from .task_manager import TaskManager

def main():
    # Creates manager 
    manager = TaskManager()

    # Creates a loop that will go on until user selects exit 
    while True:
        # Option Menu
        print("\n=== Smart To-DO List ===")
        print("1. Add Task")
        print("2. Get Next Task")
        print("3. Exit")

        # Gets the users choice 
        choice = input("Choose an option: ")

        # Option 1: Adds new task
        if choice == "1":
            name = input("Task Name: ")

            # Makes sure numbers are valid 
            try:
                importance = int(input("Importance (1-5): "))
                urgency = int(input("Urgency (1-5): "))
            except ValueError:
                print("Please enter valid numbers.")
                # restarts the loop if the numbers are not valid 
                continue 

            # Actually creates and add the task
            task = Task(name, importance, urgency)
            manager.add_task(task)
            print("Task Added!")

        # Option 2: Get next highest priority task



# Runs the program 
if __name__ == "__main__":
    main()