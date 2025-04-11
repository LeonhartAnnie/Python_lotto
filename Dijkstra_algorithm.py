import heapq
#transfer edges to graph
def build_graph(edges):
    graph = {}
    for dist, u, v in edges:
        graph.setdefault(u, []).append((v, dist))
        graph.setdefault(v, []).append((u, dist))  # 如果是無向圖
    return graph

#initial
def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        if u == end:
            break
        for v, weight in graph.get(u, []):
            alt = current_dist + weight
            if alt < distances[v]:
                distances[v] = alt
                previous[v] = u
                heapq.heappush(pq, (alt, v))
    
    # 回溯最短路徑
    path = []
    u = end
    while u is not None:
        path.insert(0, u)
        u = previous[u]
    
    return distances[end], path
