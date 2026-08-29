from agent.tool_schemas import UpdateTaskToolArgs
import json

print(json.dumps(UpdateTaskToolArgs.model_json_schema(), indent=2))