n = int(input())
users = []

for _ in range(n):
    age, name = input().split()
    users.append((int(age), name))

users.sort(key = lambda x: x[0])

for user in users:
    print(user[0], user[1])