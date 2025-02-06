# while문으로 m이 0이 될때까지 더하기
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)