"""
최소 힙

"""
import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    data = int(input())
    if data == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, data)