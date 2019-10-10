# 1. Point_Cloud_to_IFC
 
 ## Construct basic IFC geometry from point clouds 

- Reading the data into memory for processing
- Segmentation of the dominant horizontal and vertical planes
- Construct the IFC geometry

Input Point Cloud (.e57; .pts; .las) --> Floor/Ceiling Segmentation --> Wall Segmentation --> IFC Construction --> Write IFC

.E57 Point Cloud transfer to PCL point cloud data structure. Use Python PCL library, Python Open3d library. Find tools which supports creating and writing IFC.

# 2. IFC_To_Point_Cloud

## Change the detection that classifies a point cloud given an existing IFC model

- Reading the IFC object bounding boxes from the file
- Using the bounding boxes to segment the point cloud by object

...

[nuoroda] github.com