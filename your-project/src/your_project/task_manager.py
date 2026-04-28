import heapq
from typing import List, Optional
from .task import Task

class TaskManager:
    # Creates empty list for tasks
    def __init__(self):
        self.tasks: List[Task] = []
        
    # Add task to the heap 
    def add_task(self, task: Task):
        heapq.heappush(self.tasks, task)

    # Gets the highest priority task 
    def get_next_task(self) -> Optional[Task]:
        if not self.tasks:
            return None 
        return heapq.heappop(self.tasks)
    
    # Checks if task queue is empty 
    def is_empty(self) -> bool:
        return len(self.tasks) == 0 