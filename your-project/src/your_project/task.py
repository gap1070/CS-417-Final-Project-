# This file defines the Task class for the whole program

class Task:
    def __init__(self, name: str, priority: int):
        # Stores the task name and its priority 
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        # Reverse comparison so the higher priority task comes first within the heap 
        return self.priority > other.priority
    
    def __repr__(self):
        # Makes it so the printing tasks are easier to read 
        return f"Task(name={self.name}, priority={self.priority})"