# This file defines the Task class for the whole program

class Task:
    def __init__(self, name: str, importance: int, urgency: int):
        # Stores the task name and its priority 
        self.name = name
        self.importance = importance
        self.urgency = urgency

    def priority(self) -> int:
        # Calculate the score for the tasks priority rank
        return self.importance * 2 + self.urgency

    def __lt__(self, other):
        # Reverse comparison so the higher priority task comes first within the heap 
        return self.priority() > other.priority()
    
    def __repr__(self):
        # Makes it so the printing tasks are easier to read 
        return f"Task({self.name}, imp={self.importance}, urg={self.urgency})"