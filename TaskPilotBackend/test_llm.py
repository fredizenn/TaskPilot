import json

from services.exceptions import TaskNotFoundError
from services.task_service import update_task_service
from database import SessionLocal
from agent.tool_schemas import UpdateTaskToolArgs
from agent.client import client

db = SessionLocal()


tools = [
    {
        "type": "function",
        "function": {
            "name": "update_task",
            "description": "Update the title and/or description of an existing task, identified by its ID.",
            "parameters": UpdateTaskToolArgs.model_json_schema()
        }
    }
]

messages = [
    {"role": "user", "content": "Rename task 3 to 'Study French' and update its description to 'Complete tasks'"}
]



response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools
)

print(response.choices[0].message)

assistant_message = response.choices[0].message
tool_call = assistant_message.tool_calls[0]
raw_args = json.loads(tool_call.function.arguments)
validated_args = UpdateTaskToolArgs(**raw_args)

print(f"validated args {validated_args}")

try:
    result = update_task_service(
        db,
        validated_args.task_id,
        validated_args.title,
        validated_args.description
    )
    tool_result_content = f"Task updated: id={result.id}, title='{result.title}', description='{result.description}'"
    print(result.id, result.title, result.description)
except TaskNotFoundError as e:
    tool_result_content = f"Error: {e}"
finally:
    db.close()
    
    
    
messages.append(assistant_message)
messages.append({
    "role": "tool",
    "tool_call_id": tool_call.id,
    "content": tool_result_content
})
    
final_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools
)

print(final_response.choices[0].message.content)