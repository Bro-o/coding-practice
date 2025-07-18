# 체스판 다시 칠하기
"""
아이디어 1: 인덱스를 더해서 2로 나머지를 구하면 0 과 1이 번갈아서 나오는데 체스판과 동일함
아이디어 2: W로 시작했을 때 바꿔야하는 칸 수랑 B로 시작했을 때 바꿔야하는 칸 수를 더하면 전체 칸 수가 됨
아이디어 3: n, m에서 8*8이 차지하는 영역 옮겨가며 바꿔 칠해야하는 칸 수 카운팅
"""
n, m = map(int, input().split())
board = []
res = n * m

for _ in range(n):
    board.append(input())
    
def count_repaint(n_start, m_start):
    color = ['W', 'B']
    count = 0
    for i in range(n_start, n_start + 8):
        for j in range(m_start, m_start + 8):
            which_color = (i + j) % 2
            if board[i][j] != color[which_color]:
                count += 1

    if count > 32:
        count = 64 - count

    return(count)

for n_start in range(0, n - 7):
    for m_start in range(0, m - 7):
        count_repaint(n_start, m_start)
        res = min(res, count_repaint(n_start, m_start))

print(res)