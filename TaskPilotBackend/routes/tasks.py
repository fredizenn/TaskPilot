from fastapi import APIRouter, HTTPException

from schemas.task import TaskCreate
from services.exceptions import TaskNotFoundError, TaskServiceError
from services.task_service import create_task_service, delete_task_service, get_task_service, get_tasks_service, update_task_service

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return get_tasks_service()

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    try:
        return get_task_service(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@router.post("/tasks")
def create_task(task: TaskCreate):
    return create_task_service(task)

@router.patch("/tasks/{task_id}")
def update_task(task_id: int, task_req: TaskCreate):
    try:
        return update_task_service(task_id, task_req.title, task_req.description)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    try:
        return delete_task_service(task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")        
    
