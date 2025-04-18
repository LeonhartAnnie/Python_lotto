import math
from project2 import nodes

# 讀取節點資料 
with open("node.txt", "r") as f: 
    for line in f: 
        parts = line.strip().split(".") 
        # parts[0] = n1, parts[1] = (541, 503) 
        coords = eval(parts[1].strip())	 	# 將座標字串轉為 tuple 
        nodes.append(coords) 

print(nodes)
center = (500, 500)
radius = 100

def is_within_radius(node, center, radius):
    x, y = node
    cx, cy = center
    distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    return distance <= radius

# 找出半徑範圍內的所有節點
nodes_in_range = []

for node_id, coordinates in enumerate(nodes):
    if is_within_radius(coordinates, center, radius):
        nodes_in_range.append(node_id)

# 輸出範圍內的節點
print("半徑範圍內的節點:", nodes_in_range)