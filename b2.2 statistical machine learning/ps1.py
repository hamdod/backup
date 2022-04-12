import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy.linalg import eigh # eigendecomposition
from numpy.linalg import svd # SVD
# Load the crabs dataset

crabs = pd.read_csv('crabs.csv')
X = crabs[['FL', 'RW', 'CL', 'CW', 'BD']]
S = np.cov(X)
