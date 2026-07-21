# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        s = deque()
        s.append(root)
        res = [root.val]
        
        while s:
            temp = deque()
            while s:
                nd = s.popleft()
                
                if nd.right:
                    temp.append(nd.right)
                if nd.left:
                    temp.append(nd.left)
            
            if temp:
                res.append(temp[0].val)
            s = temp
            

        return res



            
            
    
