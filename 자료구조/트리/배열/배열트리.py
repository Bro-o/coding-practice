tree = ["A", "B", "C", "D", "E", "F", None, "G"]

n = len(tree)
for i in range(n):
    if tree[i] is not None:
        print(f"Parent: {tree[i]}", end=", ")
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and tree[left] is not None:
            print(f"Left: {tree[left]}", end=", ")
        if right < n and tree[right] is not None:
            print(f"Right: {tree[right]}", end=", ")
        print()

for i in range(1, n):
    if tree[i] is not None:
        print(f"Parent of {tree[i]} -> {tree[(i-1)//2]}")