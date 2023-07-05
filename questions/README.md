# Questions

An AI that replies to queries using tf-idf.

[Full Project on Harvard's website](https://cs50.harvard.edu/ai/2020/projects/6/questions)

## Overview
* The project is about using the provided texts to answer questions based on the concept of Inverse Document Frequency
* Given a number of txt files, we first parse them into the memory by tokenizing each sentence into a list of words
* We then use the parsed words to compute IDF, which is a measure of how common or rare a word is across all files
* When the user asks a question, the question is tokenized and each word is used to determine which of the files contains the answer by comparing IDF
    * Having determined the file, the sentences in the file are then ranked according to their highest IDF value as it related to the words in the question
  
## Files

In the `corpus` directory, there are some documents from wikipedia which contains some information for the AI to use. One can add more information to this directory to expand the functionality of the Q&A AI. In the `questions.py`, the AI reads from the documents, tokenize files and sentences, then use tf-idf to calculate the importance of certain words, reply the users' queries with the most relevant sentence

## How to Use

Make sure `nltk` is installed, if not, use the following command

`pip install nltk`

In the `questions` directory, run the command

`python questions.py corpus`

Then enter some query as prompt to get a reply from the AI

## Example Output

```shell
$ python questions.py corpus
Query: What are the types of supervised learning?
Types of supervised learning algorithms include Active learning , classification and regression.

$ python questions.py corpus
Query: When was Python 3.0 released?
Python 3.0 was released on 3 December 2008.

$ python questions.py corpus
Query: How do neurons connect in a neural network?
Neurons of one layer connect only to neurons of the immediately preceding and immediately following layers.
```
