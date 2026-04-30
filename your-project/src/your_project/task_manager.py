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
        
        # Rebuilds the heap since the prioritys get changed over time
        heapq.heapify(self.tasks)

        # Removes and returns the highest priority task 
        return heapq.heappop(self.tasks)
    
    # Checks if task queue is empty 
    def is_empty(self) -> bool:
        return len(self.tasks) == 0 
    
    # Returns every task inputted sorted by priority rank (does not remove any tasks)
    def get_all_tasks(self) -> list[Task]:
        # Using sorted() because it doesn't chnage the original heap 
        return sorted(self.tasks, key=lambda t: t.priority(), reverse=True)