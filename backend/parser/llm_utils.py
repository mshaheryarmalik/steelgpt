from .ollama_endpoint import (
    prompt_ollama_single,
    prompt_ollama_chat,
)

BACKEND =  "ollama"


def get_mock_response(prompt):
    return {"role": "assistant", "message": '["This is a mock response"]'}


def get_llm_queries(original_query):
    # Compile the LLM prompt
    question = (
        "You are an expert on steel production processes and have been tasked "
        "with researching the following topic:\n"
    )
    question += original_query
    question += (
        "\nWhat web searches would you do to research the topic further?\n"
        "Answer with a JSON formatted list containing five search queries."
    )
    # Prompt the model
    return call_model_single(question)


def get_system_prompt():
    prompt = (
        "You are an expert in steel production and energy-related subjects.\n"
        "You are given a context with numbered sources and a question.\n"
        "You must answer the question based only on the provided context.\n"
        "When compiling your response, refer to source in the context by putting "
        "the source number in square brackets.\n"
    )
    return prompt


def get_llm_response(chat_history):
    return call_model_chat(chat_history)


def call_model_single(prompt):
    model_call_function = get_mock_response
    if BACKEND == "ollama":
        model_call_function = prompt_ollama_single
    response = ""
    if model_call_function:
        response = model_call_function(prompt)
    return response["message"]


def call_model_chat(chat_history):
    model_call_function = get_mock_response
    if BACKEND == "ollama":
        model_call_function = prompt_ollama_chat
    response = ""
    if model_call_function:
        response = model_call_function(chat_history)
    return response
