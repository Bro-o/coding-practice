def find_max_two(arr: list[int]) -> list[int]:
    """ 정수 리스트에서 가장 큰 두 값을 찾아서 반환
    Arguments:
        arr (list): 정수 리스트
    Return:
        list: [가장 큰 값, 두번째로 큰 값]
    """
    if len(arr) < 2:
        return arr
    
    max1, max2 = arr[:2]
    if max1 > max2:
        max1, max2 = max2, max1
    for n in arr[2:]:
        if n > max1:
            max1, max2 = n, max1
        elif n > max2:
            max2 = n
    return [max1, max2]

# Test code
arr = [[3, -1, 5, 0, 7, 4, 9, 1], [7]]
for a in arr:
    print(f"{a}에서 가장 큰 두 값: {find_max_two(a)}")