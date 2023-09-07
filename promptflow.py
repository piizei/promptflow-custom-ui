
from promptflow_client import send
import json


def adapt_openai_to_prompt_flow(messages):
    transformed_data = {"chat_history": []}
    current_chat = None
    # Iterate through the original JSON data
    for item in messages:
        if item["role"] == "user":
            current_chat = {"inputs": {"chat_input": item["content"]}}
        elif item["role"] == "assistant" and current_chat:
            current_chat["outputs"] = {"chat_output": item["content"]}
            transformed_data["chat_history"].append(current_chat)

    # Add the last user input (if any)
    if current_chat:
        transformed_data["chat_input"] = current_chat["inputs"]["chat_input"]
        
    response = send(transformed_data)
    return response["chat_output"]
    