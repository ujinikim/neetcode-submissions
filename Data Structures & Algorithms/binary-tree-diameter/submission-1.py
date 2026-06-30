# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = -1
        
        def dfs(node, cur):
            nonlocal res
            if not node:
                return cur - 1

            left = dfs(node.left, cur + 1)
            right = dfs(node.right, cur + 1)

            res = max(res, left + right - (cur * 2))

            return max(left, right)
        dfs(root, 0)

        return res

