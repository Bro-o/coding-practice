"""
참조: First unique character in a string
주어진 문자열에서 반복되지 않는 문자 중 가장 먼저 나오는 문자의 인덱스를 출력하라. 모든 문자가 중복되면, -1을 출력하라.

예시

입력: leetcode, 출력: 0
입력: loveleetcode, 출력: 2
입력: aabb, 출력 -1
"""

# 이중 반복문으로 풀기
def first_unique_char(s: str) -> int:
    n: int = len(s)
    check: list[int] = [0] * n # 1이면 검사한 반복되는 문자
    for i, ch in enumerate(s):
        if check[i] == 1:
            continue
        check[i] == 1
        is_unique = True
        for j in range(i+1, n):
            if ch == s[j]:
                check[j] = 1
                is_unique = False
        if is_unique:
            return i
    return -1

# 사전을 이용하여 풀기
def first_unique_char_dict(s: str) -> int:
    count: dict[str, int] = {}
    for ch in s:
        if ch not in count:
            count[ch] = 1
        else:
            count[ch] += 1
    for i, c in enumerate(count):
        if count[c] == 1:
            return i
    return -1

# Counter 함수 이용
from collections import Counter
def first_unique_char_dict2(s: str) -> int:
    count = Counter(s)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1


#테스트 코드
for s in ("leetcode", "loveleetcode", "aabb", "eevve"):
    print(first_unique_char(s))