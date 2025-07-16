"""
참조: generate binary numbers
양의 정수 n이 주어질 때 1부터 n까지의 십진수를 이진수로 출력하라.
"""

# 파이썬 내장 함수 이용
def generate_binary2(n: int) -> None:
    for i in range(1, n+1):
        print(bin(i)[2:])

# 큐 이용
from Queue import Queue
def generate_binary(n: int) -> None:
    q = Queue()
    q.enqueue("1")
    for _ in range(n):
        i = q.dequeue()
        q.enqueue(i + "0")
        q.enqueue(i + "1")
        print(i)




#테스트 코드
generate_binary(5)
generate_binary2(5)