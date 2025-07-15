from Stack import Stack

def check_bracket(expression: str) -> bool:
    s = Stack()
    for exp in expression:
        if exp == "(":
            s.push(exp)
        elif exp == ")":
            if not s.pop():
                return False
    return True if s.is_empty() else False

#테스트 코드
print(check_bracket("((a * (b + c)) - d) / e"))
print(check_bracket("(((a * (b + c)) - d) / e"))