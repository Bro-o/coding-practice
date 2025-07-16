"""
참조: 요세푸스 순열
1번부터 N 번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K 번째 사람을 제거한다.
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

예시

입력: 7, 3
출력: [3, 6, 2, 7, 5, 1, 4]
"""

# 리스트 이용
def josephus_list(n: int, k: int) -> list[int]:
    res: list[int] = []
    line: list[int] = [1] * n # 1이면 제거 필요, 0이면 제거 완료
    i: int = -1
    for _ in range(n-1):
        count: int = 0
        while count < k:
            i = (i + 1) % n
            if line[i]:
                count += 1
        line[i] = 0
        res.append(i+1)
    res.append(line.index(1) + 1)
    return res

# 큐 이용
from Queue import Queue
def josephus_q(n: int, k: int) -> list[int]:
    res: list[int] = []
    q = Queue()
    for i in range(n):
        q.enqueue(i+1)
    while q.front.next:
        for _ in range(k-1):
            q.enqueue(q.dequeue())
        res.append(q.dequeue())
    res.append(q.dequeue())
    return res

#테스트 코드
print(josephus_list(10, 7))
print(josephus_q(10, 7))