"""
참조: Binary Array Sorting
0과 1로 이루어진 배열이 있다. 배열 자체를 오름차순으로 정렬하라.

입력: [1, 0, 1, 1, 1, 1, 1, 0, 0, 0], 출력: [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
입력: [1, 1], 출력: [1, 1]
"""

# count 메서드 이용하기
def bin_array_sort1(arr: list[int]) -> None:
    arr[:] = [0] * arr.count(0) + [1] * arr.count(1)

# 포인터 이용
def bin_array_sort2(arr: list[int]) -> None:
    left = 0
    right = len(arr) - 1
    while left < right:
        while left < len(arr) and arr[left] == 0:
            left += 1
        while right >= 0 and arr[right] == 1:
            right -= 1
        if left < right:
            arr[left], arr[right] = 0, 1
            left, right = left + 1, right - 1



# Test code
for arr in ([1, 0, 1, 1, 1, 1, 1, 0, 0, 0], [1, 1], [0], [1,0], [1]):
    # bin_array_sort1(arr)
    bin_array_sort2(arr)
    print(arr)
    