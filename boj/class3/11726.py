"""
2xn 타일링
# DP
f(n) = f(n-2) + f(n-1)
나머지 연산은 미리해서 넣어놔야 런타임 에러가 안 발생함
배열 미리 잡아놓는건 메모리를 크게 안쓰는듯
"""
# 메모리 32412 KB
n = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = (d[i-2] + d[i-1]) % 10007

print(d[n])

# 메모리 32544 KB
n = int(input())
d = [0] * (n + 1)
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    d[1] = 1
    d[2] = 2

    for i in range(3, n+1):
        d[i] = (d[i-2] + d[i-1]) % 10007

    print(d[n])