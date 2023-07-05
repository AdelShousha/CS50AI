# Traffic

An AI that uses Tensorflow to train a convolutional neural network to identify which traffic sign appears in a photograph.

[Full Project on Harvard's website](https://cs50.harvard.edu/ai/2020/projects/5/traffic)

## Overview
* The Project is about using provided images to train a neural network that classifies road signs
* The images were provided by the [German Traffic Sign Recognition Benchmark](https://benchmark.ini.rub.de/?section=gtsrb&subsection=news)
* To read the images, we use [OpenCV-Python](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html), and to build the network, we use [Tensorflow Keras](https://www.tensorflow.org/guide/keras/sequential_model)
* To train the network as efficiently as possible, we applied the concepts of convolutional and pooling layers
    * A convolutional layer serves to generalize the image by using a kernel matrix to filter the image into a fewer number of pixels
    * A pooling layer serves the same purpose but through pooling one pixel out of its neighboring pixels to bring a more general view of the image. The particular type of pooling used is Max-Pooling that takes the highest pixel out of the square

## Files

The dataset is too large, therefore the `data` directory only contains the links to download them. After downloading, the `data` directory should be replaced by the downloaded folder, namely "gtsrb". The `traffic.py` file contains the main functions including loading data, getting model, training the model and evaluating the model

## How to Use

Make sure `Tensorflow`, `opencv-python` and `scikit-learn` are installed. If not, run the following command

`pip install tensorflow opencv-python scikit-learn`

In the `traffic` directory, run the command

`python traffic.py data model_filename`

Where `data` should be either gtsrb or gtsrb-small which are downloaded through the links in the `data` directory. `Model_filename` is an optional argument that will store the trained model to the specifiled path

## Example Output
### Convolutional neural network model

Firstly, I used one convolutional layer with 32 filters and (3x3) kernel, I also used (2x2) pool size max-pooling layer and one hidden layer with 128 units and 0.5 dropout. 

```
Epoch 1/10
500/500 [==============================] - 17s 32ms/step - loss: 2.3214 - accuracy: 0.3788 
Epoch 2/10
500/500 [==============================] - 15s 29ms/step - loss: 1.1432 - accuracy: 0.6588
Epoch 3/10
500/500 [==============================] - 15s 29ms/step - loss: 0.7861 - accuracy: 0.7589
Epoch 4/10
500/500 [==============================] - 14s 29ms/step - loss: 0.6321 - accuracy: 0.8038
Epoch 5/10
500/500 [==============================] - 15s 29ms/step - loss: 0.5304 - accuracy: 0.8348
Epoch 6/10
500/500 [==============================] - 14s 29ms/step - loss: 0.4697 - accuracy: 0.8485
Epoch 7/10
500/500 [==============================] - 14s 29ms/step - loss: 0.4146 - accuracy: 0.8673
Epoch 8/10
500/500 [==============================] - 14s 29ms/step - loss: 0.3871 - accuracy: 0.8758
Epoch 9/10
500/500 [==============================] - 14s 29ms/step - loss: 0.3572 - accuracy: 0.8831
Epoch 10/10
500/500 [==============================] - 15s 29ms/step - loss: 0.3381 - accuracy: 0.8888
333/333 - 3s - loss: 0.1323 - accuracy: 0.9688 - 3s/epoch - 9ms/step
```
***
Ater that, I left it one convolutional layer but changed the filters number to 48 filters and (3x3) kernel, I also changed the max-pooling layer to (3x3) pool size max-pooling layer and changed the single hidden layer units to 256 units and 0.5 dropout, the results were better but a decided to change the approach and use more layers

```
Epoch 1/10
500/500 [==============================] - 19s 36ms/step - loss: 2.2117 - accuracy: 0.4003
Epoch 2/10
500/500 [==============================] - 17s 34ms/step - loss: 0.9654 - accuracy: 0.7085
Epoch 3/10
500/500 [==============================] - 17s 33ms/step - loss: 0.6305 - accuracy: 0.8093
Epoch 4/10
500/500 [==============================] - 17s 34ms/step - loss: 0.4826 - accuracy: 0.8502
Epoch 5/10
500/500 [==============================] - 18s 35ms/step - loss: 0.3942 - accuracy: 0.8787
Epoch 6/10
500/500 [==============================] - 18s 35ms/step - loss: 0.3478 - accuracy: 0.8927
Epoch 7/10
500/500 [==============================] - 17s 34ms/step - loss: 0.2970 - accuracy: 0.9070
Epoch 8/10
500/500 [==============================] - 17s 35ms/step - loss: 0.2603 - accuracy: 0.9221
Epoch 9/10
500/500 [==============================] - 17s 34ms/step - loss: 0.2432 - accuracy: 0.9249
Epoch 10/10
500/500 [==============================] - 17s 34ms/step - loss: 0.2242 - accuracy: 0.9317
333/333 - 4s - loss: 0.1116 - accuracy: 0.9737 - 4s/epoch - 11ms/step
```
***
I added a convolutional layer with the same 48 filters and (3x3) kernel, I also added a max-pooling layer and a hidden layer with 256 units and 0.5 dropout.

```
Epoch 1/10
500/500 [==============================] - 18s 33ms/step - loss: 2.6428 - accuracy: 0.2578
Epoch 2/10
500/500 [==============================] - 16s 32ms/step - loss: 1.1350 - accuracy: 0.6376
Epoch 3/10
500/500 [==============================] - 16s 33ms/step - loss: 0.6283 - accuracy: 0.7990
Epoch 4/10
500/500 [==============================] - 16s 32ms/step - loss: 0.4210 - accuracy: 0.8657
Epoch 5/10
500/500 [==============================] - 16s 32ms/step - loss: 0.3142 - accuracy: 0.8992
Epoch 6/10
500/500 [==============================] - 16s 32ms/step - loss: 0.2381 - accuracy: 0.9247
Epoch 7/10
500/500 [==============================] - 16s 33ms/step - loss: 0.1990 - accuracy: 0.9391
Epoch 8/10
500/500 [==============================] - 16s 33ms/step - loss: 0.1752 - accuracy: 0.9452
Epoch 9/10
500/500 [==============================] - 16s 32ms/step - loss: 0.1415 - accuracy: 0.9562
Epoch 10/10
500/500 [==============================] - 18s 35ms/step - loss: 0.1262 - accuracy: 0.9610
333/333 - 3s - loss: 0.1284 - accuracy: 0.9641 - 3s/epoch - 10ms/step
```
***
the results got better so I decided to add another hidden layer with 256 units and 0.5 dropout and I made the pooling layers(2x2)
```
Epoch 1/10
500/500 [==============================] - 31s 58ms/step - loss: 1.9954 - accuracy: 0.4223
Epoch 2/10
500/500 [==============================] - 30s 59ms/step - loss: 0.4639 - accuracy: 0.8519
Epoch 3/10
500/500 [==============================] - 30s 59ms/step - loss: 0.2090 - accuracy: 0.9405
Epoch 4/10
500/500 [==============================] - 29s 58ms/step - loss: 0.1185 - accuracy: 0.9652
Epoch 5/10
500/500 [==============================] - 29s 58ms/step - loss: 0.0882 - accuracy: 0.9742
Epoch 6/10
500/500 [==============================] - 30s 60ms/step - loss: 0.0600 - accuracy: 0.9822
Epoch 7/10
500/500 [==============================] - 30s 59ms/step - loss: 0.0579 - accuracy: 0.9835
Epoch 8/10
500/500 [==============================] - 29s 58ms/step - loss: 0.0445 - accuracy: 0.9860
Epoch 9/10
500/500 [==============================] - 29s 58ms/step - loss: 0.0348 - accuracy: 0.9895
Epoch 10/10
500/500 [==============================] - 29s 59ms/step - loss: 0.0378 - accuracy: 0.9884
333/333 - 5s - loss: 0.0581 - accuracy: 0.9861 - 5s/epoch - 15ms/step
```
***
Finally I went with my last configuration, two convolutional layers with 48 filters and (3x3) kernel, I also used two (2x2) pool size max-pooling layers and three hidden layers with 256 units and 0.5 dropout.

#### 


