from Stack import Stack

def check_bracket2(expression: str) -> bool:
    brackets: dict[str, str] = {")": "(", "}": "{", "]": "["}
    s = Stack()
    for exp in expression:
        if exp in brackets.values():
            s.push(exp)
        elif exp in brackets.keys():
            pop_bracket = s.pop()
            if not pop_bracket or pop_bracket != brackets[exp]:
                return False
    return True if s.is_empty() else False

#테스트 코드
print(check_bracket2("[{a * (b + c)} - d] / e"))
print(check_bracket2("[{a * (b + c)] - d] / e"))
