data = input()
result = []
value = 0

# 문자 확인
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
    
result.sort()

# 숫자가 하나라도 존재하면 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

print(''.join(result))