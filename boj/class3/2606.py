"""
바이러스
# 그래프 # DFS/BFS

"""
import sys
input = sys.stdin.readline
n = int(input())
edge_num = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(edge_num):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0
visited = set()

def dfs(u):
    if u in visited:
        return
    visited.add(u)
    for v in graph[u]:
        dfs(v)

dfs(1)
print(len(visited) - 1)
