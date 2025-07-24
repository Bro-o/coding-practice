"""
참조: geeksforgeeks.org
이진트리가 있을 때, 형제 노드가 없는 노드의 키를 출력하라. 형제 노드가 없는 노드가 없으면 -1을 출력하라.

예시

입력

           37
          /   
        20
       /
     113
출력: [20, 113]
"""
from 이진트리 import Node, Tree

def find_has_no_sibling(tree):
    res, q = [], [tree.root]
    while q:
        node = q.pop(0)
        if node.left:
            q.append(node.left)
            if not node.right:
                res.append(node.left.data)
                continue
        if node.right:
            q.append(node.right)
            if not node.left:
                res.append(node.right.data)
                continue
    
    return res if res else [-1]

tree = Tree()
tree.make_tree([37, 20, None, 113])
print(find_has_no_sibling(tree))