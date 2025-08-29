"""
색종이 만들기
# 분할정복 # 재귀
"""

import sys

input = sys.stdin.readline

N = int(input())
paper=[list(map(int, input().split())) for _ in range(N)]

def solution(y, x, N):
    color = paper[y][x]
    for i in range(y, y+N):
        for j in range(x, x+N):
            if color != paper[i][j]:
                M = N // 2
                solution(y, x, M)
                solution(y, x+M, M)
                solution(y+M, x, M)
                solution(y+M, x+M, M)
                return
    if color == 0: # 흰색이면
        result[0] += 1
    else: # 파란색이면
        result[1] += 1


result = [0, 0] # 흰색, 파란색
solution(0, 0, N)
print(result[0])
print(result[1])