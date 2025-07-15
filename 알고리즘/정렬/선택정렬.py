import random

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_value_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value_index]:
                min_value_index = j
        arr[i], arr[min_value_index] = arr[min_value_index], arr[i]

        print(arr)
            


# 임의의 숫자 리스트
my_list = []
for _ in range(10):
    my_list.append(random.randrange(15))


# 검증
print('정렬 전')
print(my_list)

print('정렬 과정')
selection_sort(my_list)