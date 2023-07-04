import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    # corpus = crawl("corpus2")
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    # transition_model(corpus, "1.html", DAMPING)

def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    linked_pages = corpus[page]
    
    if len(linked_pages) == 0:
        linked_pages = corpus.keys()

    damp_prob = damping_factor / len(linked_pages) 

    prob_distribution = {key: (1-damping_factor)/len(corpus) for key in corpus}

    for page in linked_pages:
         prob_distribution[page] += damp_prob
    
    return prob_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    all_pages = list(corpus.keys())
    
    page_rank = {}
    for page in all_pages:
        page_rank[page] = 0

    prev_sample = random.choice(all_pages)

    for _ in range(n):
        model = transition_model(corpus, prev_sample, damping_factor)
        model_keys = list(model.keys())
        model_prob = list(model.values())

        sample = random.choices(model_keys, model_prob)
        for key in model_keys:
            if sample[0] == key:
                page_rank[key] += 1/n
        prev_sample = sample[0] 

    return page_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    all_pages = list(corpus.keys())
    n = len(all_pages) #number of pages
    new_ranks = {}
    accuracy = 0.001
    
    pages_ranks = {}
    for page in all_pages:
        pages_ranks[page] = 1 / n

    loop = True
    
    while loop:
        for page in all_pages:
            total = 0

            for possible_page in corpus:
                if page in corpus[possible_page]:
                    total += pages_ranks[possible_page] / \
                        len(corpus[possible_page])

                if not corpus[possible_page]:
                    total += pages_ranks[possible_page] / len(corpus)

            new_ranks[page] = (1 - damping_factor) / \
                len(corpus) + damping_factor * total
        
        loop = False

        for page in pages_ranks:
            if abs(new_ranks[page] - pages_ranks[page]) > accuracy:
                loop = True

            pages_ranks[page] = new_ranks[page]

    return pages_ranks


if __name__ == "__main__":
    main()
