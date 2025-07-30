import math
import heapq

graph = {
    "A": [("B", 1), ("C", 4), ("D", 5)],
    "B": [("A", 1), ("D", 2)],
    "C": [("A", 4), ("D", 4), ("E", 3)],
    "D": [("A", 5), ("B", 2), ("C", 4), ("F", 3)],
    "E": [("C", 3), ("F", 2)],
    "F": [("D", 3), ("E", 2)]
}

def dijkstra(graph, node):
    lead_time = {node: math.inf for node in graph}
    node_from = {node: None for node in graph}

    lead_time[node] = 0
    visited = set()

    heap = []
    heapq.heappush(heap, (0, node)) # (소요시간, 노드)

    while heap:
        prev_time, u = heapq.heappop(heap)

        # 이미 방문한 노드이면 다음 노드를 꺼내고, 그렇지 않으면 방문 처리 한다.
        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph[u]:
            if(new_time := prev_time + weight) < lead_time[v]:
                lead_time[v] = new_time
                node_from[v] = u
                heapq.heappush(heap, (lead_time[v], v))

    return lead_time, node_from

def shortest_path(node_from, lead_time, start, end):
    path = ""
    node = end
    while node_from[node]:
        path = " -> " + str(node) + path
        node = node_from[node]
    return f"{str(node) + path} (cost = {str(lead_time[end])})"

lead_time, node_from = dijkstra(graph, "A")

print("A에서 다익스트라 탐색 후의 node_from과 lead_time의 상태")
print(node_from)
print(lead_time)
print()
print("A에서 F로 가는 최단 경로:", end = " ")
print(shortest_path(node_from, lead_time, "A", "F"))