"""
N과 M(9)
"""

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

num = []
visited = [0] * (n+1)

def dfs():
    if len(num) == m:
        print(' '.join(map(str, num)))
        return

    prev = 0
    for i in range(n):
        if visited[i] == 0 and arr[i] != prev:
            num.append(arr[i])
            visited[i] = 1
            prev = arr[i]
            dfs()
            visited[i] = 0
            num.pop()

dfs()