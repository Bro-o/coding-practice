"""
집합

데이터를 넣을 때는 자료형을 명확하게 하기
"""
import sys
m = int(input())
s = set()
for _ in range(m):
    command = sys.stdin.readline().split()
    if command[0] == "add":
        s.add(int(command[1]))
    elif command[0] == "remove":
        s.discard(int(command[1]))
    elif command[0] == "check":
        if int(command[1]) in s:
            print("1")
        else:
            print("0")
    elif command[0] == "toggle":
        if int(command[1]) in s:
            s.remove(int(command[1]))
        else:
            s.add(int(command[1]))
    elif command[0] == "all":
        s.update([i for i in range(1, 21)])
    elif command[0] == "empty":
        s = set()