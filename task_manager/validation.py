from datetime import datetime

def validate_task_title(title):
    if not isinstance(title,str): #Ensure the data type is a string
        return False
    return True
    
def validate_task_description(description):
    if not isinstance(description,str): #Ensure the data type is a string
        return False
    return True
    
def validate_due_date(due_date): #Ensure the data type is of the format YYYY-mm-dd
    try:
        datetime.strptime(due_date,'%Y-%m-%d')
        return True
    except ValueError:
        print(f"Invalid yyyy-mm-dd string for {due_date}")
        return False