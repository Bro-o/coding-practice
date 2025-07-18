n = int(input())
arr = []

for _ in range(n):
    x, y = input().split()
    arr.append((int(x), int(y)))

arr.sort(key=lambda x : (x[0], x[1]))

for data in arr:
    print(data[0], data[1])