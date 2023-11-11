import json
import logging
import itertools

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def get_content(scrape):
    return scrape["content"]


def content_to_snippets(content, window_size=6, step_size=1):
    # Turn content to sentences
    sentences = list(
        itertools.chain.from_iterable([map(str.strip, c.split(".")) for c in content])
    )
    # Filter out empty strings
    sentences = list(filter(None, sentences))
    sentence_count = len(sentences)
    logging.info(f"Sentence count: {sentence_count}")
    logging.debug(sentences)
    # Turn sentences to snippets
    snippets = list()
    for i in range(max([sentence_count - window_size, 1])):
        snippets.append(
            ". ".join(sentences[i : min([i + window_size, sentence_count - 1])])
        )
    logging.info(len(snippets))
    logging.debug(snippets)
    return snippets


def get_top_results(scrape_results, original_query):
    top_results = list()
    for scrape in scrape_results:
        print(scrape)
        content = get_content(scrape)
        query = scrape["query"]
        best_snippet = get_best_snippet(content, query, original_query)
        scrape["best_snippet"] = best_snippet
        top_results.append(scrape)
    return top_results


def get_best_snippet(content, query, original_query):
    # Turn the content into appropriately sized snippets
    logging.info("Compiling snippets")
    print(content)
    snippets = content_to_snippets(content)
    # Get TF-IDF vectors for the snippets
    logging.info("Vectorizing snippets")
    vectorizer = TfidfVectorizer()
    print(snippets)
    try:
        X = vectorizer.fit_transform(snippets)
    except ValueError:
        return ""
    # Rank the snippets based on the queries
    logging.info("Calculating similarities")
    queries = [original_query, query]
    Y = vectorizer.transform(queries)
    similarities = linear_kernel(X, Y)
    logging.debug(similarities)
    score_weights = (3, 1)
    scores = np.array(
        list(
            map(
                lambda x: (score_weights[0] * x[0] + score_weights[1] * x[1])
                / sum(score_weights),
                similarities,
            )
        )
    )
    logging.debug(scores)
    print(np.argsort(scores))
    top_results = np.flip(np.array(snippets)[np.argsort(scores)[-3:]])
    logging.info(top_results)
    return top_results[0]


def result_to_text(result):
    result_text = "\n".join([result["title"], result["best_snippet"], result["url"]])
    return result_text


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
    )
