n, k = map(int, input().split())
q = []
res = []

for i in range(1, n+1):
    q.append(i)

count = 1

for j in range(n-1):
    while count < k:
        q.append(q.pop(0))
        count += 1
    res.append(q.pop(0))
    count = 1
res.append(q.pop(0))

"""
차례랑 배열이 줄어드는걸 잘 적용한 예시
n, k = map(int, input().split())
q = list(range(1, n+1))
res = []
index = 0

while q:
    index = (index + k - 1) % len(q)
    res.append(q.pop(index))
"""

print("<" + ", ".join(map(str, res)) + ">")
