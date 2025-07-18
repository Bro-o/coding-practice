import sys
n = int(sys.stdin.readline())
q = []

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        q.append(command[1])
    elif command[0] == "pop":
        if not q:
            print("-1")
        else:
            print(q.pop(0))
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        if not q:
            print("1")
        else:
            print("0")
    elif command[0] == "front":
        if not q:
            print("-1")
        else:
            print(q[0])
    elif command[0] == "back":
        if not q:
            print("-1")
        else:
            print(q[-1])