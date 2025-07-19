"""
좌표 압축

input: 2 4 -10 4 -9
output: 2 3 0 3 1
"""
import sys
input = sys.stdin.readline
n = int(input())
n_list = list(map(int, input().split()))
arr = sorted(list(set(n_list))) # [-10, -9, 2, 4]
dict = {arr[i] : i for i in range(len(arr))} # {-10: 0, -9: 1, 2: 2, 4: 3}
res = [dict[i] for i in n_list] # [2, 3, 0, 3, 1]
print(' '.join(map(str, res)))