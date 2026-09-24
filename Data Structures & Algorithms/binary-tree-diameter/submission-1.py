class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def get_height(node : Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            self.diameter = max(self.diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        get_height(root)

        return self.diameter
