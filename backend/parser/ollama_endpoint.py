import json
import requests

from langchain.llms import Ollama

MODEL = "mistral"
PORT = 11434


def prompt_ollama_single(prompt):
    return prompt_ollama(prompt)


def prompt_ollama_chat(chat_history):
    message = "\n\n".join([c["message"] for c in chat_history])
    return prompt_ollama(message)


def prompt_ollama(prompt):
    ollama = Ollama(base_url=f"http://localhost:{PORT}", model=MODEL)
    message = ollama(prompt)
    response = dict()
    response["role"] = "assistant"
    response["message"] = message
    return response
