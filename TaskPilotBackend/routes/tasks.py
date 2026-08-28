from fastapi import APIRouter, Depends, HTTPException

from schemas.task import TaskCreate
from services.exceptions import TaskNotFoundError
from services.task_service import create_task_service, delete_task_service, get_task_service, get_tasks_service, update_task_service
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return get_tasks_service(db)

@router.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    try:
        return get_task_service(db, task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")

@router.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task_service(db, task)

@router.patch("/tasks/{task_id}")
def update_task(task_id: int, task_req: TaskCreate, db: Session = Depends(get_db)):
    try:
        return update_task_service(db, task_id, task_req.title, task_req.description)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    try:
        return delete_task_service(db, task_id)
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")        
    
