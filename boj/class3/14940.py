"""
쉬운 최단거리
# 그래프 # bfs
접근할 수 없는 0 칸은 0으로 출력해야함
"""
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    q = deque([(x, y)])
    res[y][x] = 0

    while q:
        current = q.popleft()
        current_x = current[0]
        current_y = current[1]
        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if land[ny][nx] == 1 and res[ny][nx] == -1:
                    res[ny][nx] = res[current_y][current_x] + 1
                    q.append((nx, ny))

    return

def find_target():
    for i in range(n):
        for j in range(m):
            if land[i][j] == 2:
                return j, i


n, m = map(int, input().split()) # n 세로, m 가로
land = [list(map(int, input().split())) for _ in range(n)]

res = [[0 if land[i][j] == 0 else -1 for j in range(m)] for i in range(n)]
x, y = find_target()
bfs(x, y)

for i in range(n):
    for j in range(m):
        print(res[i][j], end=" ")
    print()