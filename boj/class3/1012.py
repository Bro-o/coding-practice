"""
유기농 배추
# 그래프

"""
import sys
input = sys.stdin.readline

# BFS
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    matrix[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < N and 0 <= ny and ny < M and matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0
    return

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                bfs(i, j)
                cnt += 1
    
    print(cnt)

# DFS
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if matrix[x][y] == 1:
        matrix[x][y] = 0
        
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        
        return True
    return False

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                cnt += 1
    
    print(cnt)