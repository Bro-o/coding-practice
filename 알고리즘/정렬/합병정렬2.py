import random

def merge(arr, low, mid, high):
    arr1 = arr[low:mid]
    arr2 = arr[mid:high+1]
    index1 = index2 = 0
    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] <= arr2[index2]:
            arr[low] = arr1[index1]
            index1 += 1
        else:
            arr[low] = arr2[index2]
            index2 += 1
        low += 1
    
    while index1 < len(arr1):
        arr[low] = arr1[index1]
        index1 += 1
        low += 1
    while index2 < len(arr2):
        arr[low] = arr2[index2]
        index2 += 1
        low += 1


def merge_sort(arr):
    def _merge_sort(left, right):
        if left == right:
            return
        mid = (left + right) // 2
        _merge_sort(left, mid)
        _merge_sort(mid+1, right)
        merge(arr, left, mid+1, right)

    
    _merge_sort(0, len(arr) - 1)

my_list = []
for _ in range(50):
    my_list.append(random.randrange(100))

print("정렬 전:")
print(my_list)
print()
print("정렬 후:")
merge_sort(my_list)
print(my_list)