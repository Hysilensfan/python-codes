# First method
from ast import literal_eval as le


class BT:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def dfs(self, node) -> tuple:
        if node is None: return -1, 0
        (leftheight, leftdiameter) = self.dfs(node.left)
        (rightheight, rightdiameter) = self.dfs(node.right)
        height: int = max(leftheight, rightheight) + 1
        currentpath: int = leftheight + rightheight + 2
        diameter: int = max(leftdiameter, rightdiameter, currentpath)
        return height, diameter

    def longest_length(self, root) -> int:
        _, diameter = self.dfs(root)  # _ character, Declare that the returned variable is not referenced because we only need the path length.
        return diameter

    def general_tree(self, arr: list) -> int:
        nodes = [None if x is None else BT(x) for x in arr]
        for i in range(len(nodes)):
            if nodes[i] is None:
                continue
            left: int = 2 * i + 1
            right: int = 2 * i + 2
            if left < len(nodes):
                nodes[i].left = nodes[left]
            if right < len(nodes):
                nodes[i].right = nodes[right]
        return self.longest_length(nodes[0])


bt = BT()
[print(bt.general_tree(le(input().strip().replace("null", "None")))) for _ in range(int(input()))]

