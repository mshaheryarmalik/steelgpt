from typing import Dict, List

from .utils import get_google_links, get_link_content


def get_contents_from_query(query: str, link_num=10) -> List[Dict[str, str]]:
    """
    This function will return the contents from the query
    :param query: The query to search for
    :return: List of contents
    """
    for link in get_google_links(query, link_num):
        link_contents = get_link_content(link, 0)
        if len(link_contents):
            yield link_contents[0]
