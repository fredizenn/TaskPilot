from services.task_service import create_task_service, delete_task_service, get_task_service, update_task_service
from agent.tool_schemas import CreateTaskToolArgs, DeleteTaskToolArgs, GetTaskToolArgs, UpdateTaskToolArgs


def call_create_task(db, args: CreateTaskToolArgs):
    return create_task_service(db, args)
    
def call_update_task(db, args: UpdateTaskToolArgs):
    return update_task_service(db, args.task_id, args.title, args.description)

def call_get_task(db, args: GetTaskToolArgs):
    
    return get_task_service(db, args.task_id)


def call_delete_task(db, args: DeleteTaskToolArgs):
    return delete_task_service(db, args.task_id)

TOOL_REGISTRY = {
    "create_task": (CreateTaskToolArgs, call_create_task),
    "update_task": (UpdateTaskToolArgs, call_update_task),
    "get_task": (GetTaskToolArgs, call_get_task),
    "delete_task": (DeleteTaskToolArgs, call_delete_task),
}