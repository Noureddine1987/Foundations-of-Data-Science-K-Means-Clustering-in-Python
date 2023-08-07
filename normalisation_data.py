import matplotlib.pyplot as plt
import numpy as np
my_data = np.array([55, 67, 28, 235, 114])
print('my_data =', my_data)
x_axis = np.arange(len(my_data))
print('x_axis', x_axis)
my_mean1 = np.mean(my_data)
my_mean2 = my_data.mean()
print('mean =', my_mean1, '--', my_mean2)
my_std1 = np.std(my_data)
my_std2 = my_data.std()
print('std =', my_std1, '--', my_std2)

# normalisation : the data will now have
# a mean of 0 & std 1
my_data_normed = (my_data - my_mean1) / my_std1
print('my_data_normed :', my_data_normed)

# domain standarisation : the data points will all lie btw smallest 0 and largest one
my_data_domain_stand = (my_data - np.min(my_data)) / (np.max(my_data) - np.min(my_data))
print('my_data_domain_stand :', my_data_domain_stand)

# have a look at the y axis  for each figure
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 5))
ax1.plot(x_axis, my_data)
ax1.set_title('original data')
ax2.plot(x_axis, my_data_normed)
ax2.set_title('normed data')
ax3.plot(x_axis, my_data_domain_stand)
ax3.set_title('standarisation data ')
plt.show()





