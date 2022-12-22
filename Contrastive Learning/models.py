from torch import nn
import torchvision
import torch


def off_diagonal(x):
    # return a flattened view of the off-diagonal elements of a square matrix
    n, m = x.shape
    assert n == m
    return x.flatten()[:-1].view(n - 1, n + 1)[:, 1:].flatten()

mini_del = 0.0001

def matrix_sqrt(M):
  vals, vecs = torch.linalg.eigh(M)
#   if min_val < 0:
#     if abs(min_val) > mini_del:
#         print(f'Small eigenvalues are exploding! {min_val}')
#     vals -= min_val
  new_vals = vals + mini_del

  return vecs @ torch.diag(new_vals ** .5) @ vecs.T

class BarlowTwins(nn.Module):
    def __init__(self, batch_size, use_sqrt):
        super().__init__()
        # self.lam = 0.0051
        self.lam = 1
        self.batch_size = batch_size
        self.use_sqrt = use_sqrt

        self.name = 'good_sqrt'

        # So this is where the res net is.  Cool.
        self.backbone = torchvision.models.resnet50(zero_init_residual=True)
        self.backbone.fc = nn.Identity()

        sizes = [2048, 512]

        layers = []
        for i in range(len(sizes) - 2):
            layers.append(nn.Linear(sizes[i], sizes[i + 1], bias=False))
            layers.append(nn.BatchNorm1d(sizes[i + 1]))
            layers.append(nn.ReLU(inplace=True))
        layers.append(nn.Linear(sizes[-2], sizes[-1], bias=False))
        self.projector = nn.Sequential(*layers)

        # normalization layer for the representations z1 and z2
        self.bn = nn.BatchNorm1d(sizes[-1], affine=False)

        self.scale_model(0.03)

    def scale_model(self, alpha):
        state_dict = self.state_dict()

        for name, param in state_dict.items():
            # Don't update if this is not a weight.
            if not "weight" in name:
                continue

            # Transform the parameter as required.
            transformed_param = param * alpha

            # Update the parameter.
            param.copy_(transformed_param)
            
    def forward_reps(self, y1):
        return self.bn(self.projector(self.backbone(y1)))
    
    def cov_eig(self, y1):
        reps = self.forward_reps(y1)
        cov = (reps.T @ reps) / self.batch_size
        e_vals, _ = torch.linalg.eigh(cov)
        e_vals = e_vals.tolist()
        e_vals.sort(reverse=True)

        return e_vals

    def cov_sqrt(self, y1):
        reps = self.forward_reps(y1)

        # empirical cross-correlation matrix
        c = reps.T @ reps

        # sum the cross-correlation matrix between all gpus
        c.div_(self.batch_size)
        cov = c
        c = matrix_sqrt(c) 

        return cov, c

        
    def forward(self, y1):
        reps = self.forward_reps(y1)

        # empirical cross-correlation matrix
        c = reps.T @ reps

        # sum the cross-correlation matrix between all gpus
        c.div_(self.batch_size)

        if self.use_sqrt:
            c = matrix_sqrt(c)

        on_diag = torch.diagonal(c).add_(-1).pow_(2).sum()
        off_diag = off_diagonal(c).pow_(2).sum()
        loss = on_diag + self.lam * off_diag

        return loss
