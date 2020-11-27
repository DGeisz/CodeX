#CompSpec Infilteration

The proper name should be CompSpec Input Filter Network.  But I like that Infilteration sounds
like infiltration.  Makes it seem all cool and top-secret :)  

In any event, put in a very high level manner, this network filters the synapse weights with
the input vector before calculating the dot product between the input, and the weight prototype
vector.  I think this might give CompSpec networks the "or-gate" capability I so very much 
want to see in my networks, which would allow each neuron to be activated by a wider variety 
of inputs.  It would also allow the network to find correlations between a variety of related
inputs, rather than a single prototype.

I don't think I'm really going to put this network up against different metrics, I just want 
to be sure the weights are actually training in a coherent manner. By that, I mean that the 
weights prototypes are stabalizing over time and not going bat-shit crazy, which has happened
before with this type of network.

If this works, then we be really boolin' bois.
