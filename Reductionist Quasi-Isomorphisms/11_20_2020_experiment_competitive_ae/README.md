# Competitive Auto-encoder

Having been inspired by [this](../11_18_2020_metric_mnist_competitive_classification) experiment, in this 
experiment I'm going to create an algorithm that will learn prototypes competitively, but with the clear
goal of minimizing loss in the reconstructed output.  This algo is compelling because I don't necessarily 
have to implement a hand-crafted update algorithm, but rather reconstruction loss minimization naturally
handles competitive updates.