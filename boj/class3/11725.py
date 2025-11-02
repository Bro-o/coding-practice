"""
트리의 부모 찾기
"""

import sys
input = sys.stdin.readline

N = int(input())

# 그래프 생성
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부
visited = [0] * (N+1)

# dfs - 재귀함수
sys.setrecursionlimit(10**6)

def dfs(node):
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = node
            dfs(i)

dfs(1)

for x in range(2, N+1):
    print(visited[x])

# dfs - stack
def dfs(graph, node):
    stack = [node]
    while stack:
        top = stack.pop()
        for adj in graph[top]:
            if visited[adj] == 0:
                visited[adj] = top
                stack.append(adj)
    return visited

dfs(graph, 1)

for x in range(2, N+1):
    print(visited[x])

# bfs
from collections import deque

def bfs(start):
    deq = deque([start])

    while deq:
        node = deq.popleft()

        for adj in graph[node]:
            if visited[adj] == 0:
                visited[adj] = node
                deq.append(adj)

bfs(1)
answer = visited[2:]
for x in answer:
    print(x)