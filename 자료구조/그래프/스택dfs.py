graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]} #무방향 그래프
graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]}                 #방향 그래프

def dfs(graph, node):
    res = []
    stack = [node]
    visited = set(stack)

    while stack:
        u = stack.pop()
        res.append(u)

        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    return res

print("무방향 그래프의 깊이 우선 탐색")
print("==========================")
print("노드 1에서 시작: ", dfs(graph1, 1))
print("노드 2에서 시작: ", dfs(graph1, 2))
print()
print("방향 그래프의 깊이 우선 탐색")
print("========================")
print("노드 1에서 시작: ", dfs(graph2, 1))
print("노드 2에서 시작: ", dfs(graph2, 2))