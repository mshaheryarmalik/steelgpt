from scrapper import get_contents_from_query
from constants import MAX_SEARCH_LINKS

if __name__ == "__main__":
    query = input("Enter your question")
    for value in get_contents_from_query(query, link_num=MAX_SEARCH_LINKS):
        print(value)
