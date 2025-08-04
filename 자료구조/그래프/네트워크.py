"""
자세한 문제 설명은 프로그래머스를 참조
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어 있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오. 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.

입출력 예

n = 3, computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]], return =2
n = 3, computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]], return = 1
"""

# 깊이 우선 탐색을 이용한 풀이
def make_graph(n, computers):
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                graph[i].append(j)
    return graph

def solution(n, computers):
    answer = 0
    graph = make_graph(n, computers)
    visited = set()

    def dfs(u):
        if u in visited:
            return
        visited.add(u)
        for v in graph[u]:
            dfs(v)
    
    for i in range(n):
        if i not in visited:
            dfs(i)
            answer += 1
    
    return answer


# 인접행렬을 이용한 풀이
# dfs
def solution(n, computers):
    answer = 0
    visited = set()
    
    def dfs(com1):
        visited.add(com1)
        for com2 in range(n):
            if com2 not in visited and computers[com1][com2]:
                dfs(com2)

    for i in range(n):
        if i not in visited:
            answer += 1
            dfs(i)
    
    return answer

# bfs
def solution(n, computers):
    answer = 0
    visited = set()

    def bfs(i):
        q = [i]
        while q:
            com1 = q.pop(0)
            visited.add(com1)
            for com2 in range(i+1, n):
                if computers[com1][com2] == 1 and com2 not in visited:
                    q.append(com2)

    for i in range(n):
        if i not in visited:
            bfs(i)
            answer += 1
    
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
