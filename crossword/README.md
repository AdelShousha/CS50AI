# Crossword

An AI that solves crossword puzzles using given structure and words files.

[Full Project on Harvard's website](https://cs50.harvard.edu/ai/2020/projects/3/crossword)

## Overview
* The project is about solving a crossword using backtracking search that incorporates arc and node consistency
* We are given three crossword grids and three word collections 
* The <code>generate.py</code> consists of a class that implements Variable and Crossword classes from <code>crossword.py</code>
    * It provides some base methods, but there rest (starting with <code>enforce_node_consistency</code>) had to be implemented
  
* To implement the backtracking search, the assignment of words to grid variables first had to be consistent in nodes and edges (arcs)
    * Node consistency is a unary constraint that requires all grid variables to only have potential words that are of the same length (grid variable of size 4 cannot fit word "Hello")
    * Arc consistency is a binary constraint that requires all grid variable to only have potential words that are unique from other variables and are consistent in terms of characters (grid variable has to have one identical character with another variable if they share a grid cell)
## Files

The `data` directory contains the structure and words files for the crossword puzzles, one is welcome to add more data files to this directory to test the functionality or just for fun. The `crossword.py` file has two classes, `variable` and `crossword` to help solving the crossword puzzles. The main solving functions are in the `generate.py` file. In this file, main function takes arguments form command line and decide which structure and words files to use and call the solve function which uses other helper functions in the file

## How to Use

In the `crossword` directory, run the command

`python generate.py data/structure.txt data/words.txt output.png`

Where `structure` and `words` are txt files in the `data` directory, one can use the existing 0-2 files or create their own files. The program will also save a png of the solved crossword puzzle

## Example Output

```shell
$ python generate.py data/structure1.txt data/words1.txt output.png
██████████████
███████M████R█
█INTELLIGENCE█
█N█████N████S█
█F██LOGIC███O█
█E█████M████L█
█R███SEARCH█V█
███████X████E█
██████████████
```

<p align="center">
<img src="https://user-images.githubusercontent.com/99038613/176724983-d23252a0-73cc-41b1-981e-0a2575e66327.jpg" width="60%" height="60%">
</p>
