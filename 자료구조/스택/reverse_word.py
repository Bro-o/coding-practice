from Stack import Stack 

def reverse_word(word: str) -> str:
    answer: str = ""
    s = Stack()
    for w in word:
        s.push(w)
    while not s.is_empty():
        answer += s.pop()
    return answer

# 테스트 코드
print(reverse_word("aircraft"))