"""
add_nodes: 그래프에 노드를 추가한다.
add_edges: 그래프에 간선을 추가한다.
delete_nodes: 그래프에서 노드를 삭제한다.
delete_edges: 그래프에서 간선을 삭제한다.
dfs: 그래프를 특정 노드부터 깊이 우선 탐색한다.
bfs: 그래프를 특정 노드부터 너비 우선 탐색한다.
dijkstra: 가중 그래프에서 다익스트라 알고리즘으로 최단 경로를 탐색한다.
"""
class Graph:
    def __init__(self):
        self.graph = {}
        self.cost = {}
        self.node_from = {}

    def display(self):
        from pprint import pprint
        pprint(self.graph)
        print()

    def add_nodes(self, *nodes):
        for u in nodes:
            if u not in self.graph:
                self.graph[u] = {}
    
    def add_edges(self, *edges):
        for edge in edges:
            u, v = edge[0], edge[1]

            w = edge[2] if len(edge) == 3 else 0

            self.add_nodes(u, v)
            self.graph[u][v] = w
            self.graph[v][u] = w
    
    def delete_edges(self, *edges):
        for u, v in edges:
            self.graph[u].pop(v, None)
            self.graph[v].pop(u, None)
    
    def delete_nodes(self, *nodes):
        for u in nodes:
            if u not in self.graph:
                continue
            for v in self.graph[u]:
                self.graph[v].pop(u, None)
            del self.graph[u]

    def dfs(self, node):
        res = []
        visited = set()

        self.cost = {node: 0 for node in self.graph}
        self.node_from = {node: None for node in self.graph}

        def _dfs(u):
            visited.add(u)
            res.append(u)
            for v in self.graph[u]:
                if v not in visited:
                    self.cost[v] = self.cost[u] + self.graph[u][v]
                    self.node_from[v] = u
                    _dfs(v)

        _dfs(node)
        return res
    
    def bfs(self, node):
        # 리스트보다 성능이 우수한 deque 사용
        from collections import deque

        res = []
        queue = deque([node])
        visited = set(queue)

        self.cost = {node: 0 for node in self.graph}
        self.node_from = {node: None for node in self.graph}

        while queue:
            u = queue.popleft()
            res.append(u)
            for v in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    self.cost[v] = self.cost[u] + self.graph[u][v]
                    self.node_from[v] = u
                    queue.append(v)
        return res
    
    def dijkstra(self, start):
        import math, heapq

        self.cost = {node: math.inf for node in self.graph}
        self.node_from = {node: None for node in self.graph}
        self.cost[start] = 0

        res = []
        visited = set()

        heap = []
        heapq.heappush(heap, (0, start))

        while heap:
            prev_time, u = heapq.heappop(heap)
            if u in visited:
                continue
            res.append(u)
            visited.add(u)
            
            for v in self.graph[u]:
                if(new_time := prev_time + self.graph[u][v]) < self.cost[v]:
                    self.cost[v] = new_time
                    self.node_from[v] = u
                    heapq.heappush(heap, (self.cost[v], v))
            
        return res
    
    def get_path(self, end):
        path = ""
        node = end
        while self.node_from[node]:
            path = " -> " + str(node) + path
            node = self.node_from[node]
        
        if path:
            path = str(node) + path
            return f"{path} (cost = {str(self.cost[end])})"
        else:
            return f"There is no path"


g = Graph()
g.add_edges(("A", "B", 1), ("A", "C", 4), ("A", "D", 5))
g.add_edges(("B", "D", 2), ("C", "D", 4), ("C", "E", 3))
g.add_edges(("D", "F", 3), ("E", "F", 2))
print("그래프의 상태:")
g.display()

print("노드 A부터 깊이 우선 탐색 결과:", g.dfs("A"))
print()
print("노드 A부터 너비 우선 탐색 결과:", g.bfs("A"))
print("A에서 E로 가는 최소 경유 경로: ", g.get_path("E"))
print("A에서 F로 가는 최소 경유 경로: ", g.get_path("F"))
print()
print("다익스트라 알고리즘으로 탐색")
g.dijkstra("A")
print("A에서 E로 가는 최단 경로: ", g.get_path("E"))
print("A에서 F로 가는 최단 경로: ", g.get_path("F"))