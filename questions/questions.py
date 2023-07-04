import nltk
import sys
import os
import string
import math


FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = {}

    for c in os.listdir(directory):
        c_path = os.path.join(directory,c)
        with open (c_path, encoding="utf8") as f:
            files[c] = f.read()
    return files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    # if you lower all words at the beginning the result of the third test sample
    # Query: How do neurons connect in a neural network? is going to be 
    # "Neurons of one layer connect only to neurons of the immediately preceding and immediately following layers."
    # but if you lower when checking the stopwords and punctuation the result will be 
    # "How information is coded by real neurons is not known."
    
    words = [
        word.lower() for word in nltk.word_tokenize(document)  
    ]
    words = [word for word in words
             if word not in string.punctuation
             and word not in nltk.corpus.stopwords.words("english")]
    return words


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    total_documents = len(documents)

    words = {}
    for document in documents.values():
        for word in set(document):
            if word in words:
                words[word] += 1 
            else:
                words[word] = 1
    words = {key : math.log(total_documents/value) for key, value in words.items()}
    return(words)


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    f_dict = {key : 0 for key in files}

    for f in files:
        for word in query:
            tf = files[f].count(word)
            idf = idfs[word]
            f_dict[f] += tf * idf 
    sorted_dt = [key for key, value in sorted(f_dict.items(), key=lambda item: item[1], reverse = True)]

    return sorted_dt[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    s_dict = {key : 0 for key in sentences}
    s_list = []
    for s in sentences:
        for word in query:
            if word in sentences[s]:
                idf = idfs[word]
                s_dict[s] += idf
    for s in sentences:
        counter = 0
        s_words = sentences[s]
        for word in s_words:
            if word in query:
                counter += 1
        s_density = counter / len(s_words)
        s_list.append([s, s_dict[s], s_density])
    
    s_list.sort(key=lambda x: (x[1], x[2]), reverse = True)
    s_list = [s[0] for s in s_list ]
    return s_list[:n]
    

if __name__ == "__main__":
    main()
