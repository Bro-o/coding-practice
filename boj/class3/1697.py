"""
숨바꼭질
# 그래프 # bfs
위치는 범위 안에 있어야함
최소 경로를 출력해야하므로 카운트 한적이 없는 그 처음을 기록해놔야함. 업데이트 안되도록
"""
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

MAX = 10 ** 5
move_count = [0] * (MAX + 1)

q = deque()
q.append(n)

while q:
    x = q.popleft()
    if x == k:
        print(move_count[x])
        break
    
    for next_x in (x-1, x+1, x*2):
        if 0 <= next_x and next_x <= MAX and not move_count[next_x]:
            move_count[next_x] = move_count[x] + 1
            q.append(next_x)
