import pandas as pd
import open3d as o3d
import sklearn
from sklearn.cluster import DBSCAN
import numpy as np 
from open3d import *

data = [
    (0,1,0),
    (0,1,4),
    (6,1,0),
    (6,1,4),
    (2,2,2),
    (0,1.5,1),
    (0,0,3),
    (0,-1,-1),
    (3,1.5,0),
    (3,1.5,4),
] 
df = pd.DataFrame(data)
df.columns = 'x y z'.split()
df

df.to_csv('duomenys.csv')

df.y.value_counts()

df[df.y == 1]

pjuvis = df[df.y == 1]
pjuvis

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(df.values)
db = DBSCAN(min_samples=1.5, eps=1)
print('cia gaunam grupes dvi grupes: 0,1. -1 yra nepriskirti jokiai grupei')
db.fit_predict(df)

colors = [
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),
    (1,0,0),   
]

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(pjuvis.values)
# pcd.points = o3d.utility.Vector3dVector(df.values)
pcd.colors = o3d.utility.Vector3dVector(colors)
o3d.visualization.draw_geometries([pcd])
# taskai sujungiami linijomis
lines = [[0, 1], [0, 2], [1, 3], [2, 3]]
colors = [[1, 0, 0] for i in range(len(lines))]
line_set = LineSet()
line_set.points = Vector3dVector(pcd.points)
line_set.lines = Vector2iVector(lines)
line_set.colors = Vector3dVector(colors)
draw_geometries([line_set])