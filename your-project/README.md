Smart  TO-Do List 

What the poject does
This project is a command-line Smart To-Do list that was created to help its users organize tasks based on how important and how urgent the task is. After the user inputs those numbers, the program calculates the tasks priority score for each task, and will always return the task with the highest priority score (or the most important task to complete). 

How to install dependencies and run it 
1.  Make sure that you have python installed 
2. Open up a terminal and cd to the "your-project" directory, and then into the "src" directory
3. Finally, run the porgram using "python -m your_project"

The data structures and algorithms I used 
- Heap (priority queue)
Located in task_manager.py
This program uses pythons heapq in order to store the tasks in the heap. It does this so that the highest priority task out of all the tasks will be able to get retrieved easily, and efficiently. 
- A custom priority algorithm 
Located in task.py (the priority method)
This algorithm taks each task and calculates its priority based on the importance, and urgency that the user inputted, also how old a task is. Older tasks slower become more important as the days go on. 
- Sorting for the purpose of displaying 
Located in task_manager.py (in get_all_tasks)
Uses pythons sorted() function in order to return all the tasks ordered by there priority, without having to modify the heap. 

What's working 
- Adding tasks with there importance and urgency 
- The algorithm automatically calculating each tasks priority 
- Retrieving the highest priority task 
- Viewing every task the user inputted all at once, sorted by there priority 
- Handles invalid numbers, and inputs without crashing
- Handles the empty task lists correctly without crashing 

Limitations
- After you exit the program, your tasks do not get saved
- No option to edit tasks, or delete them (automatically does when you retrieve the highest priority task)
- In order to update the priority, the heap needs to be rebuilt 
- Only runs in th command line (no special interface)

Ai Usage 