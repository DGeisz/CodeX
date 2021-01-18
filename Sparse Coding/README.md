# Sparse Coding

### Overview:

After the titanic failure of DreamFlow, I went back to the drawing board.  By that, I mean
I binged all the vs265 lectures.  Anyway, it looks like there are a couple of things that 
need to be explored. Sparse Coding is one of them.  I'm not a huge fan of probabilistic 
models, but I agree with Olshausen that the vision problem should be formulated in terms 
synthesis rather than analysis.  What I would like is a model that is able to anchor its
view in terms of a series of higher-order structures.  I think sparse coding is the way
to get there.

## Table of Contents:
1. [12_11_2020_experiment_exploring_sparse_coding](12_11_2020_experiment_exploring_sparse_coding)
2. [12_11_2020_experiment_sparse_collab_ae](12_11_2020_experiment_sparse_collab_ae)
3. [12_12_2020_experiment_sparse_dream_cifar](12_12_2020_experiment_sparse_dream_cifar)
4. [12_13_2020_experiment_topographic_sparse_dream](12_14_2020_experiment_topographic_sparse_dream)
5. [12_13_2020_experiment_topo_sparse_dream_mnist](12_13_2020_experiment_topo_sparse_dream_mnist)
6. [12_14_2020_experiment_sparse_dream_lat_inhibition](12_14_2020_experiment_sparse_dream_lat_inhibition)
7. [12_14_2020_experiment_topo_sparse_dream_lat_ex_in](12_14_2020_experiment_topo_sparse_dream_lat_ex_in)
8. [12_15_2020_experiment_topo_sparse_dream_hebbian_ex](12_15_2020_experiment_topo_sparse_dream_hebbian_ex)
9. [12_17_2020_experiment_sparse_dream_conserved_flow](12_17_2020_experiment_sparse_dream_conserved_flow)
10. [12_20_2020_experiment_gradient_sparse_dream](12_20_2020_experiment_gradient_sparse_dream)
11. [12_20_2020_experiment_mwta_sparse_dream](12_20_2020_experiment_mwta_sparse_dream)
12. [12_20_2020_experiment_time_series_mwta](12_20_2020_experiment_time_series_mwta)
13. [12_29_2020_experiment_normalizing_sparse_dream](12_29_2020_experiment_normalizing_sparse_dream)
14. [1_1_2021_experiment_accelerated_mwta](1_1_2021_experiment_accelerated_mwta)
15. [1_2_2021_experiment_mwta_noise](1_2_2021_experiment_mwta_noise)
16. [1_2_2021_experiment_aws_mwta](1_2_2021_experiment_aws_mwta)
17. [1_4_2021_experiment_time_series_aws](1_4_2021_experiment_time_series_aws)
18. [1_4_2021_experiment_invariant_layer](1_4_2021_experiment_invariant_layer)
19. [1_4_2021_experiment_sparse_invariance](1_4_2021_experiment_sparse_invariance)
20. [1_5_2021_smooth_sparse_invariance](1_5_2021_smooth_sparse_invariance)
21. [1_5_2021_smooth_collab_invariance](1_5_2021_smooth_collab_invariance)
22. [1_5_2021_ribbon_invariance](1_5_2021_ribbon_invariance)
23. [1_6_2021_variable_xi_invariance](1_6_2021_variable_xi_invariance)
24. [1_7_2021_gray_cifar_mwta](1_7_2021_gray_cifar_mwta)
25. [1_9_2021_gray_ciar_mwta_10x10](1_9_2021_gray_ciar_mwta_10x10)
26. [1_17_2091_threshold_sparse_coding](1_17_2091_threshold_sparse_coding)

### Notes:
I think I messed up the dates on experiments 11 and 12.  12 should be on 12/29.  Not that it matters much.