class TaskServiceError(Exception):
    def __init__(self, message="An error occurred"):
        self.message = message
        super().__init__(self.message)
    
class TaskNotFoundError(TaskServiceError):
    def __init__(self, task_id):
        self.task_id = task_id
        message = f"Task {task_id} not found"
        super().__init__(message)