# Reductionist Quasi-isomorphisms (RQI)

### Overview
I'm really being somewhat difficult with this name.  The EMT in this topic basically
pertain to dimensionality reduction.  However, I don't like the name dimensionality reduction.
It makes me think of finding some map between real numbers.  What I'm really interested in
is finding an isomorphism between some set of states that requires a certain amount of 
information to specify a specific state, and another such set that requires a smaller amount
of information to specify a state.  That's essentially what dimensionality reduction is doing
but with some multi-dimensional set of real numbers.  The reason I call it a quasi-isomorphism is
that you can't expect to find a perfect isomorphism between two of the aforementioned sets,
so what you want instead is the mapping that is as close to an isomorphism as possible.  To get 
technical, you need to define a loss function between a particular state and a predicted
state, and then find the mapping between sets that minimizes that loss function.  The loss
function should obviously behave as you would expect (it's zero if the states are equal, and gets
larger the "further" the states are apart).

Why do I care about this?  If you can find a good quasi-isomorphism, then you've essentially
captured the essence of an input with a small amount of information, which allows you to understand
and find correlations to other related data with greater ease.  This is essential for complex information
processing required for consciousness.

## Table of Contents
1. [11_18_2020_metric_mnist_competitive_classification](11_18_2020_metric_mnist_competitive_classification)
2. [11_19_2020_experiment_prototype_ae](11_19_2020_experiment_prototype_ae)
3. [11_20_2020_experiment_competitive_ae](11_20_2020_experiment_competitive_ae)
4. [11_20_2020_metric_mnist_collaborative_classification](11_20_2020_metric_mnist_collaborative_classification)
5. [11_20_2020_experiment_collaborative_ae](11_20_2020_experiment_collaborative_ae)
6. [11_23_2020_experiment_multi_layer_collab_ae](11_23_2020_experiment_multi_layer_collab_ae)
