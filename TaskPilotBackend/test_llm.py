import json

from agent.tool_dispatch import TOOL_REGISTRY
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
    {
        "role": "system",
        "content": (
            "You are TaskPilot, an assistant that helps users manage their tasks. "
            "You have access to tools for creating, reading, updating, and deleting tasks. "
            "If a tool call fails (for example, a task ID doesn't exist), do not retry the same call. "
            "Instead, explain the failure to the user in plain language and, if helpful, suggest what they might check."
        )
    },
    {"role": "user", "content": "Rename task 3 to 'Study French' and update its description to 'Complete tasks'"}
]



response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools
)

print(response.choices[0].message)

assistant_message = response.choices[0].message
# tool_call = assistant_message.tool_calls[0]
# raw_args = json.loads(tool_call.function.arguments)
# validated_args = UpdateTaskToolArgs(**raw_args)

for tool_call in assistant_message.tool_calls:
    function_to_call = TOOL_REGISTRY.get(tool_call.function.name)
    print(f"selected: {function_to_call}")

    raw_args = json.loads(tool_call.function.arguments)
    validated_args = UpdateTaskToolArgs(**raw_args)
    # print(f"selected: {function_to_call}")

    # print(f"validated args {validated_args}")

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
    # print(tool_result_content)
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

# print(f"final: {final_response.choices[0].message}")