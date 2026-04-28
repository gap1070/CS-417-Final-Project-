# This file is the main entry for this program 

# Import the Task class from task.py
from .task import Task 
from .task_manager import TaskManager

def main():
    # Creates manager 
    manager = TaskManager()

    # Example tasks 
    manager.add_task(Task("Homework", 5, 4))
    manager.add_task(Task("Workout", 3, 3))
    manager.add_task(Task("Videgames", 2, 2))

    # Makes sure to process the tasks in the right order 
    while not manager.is_empty():
        task = manager.get_next_task()
        print(task)

# Runs the program 
if __name__ == "__main__":
    main()