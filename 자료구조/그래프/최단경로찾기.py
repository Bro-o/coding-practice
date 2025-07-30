graph = {
    "A": [("B", 1), ("C", 4), ("D", 5)],
    "B": [("A", 1), ("D", 2)],
    "C": [("A", 4), ("D", 4), ("E", 3)],
    "D": [("A", 5), ("B", 2), ("C", 4), ("F", 3)],
    "E": [("C", 3), ("F", 2)],
    "F": [("D", 3), ("E", 2)]
}

node_from = {node: "" for node in graph}

def bfs(graph, node):
    res = []
    q = [node]
    visited = set(q)

    while q:
        u = q.pop(0)
        res.append(u)

        for v in graph[u]:
            if v not in visited:
                node_from[v] = u
                visited.add(v)
                q.append(v)
    return res

print("탐색 전의 node_from의 상태")
print(node_from)
print()
print("너비 우선 탐색 결과: ", bfs(graph, "A"))
print()
print("탐색 후의 node_from의 상태")
print(node_from)