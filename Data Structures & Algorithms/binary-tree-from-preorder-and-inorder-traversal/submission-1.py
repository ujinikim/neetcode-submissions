class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        positions = {val: i for i, val in enumerate(inorder)}
        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_val = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_val)
            root_index = positions[root_val]

            root.left = build(left, root_index - 1)
            root.right = build(root_index + 1, right)

            return root

        return build(0, len(inorder) - 1)
