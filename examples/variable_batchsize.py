from torchsample import TensorDataset
import torch
import numpy as np

x = torch.ones(10,1,30,30)
y = torch.from_numpy(np.arange(10))

loader = TensorDataset(x, y, batch_size=2)

xbatch, ybatch = loader.next_batch()
print(ybatch.numpy())

xbatch, ybatch = loader.next_batch(3)
print(ybatch.numpy())

xbatch, ybatch = loader.next_batch()
print(ybatch.numpy())


# SAMPLE A FIXED NUMBER OF BATCHES WITHOUT STOPPING
for i in range(1000):
    xbatch, ybatch = loader.next_batch()

# MAKE ONLY ONE PASS THROUGH THE DATA
for xbatch, ybatch in loader:
    pass