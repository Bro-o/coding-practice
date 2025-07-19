"""
구간 합 구하기 4

완전탐색 알고리즘으로 풀면 시간 초과
누적합을 미리 구해놓고 구간합을 구한다
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_list = list(map(int, input().split()))
sum = [0]
tmp = 0

for value in n_list:
    tmp += value
    sum.append(tmp)

for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i - 1])