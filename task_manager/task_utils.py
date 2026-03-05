from datetime import datetime

# Import validation functions
from task_manager.validation import validate_task_title,validate_task_description,validate_due_date

# Define tasks list(default is empty)
tasks = []


#Implement add_task function
#Define the task as a dictionary
#Add a task to a list of tasks using append()
def add_task(title, description, due_date):

    if not validate_task_title(title):
        return
    if not validate_task_description(description):
        return
    if not validate_due_date(due_date):
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date
    }

    tasks.append(task)

    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    #Validate the index input
    #Check if it is an integer
    if not isinstance(index,int):
        return
    
    #check if the index is less than 0
    if index < 0:
        return
    
    #check if the position of the element can be accessed
    try:
        tasks[index]["completed"] = True #add a key called COMPLETED and set it to true
        print("Task marked as complete!")
    except IndexError as e:
        print(e)
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [] #Default list of pending tasks

    for task in tasks:
        if not task.get("completed"):
            pending_tasks.append(task)
    
    print(pending_tasks)


# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    completed_tasks = 0 #default is zero if there are no completed tasks
    num_of_tasks = len(tasks) #Evaluate the number of tasks using len()

    for task in tasks:
        if task.get("completed"): #check if the task has been completed
            completed_tasks = completed_tasks + 1 #increment progress by one if task has been completed
    
    progress = completed_tasks/num_of_tasks *100 #calculate progress as a percentage

    return progress

#Test cases
""" add_task("Parcel","Send parcel to my sister","2020-09-20")
add_task("Groceries","Shop at Market Basket for food","2024-06-26")

print(tasks)

mark_task_as_complete(1,tasks=tasks)

view_pending_tasks(tasks=tasks)

print(calculate_progress(tasks=tasks)) """




    