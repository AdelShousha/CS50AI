# Degrees

A program that determines how many "degrees of separation" apart two hollywood actors are. Each degree consists of a film that two actors both starred in.

[Full Assignment on Harvard's website](https://cs50.harvard.edu/ai/2020/projects/0/degrees)

## Overview
* The assignment is about finding the shortest path between two nodes
* The database comes from IMDb, and the task is to tell how one actor is connected to another through their common movie casts
* The solution is based on Breadth-First Search (BFS) because the task requires the shortest path between nodes
* To implement the search, I used a Queue-based Frontier. The Frontier is filled with neighboring nodes that share the same parameter(movie)

## Files

There are two sets of data, one in `small` folder and another in `large` folder. Both contain three csv files, `people.csv`, `movies.csv` and `stars.csv`. Data in `small` folder is relatively tiny in size comparing to the data in `large` folder so it can be used to test the functionality of the program. Whereas in the `large` folder, all the data from IMDb's database is in the csv files <br/>

- `Movies.csv` contains information each movie's assigned ID, its title and release year
- `People.csv` contains information about each hollywood movie star's unique ID, corresponding to their ID in the IMDb's database, with their name and birth year
- `Stars.csv` establishes a relationship between the movie stars in the `people.csv` and movies in `movies.csv`, stating that which person starred in which movie

The main program is written in the `degrees.py` file, which utilizes some useful classes and functions in the `util.py` file

## How to Use

In the `degrees` directory, run the command

`python degrees.py dataset`

Where dataset is the name of the dataset folder

If you are using the large dataset, it will take some time for the data to load in. Then enter the hollywood movie star names as the program prompts, wait a bit for the program to search, and you will see the results

## Example Output

```shell
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

## Acknowledgements

Information courtesy of [IMDb](https://www.imdb.com/). Used with permission.
