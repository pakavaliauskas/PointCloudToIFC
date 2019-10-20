import sklearn
import laspy
import scipy
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn import preprocessing
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import path

# Open a file in read mode:
inFile = laspy.file.File(r'C:\Users\Pakav\Desktop\Tile_1.las')
# inFile = laspy.file.File(r'C:\Users\Pakav\Desktop\Tile_2.las')
# Grab a numpy dataset of our clustering dimensions:
dataset = np.vstack([inFile.x, inFile.y, inFile.z]).transpose()
dataset.shape 

%%time
def frange(start, stop, step):
  i = start
  while i < stop:
    yield i
    i += step
    
    #ground points grid filter
n = 100 #grid step
dataset_Z_filtered = dataset[[0]]
zfiltered = (dataset[ : , 2].max() - dataset[ : , 2].min())/1.2

print('zfiltered = ' , zfiltered)

xstep = (dataset[ : , 0].max() - dataset[ : , 0].min())/n

ystep = (dataset[ : , 1].max() - dataset[ : , 1].min())/n

for x in frange (dataset[ : , 0].min(), dataset[ : , 0].max(), xstep):
    for y in frange (dataset[ : , 1].min(), dataset[ : , 1].max(), ystep):
        datasetfiltered = dataset[(dataset[ : , 0] > x)
                             &(dataset[ : , 0] < x + xstep)
                             &(dataset[ : , 1] > y)
                             &(dataset[ : , 1] < y + ystep)]
        if datasetfiltered.shape[0] > 0:
            datasetfiltered = datasetfiltered[datasetfiltered[ : , 2] 
                                      > (datasetfiltered[ : , 2].min() + zfiltered)]
            if datasetfiltered.shape[0] > 0:
                dataset_Z_filtered = np.concatenate((dataset_Z_filtered,
                                             datasetfiltered))
print('dataset_Z_filtered shape', dataset_Z_filtered.shape)

print('Examining Point Format:')
pointformat = inFile.point_format
for spec in inFile.point_format:
    print(spec.name)

    print('Z range = ', dataset[ : , 2].max() - dataset[ : , 2].min())

print('Z max = ', dataset[ : , 2].max(), 'Z min = ', dataset[ : , 2].min())

print('Y range = ', dataset[ : , 1].max() - dataset[ : , 1].min())

print('Y max = ', dataset[ : , 1].max(), 'Y min = ', dataset[ : , 1].min())

print('X range = ', dataset[ : , 0].max() - dataset[ : , 0].min()) 

print('X max = ', dataset[ : , 0].max(), 'X min = ', dataset[ : , 0].min())

dataset = preprocessing.normalize(dataset_Z_filtered)

clustering = DBSCAN(eps=2, min_samples=5, leaf_size=30).fit(dataset_Z_filtered)

core_samples_mask = np.zeros_like(clustering.labels_, dtype=bool)
core_samples_mask[clustering.core_sample_indices_] = True
labels = clustering.labels_
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)
print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)

# Black removed and is used for noise instead.
fig = plt.figure(figsize=[100, 50])
ax = fig.add_subplot(111, projection='3d')
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
  for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
  if k == -1:
    # Black used for noise.
    col = [1, 0, 0, 1]
  class_member_mask = (labels == k)
  xyz = dataset_Z_filtered[class_member_mask & core_samples_mask]
  ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2], c=col, marker='.')
plt.title('Estimated number of cluster: %d' % n_clusters_)
plt.show()