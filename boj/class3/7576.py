"""
토마토
# BFS # 그래프 # 최단 경로
"""
import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split()) # M 가로, N 세로
tomato = []

# 토마토 상자 그리기
for _ in range(N):
    tomato_data = list(map(int, input().split()))
    tomato.append(tomato_data)

# 익은 토마토 위치 찾기
q = deque()
for y in range(N):
    for x in range(M):
        if tomato[y][x] == 1:
            q.append((x, y))

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and tomato[ny][nx] == 0:
                tomato[ny][nx] = tomato[y][x] + 1
                q.append((nx, ny))

# 결과 검사
def solution():
    res = 0
    for row in tomato:
        for val in row:
            if val == 0:
                return -1
            elif val > res:
                res = val
    return res - 1

bfs()
print(solution())
