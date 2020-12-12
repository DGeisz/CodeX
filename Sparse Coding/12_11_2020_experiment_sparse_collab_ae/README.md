# Sparse Collaborative AE

Well, during my first exploration of sparsity (which happened within the last half hour)
I quickly began falling into the same traps I know and love.  I implemented Foldiak's 
network, and guess what happened?  The equivalent of an army of fuzzy threes walked in
single-file past my face, each dutifully pissing on me as they passed.

Why did this happen?  Oh, I don't know.  Maybe because learning wasn't based on 
reconstruction, and I was treating all the neurons exactly the same on every loop?  
Yeah, that sounds about right.  Anyway, I'm going to try to sparsify the one architecture
I've built that naturally learns different weight prototypes: The collaborative AE.

