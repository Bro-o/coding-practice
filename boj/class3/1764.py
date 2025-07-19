"""
듣보잡

in 연산의 속도는 list와 set에서 크게 차이남
list: O(n) (선형탐색)
set: O(1) (해시 탐색)

순서가 중요하거나 중복을 허용해야 할 때는 리스트 사용
존재 여부만 확인할 때는 set이 유리
"""
n, m = map(int, input().split())
n_list = set()
nm_list = []
for _ in range(n):
    n_list.add(input())

for _ in range(m):
    name = input()
    if name in n_list:
        nm_list.append(name)
    
print(len(nm_list))
nm_list.sort()
for name in nm_list:
    print(name)