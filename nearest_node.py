import math
from generate_node import nodes
"""
# 取得目標節點與要找最近的幾個點
while(True):
    try:
        target_node, near_number = map(int, input("請輸入想要的節點名稱以及距離最近的幾個節點（用空格分開）：").split())
        break
    except ValueError:
        print("輸入格式錯誤！請輸入兩個整數，並以空格分開，例如：5 3")
"""
target_node = 99
near_number = 5

target_coordinate = nodes[target_node]  # 直接取出目標節點座標

print("目標節點的座標是：", target_coordinate)

# 定義計算距離的函式
def compute_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# 計算所有節點到目標節點的距離
distances = []
for node_index, coordinate in enumerate(nodes):
    if node_index != target_node:  # 排除自己
        dist = compute_distance(target_coordinate, coordinate)
        distances.append((dist, node_index))  # 存成 (距離, 節點編號)

# 按照距離排序
distances.sort()

# 取出最近的 near_number 個節點
nearest_nodes = distances[:near_number]

# 顯示結果
print(f"距離 n{target_node} 最近的 {near_number} 個節點是：")
for dist, node_index in nearest_nodes:
    print(f"節點 n{node_index}，距離：{dist:.2f}")
