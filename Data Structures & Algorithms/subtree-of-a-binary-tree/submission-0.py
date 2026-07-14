class Solution:
    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode]
    ) -> bool:

        def same_tree(node1, node2) -> bool:
            # Both ended at the same time
            if not node1 and not node2:
                return True

            # Only one ended
            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False

            return (
                same_tree(node1.left, node2.left)
                and same_tree(node1.right, node2.right)
            )

        if not subRoot:
            return True

        if not root:
            return False

        if same_tree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )