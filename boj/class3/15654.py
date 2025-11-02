"""
N과 M (5)

"""

n, m = map(int, input().split())

arr = list(map(int, input().split()))
num = []

arr.sort()

def dfs():
    if len(num) == m:
        print(' '.join(map(str, num)))
        return

    for i in range(0, n):
        if arr[i] not in num:
            num.append(arr[i])
            dfs()
            num.pop()

dfs()