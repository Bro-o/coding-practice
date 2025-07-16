"""
참조: Largest subarray with 0 sum
양의 정수와 음의 정수의 배열이 있다. 합이 0인 부분 배열 중 가장 긴 배열의 길이를 구하라.

예시

입력: A = [15, -2, 2, -8, 1, 7, 10, 23]
출력: 5 (합이 0인 부분 배열은 -2 2 -8 1 7)
"""

# 이중 반복문으로 풀기
def maxLen(arr: list[int]) -> int:
    n: int = len(arr)
    answer: int = 0
    for i in range(n):
        total = 0
        left = i
        right = i
        for j in range(i, n):
            total += arr[j]
            if total == 0:
                right = j
                answer = max(answer, right - left + 1)
    return answer

# 사전을 이용하여 풀기
from collections import defaultdict
def maxLen_dict(arr: list[int]) -> int:
    total: int = 0
    dic: dict[int, list[int]] = defaultdict
    dic[0] = [-1]
    for i in range(len(arr)):
        total += arr[i]
        dic[total].append(i)
    ans = 0
    for v in dic.values():
        ans = max(ans, v[-1] - v[0])
    return ans

# 사전 이용 함수 개선
def maxLen_dict2(arr: list[int]) -> int:
    dic: dict[int, int] = {0: -1}
    ans = 0
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        if total in dic:
            ans = max(ans, i - dic[total])
        else:
            dic[total] = i
    return ans

#테스트 코드
A = [15, -2, 2, -8, 1, 7, 10, 23]
print(maxLen(A))