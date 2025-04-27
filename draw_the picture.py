import matplotlib.pyplot as plt 
from matplotlib.lines import Line2D  # 創建一個虛擬的圖形，並將它添加到圖例中
from generate_node import nodes, edges  # 產生整個圖
from catch_short_distance import path
from find_center_distance import center, radius, nodes_in_range
from nearest_node import nearest_nodes, target_coordinate

def draw_all():
    plt.figure(figsize=(8, 8))
    # 繪製節點
    x_coords = [node[0] for node in nodes]     # 取出所有 x 坐標
    y_coords = [node[1] for node in nodes]     # 取出所有 y 坐標
    plt.scatter(x_coords, y_coords, c='blue', s=15, label="Nodes")

    # 繪製邊
    for edge in edges:
        dist, node1, node2 = edge
        x_values = [nodes[node1][0], nodes[node2][0]]
        y_values = [nodes[node1][1], nodes[node2][1]]
        plt.plot(x_values, y_values, c='gray', alpha=0.5)

    plt.title("Graph Visualization")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.grid(True)

def draw_short_dis():
    x_coords = [nodes[node_id][0] for node_id in path]  # 取出所有 x 坐標
    y_coords = [nodes[node_id][1] for node_id in path]  # 取出所有 y 坐標
    plt.plot(x_coords, y_coords, c='red', alpha=1, label="Shortest Path")

def draw_center_dis():
    # 取出所有 x, y 座標 (這是圓內的節點)
    x_coords = [nodes[node_id][0] for node_id in nodes_in_range]
    y_coords = [nodes[node_id][1] for node_id in nodes_in_range]
    plt.scatter(x_coords, y_coords, c='green', s=40,  edgecolor='black', label="Points in Circle")

    # 繪製紅色圓圈
    ax = plt.gca()
    circle = plt.Circle(center, radius, color='red', fill=False, linewidth=2, label="Radius 100")
    ax.add_artist(circle)

    # 在圓心畫 "×" 符號
    plt.scatter(center[0], center[1], color='red', marker='X', s=20, label="Center (500, 500)")
    ax.set_aspect('equal')

def nearest_node_numbers():
    # 取出所有節點的 ID (即 nearest_nodes 中元組的第二個元素)
    node_ids = [node_id for _, node_id in nearest_nodes]  # 用 _ 跳過距離部分，只取 node_id

    # 根據 node_ids 取得對應的 x 和 y 坐標
    x_coords = [nodes[node_id][0] for node_id in node_ids]  # 取出所有 x 坐標
    y_coords = [nodes[node_id][1] for node_id in node_ids]  # 取出所有 y 坐標

    # 繪製散點圖
    plt.scatter(x_coords, y_coords, c='orange', s=40, edgecolor='black', label="Nearest Neighbors")

    # 繪製目標節點
    x_coords = target_coordinate[0]
    y_coords = target_coordinate[1]
    plt.scatter(x_coords, y_coords, c="#00FFFF", marker='D', s=70, label="Node 99")

def main():
    draw_all()
    draw_short_dis()
    draw_center_dis()
    nearest_node_numbers()
    plt.legend(loc='lower right')  # 設定圖例顯示在右下角
    plt.show()

if __name__ == '__main__':
    main()
