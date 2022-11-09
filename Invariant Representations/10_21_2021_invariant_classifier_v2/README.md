# Invariant Classifier V2

They thought I was dead! They thought I had disappeared into the ether! Negative, bitches! I'm back baby! I've been meditating on sparse networks and invariant networks for nine fucking months, and it's time to get these bitches to run.

In this experiment, I'm reviving the MNIST classifier, but I'm going to train the invariant layer and the sparse layer separately from the classification layer.  I think that's probably the only way.  Basically the insight here is that you can think of the classification as an invariant layer with a single "winner," so that should correspond with a WTA layer.  

Last time, I trained the WTA layer in an unsupervised fashion, so I think it learned a bunch of features that weren't at all close to actual digits, thus harming training accuracy. We'll see what I can cook up with the present architecture.