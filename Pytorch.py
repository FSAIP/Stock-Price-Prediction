import torch
a = torch.FloatTensor(10, 20)
# creates tensor of size (10 x 20) with uninitialized memory

a = torch.randn(10, 20)
# initializes a tensor randomized with a normal distribution with mean=0, var=1

a.size()
