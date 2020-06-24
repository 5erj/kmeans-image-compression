import pandas as pd
import numpy as np
from findClosestCentroids import *

data = pd.read_csv('ex7data2.csv', header=None)

K = 3;
initial_centroids = pd.DataFrame(np.array([[3, 3], [6, 2], [8, 5]]), columns=['X', 'Y'])

idx = find_closest_centroids(data, initial_centroids)

print('Closest centroids for the first 3 examples: \n')

print(initial_centroids[1:3])
print('\n(the closest centroids should be 1, 3, 2 respectively)\n')


