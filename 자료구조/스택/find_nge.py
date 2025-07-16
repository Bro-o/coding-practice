"""
참조: https://www.geeksforgeeks.org/next-greater-element/
음이 아닌 정수 배열이 주어졌을 때, 각 원소의 오른쪽에 있는 원소 중에서 현재 원소보다 큰 값을 출력하되, 가장 근접한 원소를 출력하라. 현재 원소보다 큰 값이 없으면 -1을 출력하라.

예시 1
입력: [4, 5, 2, 25]
출력:
4 --> 5
5 --> 25
2 --> 25
25 --> -1

예시 2
입력: [13, 7, 6, 12]
출력:
13 --> -1
7 --> 12
6 --> 12
12 --> -1
"""
def find_nge(arr: list[int]) -> list[int]:
    n: int = len(arr)
    s: list[int] = [] # 큰 원소를 저장 해놓는 리스트
    res: list[int] = [-1] * n
    for i in range(n-1, -1, -1):
        while s:
            if s[-1] > arr[i]:
                res[i] = s[-1]
                break
            else:
                s.pop()
        s.append(arr[i])
    for i in range(n):
        print(f"{arr[i]} --> {res[i]}")



#테스트 코드
find_nge([4, 5, 2, 25])