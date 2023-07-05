# Shopping

An AI that uses K-Nearst Neighbor model to train and predict if users will buy the product.

[Full Project on Harvard's website](https://cs50.harvard.edu/ai/2020/projects/4/shopping)

## Overview
* The Project is about using the provided data to train a nearest-neighbor classifier that would let us know if the user is going to purchase
* The provided data set has certain evidence attributes like <code>Administrative</code>, <code>Informational</code>, etc. Those attributes constitute <code>evidence</code> that we use to train model
* The data also has <code>Revenue</code> which indicates if the user bought something
* We first parse the data to buffer in <code>load_data</code>, then we use it to train model with scikit-learn's <code>KNeighborsClassifier</code>
* Finally, we need to benchmark the model
    * For this we use the understanding of <code>sensitivity</code>, 
  that is the proportion of actual positive results to accurately predicted results, and <code>specificity</code>, 
  which is the proportion of actual negative results to accurately predicted results
    * In other words, we compare positive actual information to positive predicted values and negative actual information to negative predicted values.
  
## Files

The `shopping.csv` file contains all the data regarding over 10k users, feel free to view them in Microsoft Excel, Google sheets or a text editor. The `shopping.py` file contains the loading of data, the training of the model and the predictions along with its evaluation

## How to Use

Make sure `scikit-learn` is installed on your device, if not, use the command

`pip install scikit-learn`

In the `shopping` directory, run the command

`python shopping.py shopping.csv`

Where the `shopping.csv` is the data file. Feel free to add more data files

## Example Output

```shell
$ python shopping.py shopping.csv
Correct: 4088
Incorrect: 844
True Positive Rate: 41.02%
True Negative Rate: 90.55%
```
