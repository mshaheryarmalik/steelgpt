import sys
import logging

from backend.parser.api_draft import process_query

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    prompt = sys.argv[-1]
    chat_history = [{"role": "user", "message": prompt}]
    print(process_query(chat_history))
