import numpy as np
from numpy import random

for i in range(5):
    arr = np.arange(5)  # [0, 1, 2, 3, 4]
    random.seed(1)  # Reset random state
    random.shuffle(arr)  # Shuffle!
    print arr
