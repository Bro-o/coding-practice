"""
연결 요소의 개수
# 그래프
"""
# bfs
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = set()

def bfs(i):
    queue = deque()
    queue.append(i)
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return


for i in range(1, N+1):
    if i not in visited:
        bfs(i)
        count += 1

print(count)

#dfs
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = set()

def dfs(u):
    if u in visited:
        return
    visited.add(u)
    for v in graph[u]:
        dfs(v)
    return

for i in range(1, N+1):
    if i not in visited:
        dfs(i)
        count += 1

print(count)