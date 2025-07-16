"""
괄호까지 처리하여 후위 표기법으로 바꾸기
"""

from Stack import Stack

def to_postfix2(exp: str) -> str:
    op: dict[str, int] = {"+": 1, "-": 1, "*": 2, "/": 2}
    res: str = ""
    s: list[str] = []
    for ch in exp:
        if ch.isnumeric():
            res += ch
        elif ch == "(":
            s.append(ch)
        elif ch == ")":
            while s[-1] != "(":
                res += s.pop()
            s.pop()
        elif ch in op:
            if s and s[-1] != "(" and (op[ch] <= op[s[-1]]):
                res += s.pop()
            s.append(ch)
    while s:
        res += s.pop()
    return res

def eval_postfix(exp: str) -> int:
    s: list[int] = []
    for ch in exp:
        if ch.isnumeric():
            s.append(int(ch))
        elif ch != " ":
            n2 = s.pop()
            n1 = s.pop()
            if ch == "+":
                res = n1 + n2
            elif ch == "-":
                res = n1 - n2
            elif ch == "*":
                res = n1 * n2
            elif ch == "/":
                res = n1 / n2
            s.append(res)
    return s[0]



#테스트 코드
for expr in ("(3 + 5) * 2", "((1 + 2) * 3) / 4 + 5 * (6 - 7)"):
    print(f"{expr} -> {to_postfix2(expr)}")

for expr in ("35+2*", "12+3*4/567-*+"):
    print(f"{expr} -> {eval_postfix(expr)}")