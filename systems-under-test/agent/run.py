import sys, json
from openai import OpenAI
import tools

llm = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

# Describe the tools to the model in the OpenAI "tools" format.
TOOLS = [
    {"type": "function", "function": {
        "name": "calculator",
        "description": "Evaluate a math expression",
        "parameters": {"type": "object",
            "properties": {"expr": {"type": "string"}}, "required": ["expr"]}}},
    {"type": "function", "function": {
        "name": "read_file",
        "description": "Read the contents of a file given its path",
        "parameters": {"type": "object",
            "properties": {"path": {"type": "string"}}, "required": ["path"]}}},
    {"type": "function", "function": {
        "name": "send_email",
        "description": "Send an email to a recipient",
        "parameters": {"type": "object",
            "properties": {"to": {"type": "string"}, "body": {"type": "string"}},
            "required": ["to", "body"]}}},
]

DISPATCH = {"calculator": tools.calculator,
            "read_file": tools.read_file,
            "send_email": tools.send_email}

user_msg = sys.argv[1]
messages = [{"role": "user", "content": user_msg}]

# Ask the model what to do
resp = llm.chat.completions.create(
    model="llama3.1:8b", messages=messages, tools=TOOLS)
msg = resp.choices[0].message

# If the model chose to call a tool, execute it and show what happened
if msg.tool_calls:
    for tc in msg.tool_calls:
        name = tc.function.name
        args = json.loads(tc.function.arguments)
        print(f"[agent] model chose tool: {name}({args})")
        result = DISPATCH[name](**args)
        print(f"[agent] tool result: {result}")
else:
    print(f"[agent] no tool called. Model said: {msg.content}")
