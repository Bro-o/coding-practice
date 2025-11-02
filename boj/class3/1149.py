"""
RGB 거리

"""
import sys
input = sys.stdin.readline

n = int(input())
home = []

for _ in range(n):
    home.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(n)]
dp[0] = home[0]
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + home[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + home[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + home[i][2]

print(min(dp[-1]))