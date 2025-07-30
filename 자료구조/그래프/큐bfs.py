graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]} #무방향 그래프
graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]}                 #방향 그래프

def bfs(graph, node):
    res = []
    q = [node]
    visited = set(q)

    while q:
        u = q.pop(0)
        res.append(u)

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
    return res

print("무방향 그래프의 너비 우선 탐색")
print("==========================")
print("노드 1에서 시작: ", bfs(graph1, 1))
print("노드 2에서 시작: ", bfs(graph1, 2))
print()
print("방향 그래프의 너비 우선 탐색")
print("========================")
print("노드 1에서 시작: ", bfs(graph2, 1))
print("노드 2에서 시작: ", bfs(graph2, 2))
