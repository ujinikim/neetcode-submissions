# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(maxVal, root):

            if not root:
                return 0

            max_val = max(maxVal, root.val)
            dfs_sum = dfs(max_val, root.left) +dfs(max_val, root.right)

            if maxVal <= root.val:
                return 1 + dfs_sum
            else:
                return dfs_sum
        
        return dfs(-2 ** 31, root)
