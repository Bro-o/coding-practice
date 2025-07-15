current_location = input()
row = int(current_location[1])
column = int(ord(current_location[0]) - ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

# 8가지 방향에 대해서 이동 가능한지 확인
result = 0
for step in steps:
    nrow = row + step[0]
    ncolumn = column + step[1]
    
    if nrow >= 1 and nrow <= 8 and ncolumn >=1 and ncolumn <= 8:
        result += 1

print(result)