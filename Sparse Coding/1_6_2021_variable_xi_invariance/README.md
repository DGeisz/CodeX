# Variable Xi Invariance

Ok, here are the problems we've seen so far with invariance.  If I train on the reconstruction error for all the sparse neurons (including the ones that aren't "on"), the network trains quickly, but several sparse neurons aren't represented in the invariant neurons' prototypes.  If I only train on the reconstruction error for the neurons that are "on," the sparse layer trains *way, way, way* to slowly.  And that ain't good. 

The solution?  Basically I'm going to use a smaller `xi` for training the on the sparse neurons that aren't "on."  I think this will allow the network to train relatively quickly, but it won't completely disregard the sparse features that don't show up as frequently.

I'll probably create the tapestry and ribbon datasets, and see what happens with both. 