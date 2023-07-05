# Nim

An AI that uses reinforcement learning to learn from experience playing Nim with itself

[Full Project on Harvard's website](https://cs50.harvard.edu/ai/2020/projects/4/nim)

## Overview
* The Project is about training a model using Reinforcement Learning, 
  meaning AI will repeatedly play against itself and either reward itself for the right action or punish itself for the wrong action
* In particular, the concept used is Q-Learning where losing results in -1 and winning results in 1
    * The formula is <code>Q(s, a) <- Q(s, a) + alpha * (new value estimate - old value estimate)</code>, 
      where <code>Q(s, a)</code> means a reward for the state <code>s</code> and action <code>a</code>
    * <code>alpha</code> is the learning rate, which tells whether we need to make exploratory actions or not
* As you can see from the example below, it does not always result in a perfect model that never loses as it does not explore 
all possible states like Minimax, but it is much less computationally demanding

## Files

The `nim.py` file contains the definition of the Nim game itself and a NimAI that trains itself by playing the game over and over again. The `play.py` file starts the training process and the game by calling functions in `nim.py`

## How to Use

Check in the `play.py` file, the train function takes in an integer input as how many games will the NimAI train by playing with itself. Use input of 0 to play against an untrained AI and use input of 10000 to play against a well trained one. After configuring the number of training games, run this command in the `nim` directory:

`python play.py`

As a human player, one should input which pile and what amount to remove according to the prompts

## Example Output

```shell
$ python play.py
Playing training game 1
Playing training game 2
Playing training game 3
...
Playing training game 9999
Playing training game 10000
Done training

Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 5
Pile 3: 7

AI's Turn
AI chose to take 1 from pile 2.
```
