from models.task import TaskModel
from schemas.task import Task, TaskCreate
from services.exceptions import TaskNotFoundError
from sqlalchemy.orm import Session

def update_task_service(db: Session, task_id, title, description):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise TaskNotFoundError(task_id)
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    db.commit()
    db.refresh(task)
    return task
    


def create_task_service(db: Session, task: TaskCreate):
    new_task = TaskModel(
        title=task.title,
        description=task.description
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_task_service(db: Session, task_id: int):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise TaskNotFoundError(task_id)
    return task

def get_tasks_service(db: Session):
    tasks = db.query(TaskModel).all()
    return tasks

def delete_task_service(db: Session, task_id: int):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if task is None:
        raise TaskNotFoundError(task_id)
    db.delete(task)
    db.commit()
    return task
        