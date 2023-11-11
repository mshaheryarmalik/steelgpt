import json

from .utils import (
    get_top_results,
    result_to_text,
)
from .llm_utils import (
    get_llm_queries,
    get_system_prompt,
    get_llm_response,
)
from ..scrapper.utils import scrape_query


# TODO: Add retry functionality via tenacity
def get_additional_queries(query):
    # Send the prompt to the LLM
    response = get_llm_queries(query)
    # Attempt to interpret the reply as a JSON list
    print(response)
    additional_queries = json.loads(response)
    return additional_queries


def compile_context(original_query):
    # Get additional queries from a language model
    queries = [original_query]
    queries.extend(get_additional_queries(original_query))
    # Do search queries and scrape results
    scraped_texts = list()
    for q in queries:
        scraped_texts.extend(scrape_query(q))
    # Rank the received results
    top_results = get_top_results(scraped_texts, original_query)
    # Compile the context message
    context = "\n\n".join(
        [f"{i+1}: " + result_to_text(result) for i, result in enumerate(top_results)]
    )
    return context


def process_query(chat_history):
    # Get the newest message from the chat
    latest_message = chat_history[-1]
    role = latest_message["role"]
    content = latest_message["message"]
    # If it's the first one
    if len(chat_history) == 1:
        # Prepend the system prompt
        chat_history.insert(0, get_system_prompt())
        # Append the context
        chat_history.insert(-1, compile_context(content))
    # Send the chat to the language model
    response = get_llm_response(chat_history)
    # Append the response to chat history
    chat_history.append(response)
    return chat_history
