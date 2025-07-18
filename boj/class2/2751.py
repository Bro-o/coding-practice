import sys
input = sys.stdin.readline

n = int(input())

num_in = []
for i in range(n):
    num_in.append(int(input()))

num_in.sort()

for i in range(n):
    print(num_in[i])