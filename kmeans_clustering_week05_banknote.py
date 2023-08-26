import matplotlib.pyplot as plt
import sklearn
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

data = pd.read_csv('banknote_dataset.csv')
print('dataset :\n', data)
print('#'*50)
print('data info : \n', data.info)
x = data['V1']
y = data['V2']
# Normalized data btw 0 & 1
print('#'*50)
data_values = data.values
print('data v1 \n', data_values[:, 0])
print('data v2 \n', data_values[:, 1])
print('data values : ', data_values)
xy_min = np.min(data_values, 0)
xy_max = np.max(data_values, 0)
print('#'*50, 'normalized data')
data_values = (data_values - xy_min) / (xy_max - xy_min)
print(data_values)
print('#'*50)
x = data_values[:, 0]
y = data_values[:, 1]
result = np.column_stack((x, y))
print(result)
km_result = KMeans(n_clusters=2, n_init='auto').fit(result)
clusters = km_result.cluster_centers_
print('clusters : \n', clusters)
km_res = KMeans(n_clusters=2, n_init='auto').fit(result)
labels = km_res.labels_
print('#'*50, 'labels : ')
print(np.shape(labels))
label_0 = data_values[labels == 0]
print('label_0 , count genuine :\n', label_0, len(label_0))
label_1 = data_values[labels == 1]
print('label_1', 'count forged :\n', label_1, len(label_1))
print('print data :\n', data)
# plotting
plt.scatter(label_0[:, 0], label_0[:, 1], color='red')
plt.scatter(label_1[:, 0], label_1[:, 1], color='green')
plt.scatter(clusters[:, 0], clusters[:, 1], s=1000, c='black', alpha=0.5)
plt.legend(['genuine', 'Forged'], ncol=2, loc='lower right')
plt.xlabel('v1: variance')
plt.ylabel('v2: skewness')
plt.title('variance VS skewness : banknote authentification')
plt.savefig('clusterning_kmeans_banknote.png')
plt.show()

