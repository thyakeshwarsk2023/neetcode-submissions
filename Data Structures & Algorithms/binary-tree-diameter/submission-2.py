class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def get_height(node : Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = get_height(node.left)
            right = get_height(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left,right)

        get_height(root)

        return self.diameter    