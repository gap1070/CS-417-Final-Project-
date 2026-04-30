# This file defines the Task class for the whole program

# Used for tracking the time 
from datetime import datetime 

class Task:
    def __init__(self, name: str, importance: int, urgency: int):
        # Stores the task name and its priority 
        self.name = name
        self.importance = importance
        self.urgency = urgency
        # Stores when the task was created, for smart priority 
        self.created_at = datetime.now()

    def priority(self) -> int:
        # The base score using importance and urgency 
        base_score = self.importance * 2 + self.urgency

        # Calculates how many days old a task is 
        age_days = (datetime.now() - self.created_at).days 

        # How older tasks slowly become higher and higher priority 
        return base_score + age_days

    def __lt__(self, other):
        # Reverse comparison so the higher priority task comes first within the heap 
        return self.priority() > other.priority()
    
    def __repr__(self):
        # Makes it so the printing tasks are easier to read for debugging
        return f"Task({self.name}, imp={self.importance}, urg={self.urgency})"
    
    def __str__(self):
        # Used for making the tasks print cleanly 
        return f"{self.name}, imp={self.importance}, urg={self.urgency}"