"""
길 찾기 게임
nodeinfo
[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

result
[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

파이썬의 기본 재귀 깊이는 1000이라 런타임 에러가 발생하므로 리밋을 늘린다.
enumerate(list, 1) : 인덱스를 1부터 시작

"""
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, info):
        self.x = info[0][0]
        self.data = info[1]
        self.left = None
        self.right = None

def insert(node, info):
    if node is None:
        return Node(info)
    if info[0][0] < node.data:
        node.left = insert(node.left, info)
    else:
        node.right = insert(node.right, info)
    return node

def make_tree(nodeinfo):
    # nodes = [([x,y], i), ... ] 좌표와 인덱스가 들어간 새로운 배열
    nodes = []
    for i, node in enumerate(nodeinfo, 1):
        nodes.append((node, i))
    
    # x, -y 좌표 순으로 정렬
    nodes.sort(key = lambda x: (-x[0][1], x[0][0]))

    # 이진 탐색 트리 만들기
    root = None
    for node in nodes:
        root = insert(root, node)
    return root

def preorder(root):
    def _preorder(node):
        if node:
            res.append(node.data)
            _preorder(node.left)
            _preorder(node.right)
    res = []
    _preorder(root)
    return res

def postorder(root):
    def _postorder(node):
        if node:
            _postorder(node.left)
            _postorder(node.right)
            res.append(node.data)
    res = []
    _postorder(root)
    return res


def solution():
    answer = []
    nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    root = make_tree(nodeinfo)
    answer.append(preorder(root))
    answer.append(postorder(root))
    print(answer)

solution()