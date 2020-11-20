# MNIST Collaborative Classification Metric

### Code
**Repo**: https://github.com/DGeisz/MNIST-Competive-Classification-Metric/tree/collaborative  
**Branch**: collaborative

### Purpose  
The purpose of this metric is to quantify how well a particular algorithm has captured the essence 
of a dataset, specifically the MNIST dataset.  This metric is quite similar to [this previous](../11_18_2020_metric_mnist_competitive_classification)
metric, but it doesn't depend on neurons racking up "wins" on different inputs.  For collaborative networks, 
the neurons aren't trying to recreate the entirety of the network.  They're instead selectively attuned to 
different aspects of the input data.  So this metric measures how much each neuron responds to each
classification of digit, and during the classification phase, it takes a weighted sum of each neuron's classification
response vector and weights it with the output of the neuron to a given input.  This way, the neurons can collaborate
to classify an input in the same way as they collaborate to reconstruct an input.   


### Methodology
After the network is trained, the network is passed through the dataset one final time.  This time it sums
the total activation of each neuron for each classification type.  So the classification vector for
a given neuron may be something like (12.3, 20.7, 23.3, 1.0, 0.2, 0.34, 245.3, 2.3, 7.5).  So each 
component is the accumulated activation of each neuron after a pass through the dataset.

The algo then sums the classification vectors of all the neurons to get a vector of total activations.

To classify and image, each neuron weights its classification vector with its activation measure in response
to the new image.  This weighted sum vector is divided component-wise by the vector of total activations.
The index of the resulting vector with the highest value is taken to be the network's prediction of
the classification of the current input.