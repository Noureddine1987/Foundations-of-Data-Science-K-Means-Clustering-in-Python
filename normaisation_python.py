# normalise matrix

import matplotlib.pyplot as plt
import numpy as np
xyz = [[10, 125], [100, 26], [25, 66], [67, 1], [74, 10]]
print(xyz)
xyz = np.array(xyz)
print(xyz)
print('first line : ', xyz[:, 0])
print('first column : ', xyz[:, 1])
x_min = np.min(xyz[:, 0])
x_max = np.max(xyz[:, 1])
print('min = ', x_min, '\nmax = ', x_max)

# min & max from the whole matrix by column ( np.min(xtz, 0)
x_min2 = np.min(xyz, 0)
print('min vector :', x_min2)
x_max2 = np.max(xyz, 0)
print('max vector :', x_max2)

# normalisation
normed_x = (xyz - x_min2) / (x_max2 - x_min2)
print(normed_x)

# plot normalised data
normed_min = np.min(normed_x, 0)
normed_max = np.max(normed_x, 0)

# mean & std deviation of normed data
mean_normed = np.mean(normed_x, 0)
std_normed = np.std(normed_x, 0)
print('normed mean : ', mean_normed)
print('normed std : ', std_normed)

# plot them : normed data, mean, std
fig, graph = plt.subplots()
graph.scatter(normed_x[:, 0], normed_x[:, 1])
graph.scatter(std_normed[0], std_normed[1])
plt.scatter(mean_normed[0], mean_normed[1])
plt.show()

# are items which fall too far outside of the distribution to be taken as meaningful values
# lying outside of the central area there
