"""
중위 표기법을 후위 표기법으로 바꾸는 방법
- 문자열 수식을 순회한다.
    - 피연산자를 만나면 출력한다.
    - 연산자를 만나면
        - 스택에 연산자가 있는지 확인한다.
        - 스택의 마지막 연산자가 현재 연산자보다 우선순위가 높으면 pop하여 출력한다.
    - 현재 연산자를 스택에 넣는다.
- 스택이 빌 때까지 pop하여 출력한다.
"""
from Stack import Stack

# 스택 이용
def to_postfix_stack(exp: str) -> str:
    op: dict[str, int] = {"+": 1, "-": 1, "*": 2, "/": 2}
    res: str = ""
    s = Stack()
    for ch in exp:
        if ch.isnumeric():
            res += ch
        elif ch in op:
            if not s.is_empty() and (op[ch] <= op[s.peek()]):
                res += s.pop()
            s.push(ch)
    while not s.is_empty():
        res += s.pop()
    return res

# 리스트 이용
def to_postfix_list(exp: str) -> str:
    op: dict[str, int] = {"+": 1, "-": 1, "*": 2, "/": 2}
    res: str = ""
    s: list[str] = []
    for ch in exp:
        if ch.isnumeric():
            res += ch
        elif ch in op:
            if s and (op[ch] <= op[s[-1]]):
                res += s.pop()
            s.append(ch)
    while s:
        res += s.pop()
    return res

for expr in ("3+5*2", "3*5+2"):
    print(f"{expr} -> {to_postfix_stack(expr)}")