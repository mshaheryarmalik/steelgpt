from typing import List
from bs4 import BeautifulSoup
import requests
from googlesearch import search


def get_google_links(query, num_results=10):
    results = []
    for j in search(query, num_results=num_results):
        results.append(j)
    return results


def fetch_link(link: str):
    response = requests.get(link)
    if response.status_code == 200:
        return response.text
    return None


def get_google_query_link(query) -> List[str]:
    formatted_query = "+".join(query.split())
    return f"https://www.google.com/search?q={formatted_query}&num=100"


def get_link_content(link: str, recursive: int = 0) -> List[str]:
    try:
        results = []
        link_text = fetch_link(link)
        if link_text:
            soup = BeautifulSoup(link_text, "html.parser")
            results.append(
                {"source": link, "content": " ".join(soup.get_text().split())}
            )
            if recursive:
                result_links = soup.select(".tF2Cxc")
                print(result_links)
                for link in result_links:
                    results.append(*get_link_content(link, recursive=recursive - 1))
                    # print(link.get("href"))
            result_links = soup.select(".tF2Cxc")
            return results
    except Exception as e:
        print(f"Error processing URL: {link}")
        print(f"Error details: {e}")
    return []


def scrape_query(query):
    links = get_google_links(query)
    results = list()
    for link in links:
        contents = get_link_content(link)
        for content in contents:
            title = content["content"][:50] if len(content["content"]) > 0 else ""
            entry = {
                "title": title,
                "query": query,
                "url": link,
                "content": [content["content"]],
            }
            results.append(entry)
    return results
