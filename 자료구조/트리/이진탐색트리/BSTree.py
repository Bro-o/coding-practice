class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def __contains__(self, data):
        node = self.root
        while node:
            if node.data == data:
                return True
            elif node.data > data:
                node = node.left
            else:
                node = node.right
        return False
    
    def inorder(self):
        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            res.append(node.data)
            _inorder(node.right)
        res = []
        _inorder(self.root)
        return res

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if node.data > data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node
    
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def get_leftmost(node):
        while node.left:
            node = node.left
        return node

    def _delete(self, node, data):
        if node is None:
            return
        if node.data > data:
            node.left = self._delete(node.left, data)
        elif node.data < data:
            node.right = self._delete(node.right, data)
        else:
            # 삭제할 노드를 찾았고, 자식노드가 둘
            # 삭제할 노드의 오른쪽에서 제일 작은 값을 노드를 찾는다.
            # 삭제할 노드의 값은 가장 작은 값으로 대체
            # 가장 작은 노드를 찾아서 삭제하고, 결과를 반환한다
            if node.left and node.right:
                leftmost = self.get_leftmost(node.right)
                node.data = leftmost.data
                node.right = self._delete(node.right, leftmost)
                return node
            
            # 자식이 하나이거나 리프 노드이면 해당 자식을 반환
            if node.left:
                return node.left
            else:
                return node.right
        return node
        
    def delete(self, data):
        self.root = self._delete(self.root, data)
    
    def balancing(root):
        # 중위 순회 결과 반환
        # 노드 자체가 들어감
        def _sort_nodes(node):
            _sort_nodes(node.left)
            nodes.append(node)
            _sort_nodes(node.right)

        # 균형 잡기 위한 재귀 함수
        def _balancing(left, right):
            if left > right:
                return
            mid = (left + right) // 2
            node = nodes[mid]
            node.left = _balancing(left, mid-1)
            node.right = _balancing(mid+1, right)
            return node
        
        nodes = []
        _sort_nodes(root)
        root = _balancing(0, len(nodes)-1)

# 테스트 코드
# bst = BSTree()
# for x in (6, 4, 9, 2, 5, 7, 8):
#     bst.insert(x)

# print(f"Inorder traversal: {bst.inorder()}")