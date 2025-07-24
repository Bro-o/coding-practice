"""
참조: geeksforgeeks.org
알파벳 소문자로 이루어진 문자열 s과 숫자 k가 주어진다. k개의 문자를 삭제하여 얻을 수 있는 문자열의 최솟값을 반환하라. 문자열의 값은 각 문자의 개수를 제곱하여 더한 것이다.

예시 1

입력: s = abccc, k = 1
출력: 6
"c"를 하나 제거하면 a와 b는 한 개씩, "c"는 두 개다. 따라서 문자열의 값은 1^2 + 1^2 + 2^2 = 6 이다.

예시 2

입력: s = aabcbcbcabcc, k = 3
출력: 27
"c를 두 개, "b"를 하나 제거하면, 모든 문자의 개수는 세 개씩이다. 따라서  3^2 + 3^2 + 3^2 = 27 이다.
"""
import heapq

def minValue(s: str, k: int) -> int:
    counter: dict[str, int] = {}
    for ch in s:
        if ch not in counter:
            counter[ch] = 1
        else:
            counter[ch] += 1
    
    heap: list[int] = []
    for value in counter.values():
        heapq.heappush(heap, -value)

    for _ in range(k):
        temp = heapq.heappop(heap) + 1
        heapq.heappush(heap, temp)
    
    answer = 0
    for value in heap:
        answer += value**2
    return answer

print(minValue('abccc', 1))
print(minValue('aabcbcbcabcc', 3))