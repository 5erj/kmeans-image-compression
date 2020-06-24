import pandas as pd
from findClosestCentroids import *

# Load example dataset
data = pd.read_csv('ex7data2.csv', header=None).to_numpy()

# Pick some initial centroids
K = 3
initial_centroids = np.array([[3, 3], [6, 2], [8, 5]])

# Find closest centroid for each example
idx = find_closest_centroids(data, initial_centroids)

print('Closest centroids for the first 3 examples: \n')
print(idx[0:3])
print('\n(the closest centroids should be 1, 3, 2 respectively)\n')
