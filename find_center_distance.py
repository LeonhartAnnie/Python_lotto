import math
from generate_node import nodes

center = (500, 500)
radius = 100

def is_within_radius(node, center, radius):
    x, y = node
    cx, cy = center
    distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    return distance <= radius

# 找出半徑範圍內的所有節點
nodes_in_range = []

for node_id, coordinates in enumerate(nodes):  # ✅ 用 enumerate
    if is_within_radius(coordinates, center, radius):
        nodes_in_range.append(node_id)

# 輸出範圍內的節點
print("半徑範圍內的節點:", nodes_in_range)
