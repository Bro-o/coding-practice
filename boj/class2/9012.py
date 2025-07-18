# 괄호
#자료구조 #문자열 #스택
n = int(input())

def check_vps(expression):
    stack = []
    for exp in expression:
        if exp == "(":
            stack.append(exp)
        elif exp == ")":
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"
    
for _ in range(n):
    expression = input()
    print(check_vps(expression))