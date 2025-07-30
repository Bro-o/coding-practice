from Graph import Graph

class Digraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edges(self, *edges):
        for edge in edges:
            u, v = edge[0], edge[1]
            w = edge[2] if len(edge) == 3 else 0
            self.add_nodes(u, v)
            self.graph[u][v] = w

    def delete_nodes(self, *nodes):
        for u in nodes:
            if u not in self.graph:
                continue
            for v in self.graph:
                self.graph[v].pop(u, None)
            del self.graph[u]

g = Digraph()
g.add_edges(("A", "C", 4), ("B", "C", 2))
g.add_edges(("C", "E", 3), ("C", "F", 5), ("D", "B", 3))
g.add_edges(("E", "F", 1), ("F", "D", 2))

print("방향 그래프의 상태:")
g.display()

print("노드 B부터 깊이 우선 탐색 결과:", g.dfs("B"))
print()
print("노드 B부터 너비 우선 탐색 결과:", g.bfs("B"))
print("B에서 E로 가는 최소 경유 경로: ", g.get_path("E"))
print("B에서 F로 가는 최소 경유 경로: ", g.get_path("F"))
print("B에서 A로 가는 최소 경유 경로: ", g.get_path("A"))
print()

print("다익스트라 알고리즘으로 탐색")
g.dijkstra("B")
print("B에서 E로 가는 최단 경로: ", g.get_path("E"))
print("B에서 F로 가는 최단 경로: ", g.get_path("F"))
print("B에서 A로 가는 최단 경로: ", g.get_path("A"))
print()

print("초기 방향 그래프의 상태:")
g.display()
print("간선 C-E를 삭제한 후의 상태")
g.delete_edges(("C", "E"))
g.display()
print("노드 A와 F를 삭제한 후의 상태")
g.delete_nodes("A", "F")
g.display()
