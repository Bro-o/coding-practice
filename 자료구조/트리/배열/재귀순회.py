def preorder(tree):
    def _preorder(i = 0):
        if i >= len(tree) or tree[i] is None:
            return
        res.append(tree[i])
        _preorder(2 * i + 1)
        _preorder(2 * i + 2)
    res = []
    _preorder()
    return res

def inorder(tree):
    def _inorder(i = 0):
        if i >= len(tree) or tree[i] is None:
            return
        _inorder(2 * i + 1)
        res.append(tree[i])
        _inorder(2 * i + 2)
    res = []
    _inorder()
    return res

def postorder(tree):
    def _postorder(i = 0):
        if i >= len(tree) or tree[i] is None:
            return
        _postorder(2 * i + 1)
        _postorder(2 * i + 2)
        res.append(tree[i])
    res = []
    _postorder()
    return res

#테스트 코드
tree = ["A", "B", "C", "D", "E", "F", None, "G"]
print(preorder(tree))
print(inorder(tree))
print(postorder(tree))