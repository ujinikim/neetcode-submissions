# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        lst = []
        while stack:
            root, v = stack.pop(), visit.pop()
            if root:
                if not v:
                    # add back in with true visit
                    stack.append(root)
                    visit.append(True)
                    stack.append(root.right)
                    visit.append(False)
                    stack.append(root.left)
                    visit.append(False)
                else:
                    lst.append(root.val)
        return lst

