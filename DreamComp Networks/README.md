# DreamComp Networks

### Overview
My first endeavors in this project are essentially reconstructions of 
[Krotov and Hopfield's](https://www.pnas.org/content/116/16/7723) competitive 
network, but key realization is that I shouldn't think about this network as trying to
do spherical learning, but rather as a collection of neurons trying to reconstruct their
inputs as well as possible. If neurons have the capability to reconstruct their 
inputs, then they basically have the capability of back-filling missing information 
based on higher level constructs.  So, to put it colloquially, filling in the parts 
based on information about the whole.  

There are several avenues I need to explore within this model. Just this morning, 
I think I came up with a method of making a collaborative network with local competition,
which I think might just be able to take apart an input vector for me.  

I also need to look into the effect of reconstruction weights on classification 
accuracy.  But now I'm essentially muttering about different projects.

This'll be an interesting one.

Oh, I should also say that I came up with the idea for DreamComp
in [this experiment.](../CompSpec%20Networks/11_30_2020_experiment_nat_comp_cookhouse)

I call it DreamComp first because of the crucial importance competition plays in 
the network, and because I had the idea that perhaps this whole process of 
back-filling information when input information isn't present is the process that
allows us humans to dream when we've "shut out sight" for a sufficiently long period of 
time.  Basically at that point, our brain could potentially back-fill information all 
the way to the optic neurons, which would allow us to "see" visions, in the same
manner that we see the world around us when our eyes are open.

##Table of Contents:
1. [12_3_2020_experiment_dream_comp_recon_weights](12_3_2020_experiment_dream_comp_recon_weights)
2. [12_3_2020_experiment_dream_flow](12_3_2020_experiment_dream_flow)