"""
피보나치 함수
# DP
"""
T = int(input())
for _ in range(T):
    n = int(input())
    a, b = 1, 0
    for i in range(n):
        a, b = b, a+b
    print(a, b)