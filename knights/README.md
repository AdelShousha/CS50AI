# Knights

An AI solving [Knights and Knaves](https://en.wikipedia.org/wiki/Knights_and_Knaves) logic puzzles using propositional logics

[Full Project on Harvard's website](https://cs50.harvard.edu/ai/2020/projects/1/knights)

## Overview
* The project is about solving puzzles using propositional logic
* Using given module <code>logic.py</code>, the puzzles first need to be presented
    * We first need to define base knowledge in each of the knowledge bases, such as that knaves only lie and knight only tell the truth
    * Then, given the statements of symbols (e.g. Symbol A says "We're both knaves" and Symbol B says nothing), we need to represent them using logic
        *  This case involves using biconditionals to show that if A is a knight, his words are true and if not, they are lies

## Files

There are two files, `logic.py` and `puzzle.py`. `Logic.py` has all the helper functions for us to translate human logic into AI knowledge, such as AND, OR, NOT, etc. Furthermore there are also functions to give entailments based on existing knowledge base such as the model check function. `Puzzle.py` is the actual use of all the helper functions in `logic.py`. There are four scenarios, each have its own KB. We have to determine whether each character in each scenario is a knight or a knave based on the corresponding KB. Some are easy for human to "logic" it out and some are a bit tricky, that's why AI will be better at these kinds of job since they will never make mistakes, they "algorithm" it out (otherwise blame on the programmer LOL)

## How to Use

Go into the `puzzle.py` and check the four scenarios, try to reason it out which character is a knight or a knave. Then in the `knights` directory, run the command below to see if you got it right!

`python puzzle.py`

## Example Output

```shell
Puzzle 0
    A is a Knave
Puzzle 1
    A is a Knave
    B is a Knight
Puzzle 2
    A is a Knave
    B is a Knight
Puzzle 3
    A is a Knight
    B is a Knave
    C is a Knight
```
