# Heredity

An AI that assess the likelihood that a person will have a particular genetic trait.

[Full Project on Harvard's website](https://cs50.harvard.edu/ai/2020/projects/2/heredity)

## Overview
* The project is about using a bayesian network that models the relationships of getting a certain gene and make inferences about a population
* We are given information about people, who their parents are, and whether they have a trait that is caused by a gene. The AI then infers the probability distribution for each person
* The <code>heredity.py</code> has base probabilities for people who do not have parents listed.
Using those base probabilities we can make inferences for their children based on the chances they inherited zero genes, one gene, or two genes and whether they exhibit a trait

## Files

There are three datasets in the `data` directory, which are three family relationships and genetic traits.
And in the `heredity.py` file, there are some probability constants and we are to use them and the dataset to infer the probability distribution of which family member has certain genetic traits. The `testcase.py` contains a unit test test case that is provided as an example in the course's project description. One can use this to confirm the functionality of the `joint_probability` function in `heredity.py`

## How to Use

One can use either the existing data in the `data` directory or custom data. If using custom data, one should be familiar with the format of the data and added into the `data` directory. Run this command in the `heredity` directory to get the probability distribution for genetic traits

`python heredity.py data/dataname`

Where dataname is the name of the data file in the `data` directory

If one wants to run the unit test `testcase.py`, use the command

`python testcase.py`

## Example Output

```shell
$ python heredity.py data/family0.csv
Harry:
  Gene:
    2: 0.0092
    1: 0.4557
    0: 0.5351
  Trait:
    True: 0.2665
    False: 0.7335
James:
  Gene:
    2: 0.1976
    1: 0.5106
    0: 0.2918
  Trait:
    True: 1.0000
    False: 0.0000
Lily:
  Gene:
    2: 0.0036
    1: 0.0136
    0: 0.9827
  Trait:
    True: 0.0000
    False: 1.0000
```
