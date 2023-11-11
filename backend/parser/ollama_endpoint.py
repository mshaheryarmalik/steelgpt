import json
import requests

MODEL = "mistral"
PORT = 11434


def prompt_ollama_single(prompt):
    return prompt_ollama(prompt)


def prompt_ollama_chat(chat_history):
    message = "\n\n".join([c["message"] for c in chat_history])
    return prompt_ollama(message)


def prompt_ollama(prompt):
    data = dict()
    data["model"] = MODEL
    data["prompt"] = prompt
    data["format"] = "json"
    data["stream"] = "false"
    model_endpoint = f"http://localhost:{PORT}/api/generate"
    http_response = requests.post(model_endpoint, json=json.dumps(data))
    response = dict()
    response["role"] = "assistant"
    response["message"] = response["response"]
    return response
