"""
자세한 문제 설명은 프로그래머스를 참조
n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 개수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단 경로로 이동했을 때 간선의 개수가 가장 많은 노드를 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해 주세요.

입출력 예

n	vertex	return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
예제의 그래프를 표현하면 아래 그림과 같고, 1번 노드에서 가장 멀리 떨어진 노드는 4,5,6번 노드입니다.
"""

# (1로부터 떨어진 거리, 노드 번호)처럼 튜플로 정보 저장
def make_graph(n: int, edge: list[list]) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = {}
    for i in range (1, n+1):
        graph[i] = []
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def solution(n: int, edge: list[list]) -> int:
    answer: int = 0
    graph = make_graph(n, edge)

    res: list[tuple[int, int]] = []
    queue = [(0, 1)]
    visited = set([1]) # set 자료형에는 리스트를 입력하여 만들 수 있음

    while queue:
        level, u = queue.pop(0)
        res.append((level, u))
        level += 1
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                queue.append((level, v))
    
    res.sort(reverse=True)
    max_instance = res[0][0]
    for dist, _ in res:
        if dist < max_instance:
            break
        answer += 1
    return answer


# 거리를 리스트에 따로 담기
from collections import deque
def make_graph(n: int, edge: list[list]) -> list[list]:
    graph: list[list] = [[] for _ in range(n+1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    return graph
def solution(n: int, edge: list[list]) -> list[list]:
    graph: list[list] = make_graph(n, edge)

    distance = [-1 for _ in range(n+1)]
    distance[1] = 0

    queue: deque[int] = deque([1])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                queue.append(v)
    
    distance.sort(reverse=True)
    return distance.count(distance[0])


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))