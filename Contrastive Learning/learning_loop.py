import json
import sys
import time
import math
import shutil
import os

from augs import Transform
from optimizer import LARS
from pathlib import Path

from torch import nn
import torch
import torchvision

WEIGHT_DECAY = 1E-6
EPOCHS = 1000
BATCH_SIZE = 256
LEARNING_RATE_WEIGHTS = 0.2
LEARNING_RATE_BIASES = 0.0048
WORLD_SIZE = 1
PRINT_FREQ = 25


def adjust_learning_rate(optimizer, loader, step):
    max_steps = EPOCHS * len(loader)
    warmup_steps = 10 * len(loader)
    base_lr = BATCH_SIZE / 256
    if step < warmup_steps:
        lr = base_lr * step / warmup_steps
    else:
        step -= warmup_steps
        max_steps -= warmup_steps
        q = 0.5 * (1 + math.cos(math.pi * step / max_steps))
        end_lr = base_lr * 0.001
        lr = base_lr * q + end_lr * (1 - q)
    optimizer.param_groups[0]['lr'] = lr * LEARNING_RATE_WEIGHTS
    optimizer.param_groups[1]['lr'] = lr * LEARNING_RATE_BIASES


def learning_loop(model, dataset, output_dir, delete_existing_dir=False):
    checkpoint_path = f"./checkpoint_{output_dir}/"
    checkpoint_dir = Path(checkpoint_path)

    if delete_existing_dir and os.path.isdir(checkpoint_path):
        shutil.rmtree(checkpoint_path)

    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    stats_file = open(checkpoint_dir / 'stats.txt', 'a', buffering=1)
    eigen_file = open(checkpoint_dir / 'eigen.txt', 'a', buffering=1)

    print(' '.join(sys.argv))
    print(' '.join(sys.argv), file=stats_file)

    # torch.backends.cudnn.benchmark = True

    # Create the model
    # model = nn.SyncBatchNorm.convert_sync_batchnorm(model)
    param_weights = []
    param_biases = []

    for param in model.parameters():
        if param.ndim == 1:
            param_biases.append(param)
        else:
            param_weights.append(param)
    parameters = [{'params': param_weights}, {'params': param_biases}]
    optimizer = LARS(parameters, lr=0, weight_decay=WEIGHT_DECAY,
                     weight_decay_filter=True,
                     lars_adaptation_filter=True)

    # automatically resume from checkpoint if it exists
    if (checkpoint_dir / 'checkpoint.pth').is_file():
        ckpt = torch.load(checkpoint_dir / 'checkpoint.pth',
                          map_location='cpu')
        start_epoch = ckpt['epoch']
        model.load_state_dict(ckpt['model'])
        optimizer.load_state_dict(ckpt['optimizer'])
    else:
        start_epoch = 0

    assert BATCH_SIZE % WORLD_SIZE == 0

    loader = torch.utils.data.DataLoader(
        dataset, batch_size=BATCH_SIZE,
        pin_memory=True)

    start_time = time.time()
    scaler = torch.cuda.amp.GradScaler()

    for epoch in range(start_epoch, EPOCHS):
        for step, (y1,  _) in enumerate(loader, start=epoch * len(loader)):
            y1 = y1.to("cuda")

            adjust_learning_rate(optimizer, loader, step)
            optimizer.zero_grad()

            loss = model.forward(y1)
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()
            if step % PRINT_FREQ == 0:
                stats = dict(epoch=epoch, step=step,
                             lr_weights=optimizer.param_groups[0]['lr'],
                             lr_biases=optimizer.param_groups[1]['lr'],
                             loss=loss.item(),
                             time=int(time.time() - start_time))
                start = time.time()
                print('Starting Eigen Comp')
                eigen = dict(eigenvalues=model.cov_eig(y1))
                end = time.time()
                print('Ending Eigen Comp', end - start, "sec")

                print(json.dumps(stats))

                # if eigen.eigenvalues:
                print(eigen['eigenvalues'][:5])

                print(json.dumps(eigen), file=eigen_file)
                print(json.dumps(stats), file=stats_file)

        # save checkpoint
        state = dict(epoch=epoch + 1, model=model.state_dict(),
                     optimizer=optimizer.state_dict())
        torch.save(state, checkpoint_dir / 'checkpoint.pth')
    # save final model
    torch.save(model.module.backbone.state_dict(),
               checkpoint_dir / 'resnet50.pth')
