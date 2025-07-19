"""
수 찾기

해시를 이용해서 딕셔너리에 넣어서 풀었는데 그냥 리스트에서 파이썬 in 연산자로 찾는게 더 빠름
"""
# 해시 인덱스로 딕셔너리 삽입
from collections import defaultdict
n = int(input())
sample = map(int, input().split())
dict = defaultdict(list)
for value in sample:
    index = hash(value) % n
    dict[index].append(value)

m = int(input())
data = map(int, input().split())
for value in data:
    index = hash(value) % n
    if value in dict[index]:
        print("1")
    else:
        print("0")

# 파이썬 in 연산자
import sys
n = int(sys.stdin.readline())
ns = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
ms = list(map(int, sys.stdin.readline().split()))

for i in ms:
    if i in ns:
        print('1')
    else:
        print('0')