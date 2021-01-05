# Smooth Collaborative Invariance

This is another crack at getting the invariant layer to work properly.  This is pretty similar to the collaborative autoencoder I developed back in October, and this time, during the reconstruction step, I'm not zeroing error where the sparse layer isn't "on" because I need neurons to quickly learn what *doesn't* activate them.

Hopefully this works.