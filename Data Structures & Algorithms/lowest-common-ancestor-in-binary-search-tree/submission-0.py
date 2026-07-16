class Solution:
    def lowestCommonAncestor(
        self,
        root: TreeNode,
        p: TreeNode,
        q: TreeNode
    ) -> TreeNode:

        # node value -> parent value
        parents = {root.val: None}

        # node value -> actual node in the tree
        nodes = {}

        def dfs(node, parent):
            if not node:
                return

            nodes[node.val] = node
            parents[node.val] = parent.val if parent else None

            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        ancestors = set()

        current = p.val

        # Include p itself
        while current is not None:
            ancestors.add(current)
            current = parents[current]

        current = q.val

        while current not in ancestors:
            current = parents[current]

        return nodes[current]