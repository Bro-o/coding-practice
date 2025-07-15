import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        print(f'\n시작 인덱스 {i}')
        print(arr)
        while i > 0 and arr[i] < arr[i - 1]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
            print(arr)


# 임의의 숫자 리스트
my_list = []
for _ in range(10):
    my_list.append(random.randrange(15))


# 검증
print('정렬 전')
print(my_list)

print('정렬 과정')
insertion_sort(my_list)