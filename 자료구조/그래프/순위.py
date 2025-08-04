"""
참조: 프로그래머스
n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해 주세요.

results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
모든 경기 결과에는 모순이 없습니다.
입출력 예

n	results	return
5	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	2
2번 선수는 [1, 3, 4] 선수에게 패배했고 5번 선수에게 승리했기 때문에 4위입니다.
5번 선수는 4위인 2번 선수에게 패배했기 때문에 5위입니다.
"""
def make_graph(n, results):
    graph = [[] for _ in range(n+1)]
    for a, b in results:
        graph[a].append(b)
    return graph

def dfs(graph, i):
    res = []
    visited = set()

    def _dfs(u):
        if u not in visited:
            res.append(u)
            visited.add(u)
            for v in graph[u]:
                _dfs(v)
    
    _dfs(i)
    return res


def solution(n, results):
    answer = 0
    graph = make_graph(n, results)
    count = [0] * (n+1)

    for i in range(1, n+1):
        res = dfs(graph, i)
        count[i] += len(res) - 1 # 이긴 횟수
        for lose in res[1:]:
            count[lose] += 1 # 진 횟수 더하기

    for cnt in count:
        if cnt == n-1:
            answer += 1
    
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))