"""
회의실 배정
# 그리디 # 정렬
"""

n = int(input())
meeting_list = []

for _ in range (n):
    start, end = map(int, input().split())
    meeting_list.append((start, end))

meeting_list.sort(key = lambda x: (x[0], x[1]))

tmp = (0, 0)
res = 0

for s, e in meeting_list:
    if s < tmp[1]: # 현재 회의 아직 안 끝남
        duration = e - s
        if duration < tmp[1] - tmp[0] and e < tmp[1]: # 회의가 끝나는 시간이 더 늦춰지면 안됨
            tmp = (s, e)
    else: # 회의 끝남
        res += 1
        tmp = (s, e)

print(res)