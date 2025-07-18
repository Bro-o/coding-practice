"""
sys.stdin.readline()은 입력 받은 값 끝에 \n 개행문자가 포함되므로 바로 == 연산을 하면 안됨
strip() 또는 rstrip('\n') 사용하거나
split()을 이용하는 방법도 있음
"""
import sys
n = int(sys.stdin.readline())
s = []

for _ in range(n):
    command = sys.stdin.readline().strip()
    
    if command.startswith("push"):
        order, data = command.split()
        s.append(data)
    elif command == "pop":
        if not s:
            print("-1")
            continue
        print(s.pop())
    elif command == "size":
        print(len(s))
    elif command == "empty":
        if len(s):
            print("0")
        else:
            print("1")
    elif command == "top":
        if not s:
            print("-1")
            continue
        print(s[-1])