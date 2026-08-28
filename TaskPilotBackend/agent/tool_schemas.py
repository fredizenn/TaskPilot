from typing import Optional

from pydantic import BaseModel

class CreateTaskToolArgs(BaseModel):
    title: str
    description: Optional[str] = None

class UpdateTaskToolArgs(BaseModel):
    task_id: int
    title: Optional[str] = None
    description: Optional[str] = None
    
class GetTaskToolArgs(BaseModel):
    task_id: int
    
class DeleteTaskToolArgs(BaseModel):
    task_id: int