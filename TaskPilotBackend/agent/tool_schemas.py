from typing import Optional

from pydantic import BaseModel, Field

class CreateTaskToolArgs(BaseModel):
    title: str = Field(..., description="The title of the task being added")
    description: Optional[str] = Field(None, description="The description of the task being added")

class UpdateTaskToolArgs(BaseModel):
    task_id: int = Field(..., description="The id of the task being updated")
    title: Optional[str] = Field(None, description="The new title")
    description: Optional[str] = Field(None, description="The new description")
    
class GetTaskToolArgs(BaseModel):
    task_id: int = Field(..., description="The id of the task being retrieved")
    
class DeleteTaskToolArgs(BaseModel):
    task_id: int = Field(..., description="The id of the task being deleted")