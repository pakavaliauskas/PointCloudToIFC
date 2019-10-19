import pandas as pd
import open3d as o3d
import sklearn
from sklearn.cluster import DBSCAN
import numpy as np 
from open3d import *

data = [
    (2,2,2),
    (0,2,4),
    (3,2,5),
    (2,5,7),
    (0,7,1),
    (0,5,2),
    (0,8,-1),
]  
df = pd.DataFrame(data)
df.columns = 'x y z'.split()
df

df.y.value_counts()

df[df.y == 2]

pjuvis = df[df.y == 2]
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
    (0,0,0),
    (0,1,0),
    (0,1,0),
    (0,0,0),
]
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(pjuvis.values)
# pcd.points = o3d.utility.Vector3dVector(df.values)
pcd.colors = o3d.utility.Vector3dVector(colors)
o3d.visualization.draw_geometries([pcd])
# taskai sujungiami linijomis
lines = [[2, 0], [0, 3], [2, 3]]
colors = [[1, 0, 0] for i in range(len(lines))]
line_set = LineSet()
line_set.points = Vector3dVector(pcd.points)
line_set.lines = Vector2iVector(lines)
line_set.colors = Vector3dVector(colors)
draw_geometries([line_set])