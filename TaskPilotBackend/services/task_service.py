from schemas.task import Task, TaskCreate
from services.exceptions import TaskNotFoundError

tasks = []

next_task_id = 1

def update_task_service(task_id, title, description):
    for task in tasks:
        if task.id == task_id:
            task.title = title
            task.description = description
            return task
    raise TaskNotFoundError(task_id)
    
def get_tasks_service():
    return tasks

def create_task_service(task: TaskCreate):
    global next_task_id
    
    new_task = Task(
        id=next_task_id,
        title=task.title,
        description=task.description
    )
    
    
    tasks.append(new_task)
    
    next_task_id += 1
    
    return new_task

def get_task_service(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
            
    raise TaskNotFoundError(task_id)

def delete_task_service(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return task
    raise TaskNotFoundError(task_id)
        