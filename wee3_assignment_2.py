import numpy as np

population = np.array([[1, 2, 3, 4, 5], [2, 4, 2, 5, 1], [3, 5, 1, 0, 4]])
pop_birds = population.transpose()
print('birds population : \n', pop_birds)
print('mean_population : ', np.mean(pop_birds, axis=0))
