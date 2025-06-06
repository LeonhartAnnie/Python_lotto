import Dijkstra_algorithm

# 讀取邊資料 
edges = set()

with open("edge.txt", "r") as f:
    for line in f:
        if not line.strip():  # 忽略空行
            continue

        parts = line.strip().split(".", 1)  # 最多只分割一次，避免多個小數點出錯
        if len(parts) < 2:
            continue  # 略過格式錯誤的行

        content = parts[1].strip()
        if content.startswith("(") and content.endswith(")"):
            content = content[1:-1]  # 去掉括號

        edge_parts = [p.strip() for p in content.split(",")]  # 去除空白
        if len(edge_parts) != 3:
            print(f"格式錯誤：{line.strip()}")
            continue

        try:
            weight = float(edge_parts[0])
            node1 = int(edge_parts[1][1:])
            node2 = int(edge_parts[2][1:])
        except ValueError as e:
            print(f"轉換錯誤：{line.strip()} → {e}")
            continue

        edge = tuple(sorted((node1, node2)))
        edges.add((weight, edge[0], edge[1]))

graph = Dijkstra_algorithm.build_graph(edges)
dist, path = Dijkstra_algorithm.dijkstra(graph, start=0, end=50)
print("最短距離：", dist)
print("路徑：", path)
