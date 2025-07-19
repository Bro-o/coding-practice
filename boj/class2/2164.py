"""
카드2

큐를 이용하는 방법
or
규칙을 발견해서 계산하는 방법(이게 더 빠르긴 함)
"""
# deque 사용
from collections import deque
n = int(input())
q = deque([i for i in range(1, n+1)])
res = 0

while q:
    res = q.popleft()
    if q:
        q.append(q.popleft())

print(res)

# 규칙 발견
n = int(input())
square = 2

while True:
    if(n == 1 or n == 2):
        print(n)
        break

    square *= 2
    if (square >= n):
        print((n - (square // 2)) * 2)
        break
