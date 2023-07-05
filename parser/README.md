# Parser

An AI that recognizes sentence structures/syntax/grammar.

[Full Project on Harvard's website](https://cs50.harvard.edu/ai/2020/projects/6/parser)

## Overview
* The Project is about parsing a sentence to determine its structure
* First, the task requires pre-processing the sentence to convert it into a list of words
* Second, the task requires a set of context-free grammar rules on how sentences can be structured (the most challenging part)
    * Building a set of rules that would let us to parse all sentences took me a few hours
    * I was able to derive that all 10 sentences divide into two types,
        * a sentence that starts with a noun phrase and ends with a verb (adverbs can be after or before the verb)
        * a sentence that starts with another sentence (the first type) and ends with a conjunction in front of a verb or another sentence

* Third, the task requires a list of noun phrase chunks, which is a noun phrase that does not have other noun phrase within it
    * The context-free grammar rules used in our case do not allow such cases, so it is reasonable to just count the number of noun phrases ([nltk.tree](https://www.nltk.org/_modules/nltk/tree.html) documentation is really helpful)
## Files

In `sentences` directory, there are 10 different pre-defined sentences as txt files, each with a different syntax. One is welcome to add more sentences as txt files to test the functionality of the AI. In the `parser.py` file, the AI use the [nltk (natural language tool kit)](https://www.nltk.org/) and some customized context free grammars to recognize the sentence structures. Feel free to add more words to the non-terminal variable to expand the functionality of the AI

## How to Use

Make sure `nltk` is installed, if not, use the following command

`pip install nltk`

In the `parser` directory, run the command

`python parser.py sentences/.txt`

Where the `sentences/.txt` is an optional argument, if not provided, the AI will take user input

## Example Output

```shell
        S
   _____|___
  NP        VP
  |         |
  N         V
  |         |
holmes     sat
```
