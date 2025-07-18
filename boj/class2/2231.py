n = int(input())

for i in range(1, n+1):
    each_num_sum = sum(list(map(int, str(i))))
    result = i + each_num_sum
    
    if result == n:
        print(i)
        break
    if i == n:
        print(0)