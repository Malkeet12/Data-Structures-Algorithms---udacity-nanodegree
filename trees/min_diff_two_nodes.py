# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class bst:
    def __init__(self):
        pass

    def minDiffInBST(self, root: TreeNode) -> int:
        return self.minDiffInBSTRecur(root, 0)

    def minDiffInBSTRecur(self, root: TreeNode, out) -> int:
        if root is None:
            return out

        if root.left is not None:
            out = min(root.val - root.left.val, out)
            print(out)
        if root.right is not None:
            out = min(root.right.val - root.val, out)
            print(out)
        left = self.minDiffInBSTRecur(root.left, out)
        right = self.minDiffInBSTRecur(root.right, out)
        print(out)

        if left > right:
            return right

        return left


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left = TreeNode(1)
root.left = TreeNode(3)
root.left = TreeNode(None)
root.left = TreeNode(None)
bst().minDiffInBST(root)
