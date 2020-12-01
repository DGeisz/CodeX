# Multi CompSpec

In this case, the multi is for multiple competition, not multiple layers.  In this network, we 
basically have many different competitions occuring.  Basically, every single neuron is competing
with a set of "inhibitory synapses," and it updates if its value surpasses the values of the 
inhibitions.  This is to provide more robust network activations to different inputs, which should
hopefully increase classification accuracy.

**Edit**: I temporarily halted this project later on 11/30/2020 because I saw looming computational complexity
on the horizon, and because I had a bit of an epiphany about natural competition.