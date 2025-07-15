def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    low = []
    high = []

    for value in arr[1:]:
        if value <= pivot:
            low.append(value)
        else:
            high.append(value)
    
    print(f'{low} + {[pivot]} + {high}')
    return qsort(low) + [pivot] + qsort(high)

my_list = [24, 26, 2, 16, 32, 31, 25]
print("정렬 전:")
print(my_list)
print()
print("정렬 과정:")
print(qsort(my_list))