"""
ATM
"""
n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
res = 0
for i, time in enumerate(n_list):
    res = res + time * (n - i)

print(res)