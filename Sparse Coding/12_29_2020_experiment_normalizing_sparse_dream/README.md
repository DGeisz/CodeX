# Normalizing SparseDream

As much as I learned to hate weighted averages, I think I need them.  Basically, I need my network to be linear, but I also need it to have the behavior I've learned to love.  Ie, it needs to not break cataclysmically every single time it is run.

So I'm going to experiment with a couple flavors of weighted averages, and see what works.