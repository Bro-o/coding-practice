def partition(arr, low, high):
    print(f'분할 범위 {low}~{high}', end=': ')
    pivot_index = low
    pivot = arr[pivot_index]
    low += 1
    while low <= high:
        while (low <= high) and (arr[low] <= pivot):
            low += 1
        while (low <= high) and (arr[high] > pivot):
            high -= 1
        if (low < high):
            arr[low], arr[high] = arr[high], arr[low]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    print(f'피벗 {pivot}을 기준으로 분할: {arr}')
    return high

def qsort(arr):
    def _qsort(arr, low, high):
        if low < high:
            pivot = partition(arr, low, high)
            _qsort(arr, low, pivot - 1)
            _qsort(arr, pivot + 1, high)

    _qsort(arr, 0, len(arr) -1)

my_list = [6, 9, 5, 3, 11, 2, 13, 7, 6, 10]
print("정렬 전:")
print(my_list)
# print("\n정렬 과정:")
qsort(my_list)
print("\n정렬 후:")
print(my_list)