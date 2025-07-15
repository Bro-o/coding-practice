arr = [5, 2, 8, 3, 7, 6, 1, 4]
sorted_arr = sorted(arr, key=lambda x: (x % 2, x))
print(sorted_arr)  # 출력: [2, 4, 6, 8, 1, 3, 5, 7]

# 짝수는 내림차순, 홀수는 오름차순
sorted_arr_mixed = sorted(arr, key=lambda x: (x % 2, -x))
print(sorted_arr_mixed)  # 출력: [8, 6, 4, 2, 7, 5, 3, 1]