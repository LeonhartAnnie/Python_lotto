from project2 import nodes
from project2 import edges
import Dijkstra_algorithm

# 讀取節點資料 
with open("node.txt", "r") as f: 
    for line in f: 
        parts = line.strip().split(".") 
        # parts[0] = n1, parts[1] = (541, 503) 
        coords = eval(parts[1].strip())	 	# 將座標字串轉為 tuple 
        nodes.append(coords) 


# 讀取邊資料 
with open("edge.txt", "r") as f: 
    for line in f: 
        parts = line.strip().split(".") 
        # parts[0] = e1, parts[1] = (n5, n56) 
        node_ids = parts[1].strip()[1:-1].split(",")	 # 去掉括號並分割 
        node1 = int(node_ids[0][1:]) 		# 取出 n5 -> 5，並轉為索引 (0-based) 
        node2 = int(node_ids[1][1:]) 		# 同上 
        edge = tuple(sorted((node1, node2))) 	# 保證邊無向性 
        edges.add(edge) 

graph = Dijkstra_algorithm.build_graph(edges)
dist, path = Dijkstra_algorithm.dijkstra(graph, start=0, end=2)
print("最短距離：", dist)
print("路徑：", path)
