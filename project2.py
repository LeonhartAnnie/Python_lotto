import random 
import matplotlib.pyplot as plt 
import numpy as np 
from scipy.spatial import Delaunay 
import math 
# 定義空間範圍與參數 
SPACE_SIZE = 1000 
NUM_NODES = 100 
NUM_EDGES = 200 
random.seed(10)  

# 生成節點 
nodes = [(random.randint(0, SPACE_SIZE), random.randint(0, SPACE_SIZE)) for _ in range(NUM_NODES)] 
nodes = sorted(nodes, key=lambda point: point[0]**2 + point[1]**2) 

# 進行 Delaunay 
points = np.array(nodes) # 轉換為 NumPy 陣列 
tri = Delaunay(points) # 執行三角剖分 

# 添加 Delaunay 邊 
edges = set() 
for simplex in tri.simplices: 
    for i in range(3):  # 每個 simplex 有 3 個點 
        for j in range(i + 1, 3): 
            p1, p2 = sorted((simplex[i], simplex[j])) 
            dist = math.sqrt((points[p1][0] - points[p2][0])**2 + (points[p1][1] - points[p2][1])**2)
            edges.add((dist, p1, p2))  # 儲存 (距離, 點1, 點2)
# 按邊長排序，選擇最短的 MAX_EDGES 條 
edges = sorted(edges)[:200] 

#寫入txt
with open("node.txt", "w") as node_file: 
    for i, (x, y) in enumerate(nodes): 
        node_file.write(f"n{i}.({x},{y})\n") 

with open("edge.txt", "w") as edge_file: 
    for i, (dist, node1, node2) in enumerate(edges): 
        edge_file.write(f"e{i}.({dist},n{node1},n{node2})\n")

plt.figure(figsize=(8, 8))

# 繪製節點
x_coords = [node[0] for node in nodes]     # 取出所有 x 坐標
y_coords = [node[1] for node in nodes]     # 取出所有 y 坐標
plt.scatter(x_coords, y_coords, c='blue')

for i, (x, y) in enumerate(nodes):
    plt.text(x + 5, y + 5, f'n{i}', fontsize=8, color='red')
    
# 繪製邊
for edge in edges:
  dist, node1, node2 = edge
  x_values = [nodes[node1][0], nodes[node2][0]]
  y_values = [nodes[node1][1], nodes[node2][1]]
  plt.plot(x_values, y_values, c='gray', alpha=0.5)

# 繪製
plt.title("Graph Visualization")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.grid(True)
plt.show()

