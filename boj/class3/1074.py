"""
Z
# 재귀
N은 15이하의 수이므로 모두 방문하게 되면 시간초과
내가 찾는 칸이 현재 번위에 없다면 N*N 만큼 스킵하도록 해야한다
"""

N, r, c = map(int, input().split())
count = -1

def recursive(x, y, n):
    global count

    if n == 2:
        for i in range(x, x+n):
            for j in range(y, y+n):
                count += 1
                if i == r and j == c:
                    print(count)
                    exit(0)
        return

    if not (x <= r < x+n and y <= c < y+n):
        count += n*n
        return

    for i in range(x, x+n, n//2):
        for j in range(y, y+n, n//2):
            recursive(i, j, n//2)
    


recursive(0, 0, 2 ** N)
