"""
참고: 프로그래머스
15는 다음과 같이 4가지로 표현할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15
자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution을 완성해 주세요.
"""

# 큐 이용
def solution(n: int) -> int:
    q: list[int] = [1]
    answer: int = 1
    i: int = 1
    total: int = 1
    mid: int = (n + 1) // 2
    while i < mid:
        i += 1
        total += i
        q.append(i)
        while total > n:
            total -= q.pop(0)
        if total == n:
            answer += 1
    return answer

# 포인터 이용
def solution2(n: int) -> int:
    left = 1
    right = 1
    answer = 1
    total = 0
    while right < n:
        total += right
        while total > n:
            total -= left
            left += 1
        if total == n:
            answer += 1
        right += 1
    return answer



#테스트 코드
print(solution2(15))
print(solution2(20))