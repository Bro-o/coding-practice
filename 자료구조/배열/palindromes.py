# 문자열 슬라이싱 이용
def is_palindrom1(word: str) -> bool:
    if word == word[::-1]:
        return True
    else:
        return False

# 두 포인터를 이용
def is_palindrom2(word: str) -> bool:
    left = 0
    right = len(word) -1
    while left < right:
        if word[left] != word[right]:
            return False
        left, right = left + 1, right - 1
    return True

# Test code
words = ["racecar", "rotor", "tomato", "별똥별", "코끼리"]
for word in words:
    print(f"Is '{word}' palindrome? {is_palindrom1(word)}")
    print(f"Is '{word}' palindrome? {is_palindrom2(word)}")