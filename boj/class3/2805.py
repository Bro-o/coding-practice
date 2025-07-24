"""
나무 자르기
# 이분 탐색

반복문을 일찍 탈출할 수 있을때 하기 (21, 22 line)
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2

    total = 0 # 벌목된 나무 총합
    for tree in trees:
        if tree >= mid:
            total += tree - mid
        if total > M:
            break
        
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)