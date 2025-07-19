"""
숫자 카드 2

맵 객체 대신 리스트로 변환하면 여러번 참조할 수 있어 더 안정적임
리스트 컴프리헨션을 이용하는게 print() 호출을 반복하지 않으므로 더 빠름
"""
# 카운터 내장 함수 이용
from collections import Counter
n = int(input())
n_list = map(int, input().split())

count = Counter(n_list)

m = int(input())
m_list = map(int, input().split())
for value in m_list:
    print(count[value], end=" ")

# 리스트 반환, 리스트 컴프리헨션 사용으로 속도 업
from collections import Counter
N = int(input())
n_list = list(map(int,input().split()))

M = int(input())
m_list = list(map(int,input().split()))

cnt = Counter(n_list)

res = [cnt[i] for i in m_list]
print(" ".join(map(str, res)))
