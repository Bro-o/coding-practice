data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    # 만약 0 또는 1이라면 + 수행
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
    
print(result)