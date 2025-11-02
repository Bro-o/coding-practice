"""
N과 M (2)

"""

n, m = map(int, input().split())
num = []

def dfs(now):
    if len(num) == m:
        print(' '.join(map(str, num)))
        return
    
    for i in range(now, n+1):
        if i not in num:
            num.append(i)
            dfs(i+1)
            num.pop()

dfs(1)